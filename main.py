from flask import Flask
from twilio.rest import Client


app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = "AC56409d1a92925652258306a3d332aa6e"
# Your Auth Token from twilio.com/console
auth_token = "6bbfaef7cee22796c0e3145557c79dfb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
