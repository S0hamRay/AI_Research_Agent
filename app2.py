import os
from ingest2 import process_documents
from query2 import create_qa_chain, query_knowledge_base
import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
our_email = 'your_email@gmail.com'

def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
service = gmail_authenticate()

def build_message(destination, obj, body):
    message = MIMEText(body)
    message['to'] = destination
    message['from'] = our_email
    message['subject'] = obj
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, destination, obj, body):
    return service.users().messages().send(
      userId="me",
      body=build_message(destination, obj, body)
    ).execute()



def search_email_by_subject(service, subject):
    # Search for emails with the given subject
    result = service.users().messages().list(userId='me', q=f'subject:"{subject}"').execute()
    messages = result.get('messages', [])
    
    if not messages:
        print("No email found with subject:", subject)
        return None

    # Get the first (most recent) email matching the subject
    msg_id = messages[0]['id']
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    
    # Extract email content
    payload = msg.get('payload', {})
    headers = payload.get('headers', [])
    parts = payload.get('parts', [])

    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), None)
    sender = next((h['value'] for h in headers if h['name'] == 'From'), None)

    # Try to find the plain text part
    body = ""
    for part in parts:
        if part['mimeType'] == 'text/plain':
            data = part['body']['data']
            body = urlsafe_b64decode(data).decode('utf-8')
            break

    return {
        'subject': subject,
        'from': sender,
        'body': body
    }

from_email = ""
subject = ""
body = ""

# Example usage
email_data = search_email_by_subject(service, "THIS EMAIL")
if email_data:
    from_email = email_data['from']
    subject = email_data['subject']
    body = email_data['body']
    print("From:", email_data['from'])
    print("Subject:", email_data['subject'])
    print("Body:", email_data['body'])


OPENAI_API_KEY="completely_legitimate_api_key"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Check if database exists, if not create it
db_dir = './data/chroma_db'

if not os.path.exists(db_dir):
    print("No existing database found. Processing documents...")
    process_documents()

# Create QA chain once
qa_chain = create_qa_chain()

print("Welcome to your Personal Knowledge Base Assistant!")
print("Type 'exit' to quit or 'refresh' to update the knowledge base.")

user_input = "you are an AI assistant for Soham. Begin your answer by telling people that and then proceed. Refer to Soham in the third person. Also end answers like you're signing off on an email, your name is Soham's Assistant. Make sure to leave a line before you sign your name. All the documents you refer to are related to Soham's work so refer to them as such. Make sure you discuss ALL the documents if none are mentioned in specific. Respond charismatically. " + body


if user_input.lower() == 'refresh':
    print("Refreshing knowledge base...")
    process_documents()
    qa_chain = create_qa_chain()
    print("Knowledge base refreshed!")
else:
    print("\nSearching your knowledge base...")
    result = query_knowledge_base(user_input, qa_chain)
    
    print("\nAnswer:", result["answer"])
    
    # Print sources if available
    if result["sources"]:
        print("\nSources:")
        for i, source in enumerate(result["sources"], 1):
            if 'source' in source:
                print(f"{i}. {source['source']}")

send_message(service, from_email, "Reply from Soham (Definitely not AI)", 
        result["answer"])


