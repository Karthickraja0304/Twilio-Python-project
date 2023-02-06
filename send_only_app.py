import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# use .env files to change the env variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        # body - 'Takes in the message part we need to send'
        body="Hello customer",
        
        #from -  'will be your Twilio phone number'
        from_='+12526506681',

        #to -  'will be the mobile to which the message from body need to be sent'
        to='+919952014523'
    )

print('Message sent successfully')