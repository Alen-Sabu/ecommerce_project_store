# import os
# from twilio.rest import Client
# from twilio.base.exceptions import TwilioRestException

# client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
# verify = client.verify.services(os.environ['TWILIO_VERIFY_SERVICE_SID'])


# def send(phone):
#     verify.verifications.create(to=phone, channel='sms')


# def check(phone, code):
#     try:
#         result = verify.verification_checks.create(to=phone, code=code)
#     except TwilioRestException:
#         print('no')
#         return False
    
#     return True



import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

TWILIO_VERIFY_SERVICE_SID = 'VA89dc7b5b5b751bc6c7aa70bc54dcc8b2'
TWILIO_ACCOUNT_SID = 'ACef56b41be68c1347d110597aee7e1118'
TWILIO_AUTH_TOKEN = 'e2de8e4540a49c6bc5ec56b488d446ae'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
verify = client.verify.services(TWILIO_VERIFY_SERVICE_SID)



def send(phone):
    verify.verifications.create(to=phone, channel='sms')


def check(phone, code):
    try:
        result = verify.verification_checks.create(to=phone, code=code)
    except TwilioRestException:
        print('no')
        return False
    
    return True