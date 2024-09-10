# Read "Unread" Emails via Gmail API

This project is a simple Python application that interacts with the Gmail API to list unread emails in your inbox. It is a learning project and marks the first attempt at using an API for handling Gmail messages.

## Project Structure

- **listUnread.py**: The main Python script that interacts with the Gmail API to list unread emails and save the information to a CSV file.
- **credentials.json**: Contains the OAuth2 credentials required to access the Gmail API.
- **token.json**: Stores the OAuth2 access and refresh tokens, used to authenticate API requests.
- **unread.csv**: Output file where the script saves the list of unread emails.
- **requirements.txt**: Lists the Python packages required to run the project.
- **.gitignore**: Specifies the files to ignore in version control (e.g., credentials and token files).

## Features

- Lists unread emails from the Gmail inbox.
- Saves the list of unread emails to a CSV file.
- Simple OAuth2 flow using Google's API to authenticate the user.

## Technologies

This project leverages the following technologies:
- **Python**: The core programming language used to write the script.
- **Google Gmail API**: The API used to fetch unread emails from your Gmail inbox.
- **OAuth2**: Used for secure authentication with Google’s API.
- **CSV**: The output format for storing email data.
- **Google API Client Libraries**: Python libraries that facilitate interaction with Google’s services.

## Prerequisites

- Python 3.x
- Gmail account with API access enabled.
- Enable Gmail API and create credentials (OAuth2) for the project via Google Cloud Console.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/unread-emails.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your OAuth2 credentials in the `credentials.json` file. The file should contain your Gmail API credentials.

4. Run the script to list unread emails:
    ```bash
    python listUnread.py
    ```

5. The script will output the unread emails to `unread.csv`.

## Usage

1. **Authentication**: On the first run, the script will prompt you to log in to your Gmail account and grant access to the Gmail API. Once authenticated, a `token.json` file will be generated to store access tokens, so you won't need to log in every time.
   
2. **Fetching Emails**: The script will automatically fetch unread emails from your inbox and save them to `unread.csv`. You can view this CSV file for details like email subjects and senders.

3. **Regenerating Access**: If your access token expires, the script will refresh it automatically using the `token.json` file.

## Dependencies

The project uses the following Python packages, as specified in `requirements.txt`:
- `google-api-python-client`
- `google-auth`
- `google-auth-httplib2`
- `google-auth-oauthlib`
- `httplib2`
- `requests`
- `oauthlib`
- `uritemplate`

These packages handle the API interactions, authentication, and HTTP requests.

## Troubleshooting

- **Invalid Credentials**: Make sure you have correctly set up the `credentials.json` file from Google Cloud Console.
- **Expired Token**: If the access token in `token.json` has expired, the script will refresh it automatically. If that doesn’t work, try deleting `token.json` and re-running the script to authenticate again.
- **Permission Issues**: Ensure that you have granted the required permissions when first prompted by Google’s OAuth2.

### License

This project is licensed under the ISC License:

Copyright (c) 2024, Justus Jones

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

---

Made by [Justus Jones](https://github.com/Jorstors)
