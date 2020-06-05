import os
from twilio.rest import Client

# setTwilioEnvVariables
account_sid = os.environ['TWILIOACCOUNTSID']
auth_token = os.environ['TWILIOAUTHTOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="Luke, I am your father",
                              from_='+12055709445',
                              to='+19022929294'
                          )

print(message.sid)
