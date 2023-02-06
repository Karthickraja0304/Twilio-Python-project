import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, Response, request
from dotenv import load_dotenv

#we are first loading the environment variables
load_dotenv()


# use .env files to change the env variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')


client = Client(account_sid, auth_token)


app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_reply():

    """This is the main function of this project which takes in sms and responds appropriately"""

    try:
        body = request.values.get('Body').lower()
        #getting string from Body
        message = ''

        #jus for our reference
        print(f'This is in body :--{body}--')

        #creating object of MessagingResponse
        resp = MessagingResponse()
        
        #conditonal statements for appropriate response
        if body == 'y':
            message = "Thank you"
        
        elif body == 'n':
            message = "Sounds good"


        #now this portion of code responds to sms from client with 'message' based on client sms
        # reply sms code is same as in send_only_app.py        
        message = client.messages.create(
                                # body - 'Takes in the message part we need to send'
                                body=message,
                                
                                #from -  'will be your Twilio phone number'
                                from_='+12526506681',

                                #to -  'will be the mobile to which the message from body need to be sent'
                                to= '+919952014523'
                                )

        resp.message(message)
        return Response(str(resp), mimetype="application/xml")
    
    except Exception as e:
        print(e)
        return Response(str(e), mimetype="application/xml")


@app.route("/sms", methods=['GET'])
def sms_get():
    try:
        
        resp = MessagingResponse()

        resp.message("Welcome")

        return Response(str(resp), mimetype="application/xml")
    
    except Exception as e:
        print(e)
        return Response(str(e), mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
