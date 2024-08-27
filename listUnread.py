import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(userId="me", labelIds=["UNREAD"]).execute()
    emails = results.get("messages", [])

    if not emails:
      print("No emails found.")
      return
    
    print("Reading emails...")

    emailCount = 0
    with open("unread.csv", "w", encoding="utf-8") as f:
      for email in emails:
        emailCount+=1
        eml = service.users().messages().get(userId="me", id=email["id"]).execute()

        for header in eml['payload']['headers']:
          if header['name'] == 'Subject':
            subject = header['value']
            break
        
        snippet = eml.get('snippet', '')

        print(f"Subject: {subject}\nSnippet: {snippet}\n\n")
        f.write(f"Subject: {subject}\nSnippet: {snippet}\n\n")
      
      print(f"Found {emailCount} unread emails.")
      f.write(f"Found {emailCount} unread emails.")

      print("\nCSV file created in directory.")

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()