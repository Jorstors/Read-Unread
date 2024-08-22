# Gmail Unread Email Reader
This project is a Python script that uses the Gmail API to list the subjects and snippets of unread emails. The results are printed to the terminal and saved to a file (unread.csv).


## Requirements
- Python 3.x
- Pip (Python package installer)
- A Google account with Gmail enabled

## Setup
### 1. Clone the Repository
```
git clone https://github.com/Jorstors/read_unread.git
cd read_unread
```

### 2. Install Dependencies
Install the required Python packages:
```
pip install -r requirements.txt
```

### 3. Create Google Cloud Project and Enable Gmail API
- Go to the Google Cloud Console.
- Create a new project.
- Enable the Gmail API for your project.
- Create OAuth 2.0 credentials and download the credentials.json file.
- Place the credentials.json file in the root directory of this project.

### 4. Authenticate with Gmail
The first time you run the script, you'll be prompted to authenticate with your Google account. The script will generate a token.json file to store your access and refresh tokens for future use.

Running the Script
To run the script and fetch unread emails:

```
python listUnread.py
```
The script will output the subjects and snippets of your unread emails to the terminal and save them to unread_emails.txt.

## Output
- Terminal: The script prints the subjects and snippets of unread emails.
- File: The script saves the output to unread.csv in the root directory.

## Security Considerations
Do not share your credentials.json or token.json files. These files contain sensitive information that can grant access to your Gmail account.
