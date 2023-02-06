# Twilio Python Library
A Python library for communicating with the Twilio API and generating TwiML.

## Installation

    pip install twilio

## Usage

    from twilio.rest import Client
    # Your Account SID and Auth Token from twilio.com/console
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Hello from Python",
                     from_='your_twilio_number',
                     to='destination_number'
                 )
    print(message.sid)
