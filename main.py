from flask import Flask, request, session
from twilio import twiml
from twilio.rest import TwilioRestClient 
from analyze import analyzeMsg
import string

SECRET_KEY = 'randomshit'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    userInput = request.values.get('Body', None).lower().strip()

    userInput = [userInput.strip(string.punctuation) for x in userInput.split()][0]
    # session.clear()

    # Increment the counter
    counter = session.get('counter', 0)
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    # put your own credentials here 
    ACCOUNT_SID = "AC56409d1a92925652258306a3d332aa6e" 
    AUTH_TOKEN = "6bbfaef7cee22796c0e3145557c79dfb" 
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

    # Build our reply
    message = analyzeMsg(userInput, counter, session)

    response = "<?xml version='1.0' encoding='UTF-8'?><Response><Message>" + message + "</Message></Response>"
    return response

if __name__ == '__main__':
    app.run(debug=True)