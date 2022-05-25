from crypt import methods
import os
from pprint import pprint
from flask import Flask
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message("PANIK")

    return str(resp)
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']

    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body='Smells like upgamers in here',
    #     from_='+19378074692',
    #     to='+12487528167'
    # )

if __name__ == "__main__":
    app.run(debug=True)