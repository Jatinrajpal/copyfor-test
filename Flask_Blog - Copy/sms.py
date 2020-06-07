# PJWli8WnceU-tWPszSeAWo6sIHpFYvuGO2pHY2NKqh
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
import urllib.request
import urllib.parse
import random
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
resp =  sendSMS('PJWli8WnceU-tWPszSeAWo6sIHpFYvuGO2pHY2NKqh', '919079932715',
    'TXTLCL', 'Your Verification code is '+str(otp))
print (resp)