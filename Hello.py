"""
Author:     Connor Perill
Program:    Hello - Testing that Flask is working correctly
Usage:      Repeats the user
                Functions:
                    

Lesson: n/a
"""

# Imports need, Flask is web framework for python
from flask import Flask, request
import json
import requests

app=Flask(__name__)

# Page access token that the Facebook App uses
PAT = 'EAACAFmJHCnYBALaqWcQC5bTtCkld5rQPhHeEveG6ytZBJh5UPydcyxTpEitVTNCqbPztvm5xkxWmBVkgk0NYRGcLHEgRpVGpwqvtjEFLb' \
      'SgLhBAXNH42f5ozx3ZAOnu7VIZCJ1kZBxSP5MqaPSVaiv9WT4my2LXpnV2SzxRz9gZDZD'

@app.route('/', methods=['GET'])    # Verify token created when we created app on Facebook, if it matches we return the
                                    # challenge back to Facebook
def handle_verification():
    print "Handling Verification"
    if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
        print "Verification Successful"
        return request.args.get('hub.challenge', '')
    else:
        print "Verification Failed!"
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])   #
def handle_messages():
    print "Handling Messages"
    payload = request.get_data()
    print payload
    for sender, message in messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)
        send_message(PAT, sender, message)
    return "ok"

def messaging_events(payload):
    """ Generate ruples of sender_id and message_text from payload provided 
    :param payload: 
    :return: 
    """

    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
        else:
            yield event["sender"]["id"], "I can't echo this lad"

def send_message(token, recipient, text):
    """
    Send the message text to person with id
    :param token: 
    :param recipient: 
    :param text: 
    :return: 
    """

    r = requests.post("https://graphs.facebook.com/v2.6/me/messages", #url, data, json, **kargs
                      params={"access_token": token},
                      data=json.dumps({
                          "recipient": {"id": recipient},
                          "message" : {"text": text.decode('unicode_escape')}
                      }),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text

if __name__ == '__main__':
    app.run()