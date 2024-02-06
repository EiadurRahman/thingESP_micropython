import ujson as json
import network
import time
import usocket as socket
import machine
from machine import Pin
import ustruct
import os
import urequests as requests
# import sensor
from umqtt.simple import MQTTClient


thingesp_server = 'thingesp.siddhesh.me'

class Client:
    def __init__(self, username, projectName, password):
        self.username = username
        self.projectName = projectName
        self.password = password
        self.initalized = False
        self.mqtt_client = MQTTClient(client_id=projectName + "@" + username,
                                      server=thingesp_server, port=1893, user=projectName + "@" + username, password=password,keepalive=0)
        self.mqtt_client.set_callback(self.on_message)
        self.mqtt_client.connect()

        
    def setCallback(self, func):
        self.callback_func = func
        self.initalized = True
        return self

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to thingesp with result code ", rc)
        self.mqtt_client.subscribe(self.projectName + "/" + self.username)

    def on_message(self, client, msg):
        if self.initalized != True:
            print('Please set the callback func!')
            return
        else:
            payload = json.loads(msg.decode("utf-8"))
            print(payload)
            if payload['action'] == 'query':
                out = self.callback_func(payload['query'].lower()) or ""
                sendr = {
                    "msg_id": payload['msg_id'], "action": "returned_api_response", "returned_api_response": out}
                self.mqtt_client.publish(
                    self.projectName + "/" + self.username, json.dumps(sendr))

    def device_call(self, to_num, msg):
        out = {"action": "device_call", "to_number": to_num, "msg": msg}
        self.mqtt_client.publish(
            self.projectName+"/"+self.username, json.dumps(out))

    def start(self):
        self.mqtt_client.set_callback(self.on_message)
        self.mqtt_client.subscribe(self.projectName + "/" + self.username)
        while True:
            self.mqtt_client.check_msg()
            # Add other non-blocking operations here
            # For example, reading sensors, handling callbacks (shown in the main.py file), etc.
            time.sleep(0.1) # pro tip : play with this sleep function
            
#this part is to send messages from your ESP module
def send_msg(msg):
    # Your Twilio Account SID and Auth Token
    account_sid = 'account_sid'
    auth_token = 'auth_token'

    # Set up the Twilio API URL for sending WhatsApp messages
    twilio_url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(account_sid)

    # Set up the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Set up the request payload (message details)
    payload = {
        'To': 'whatsapp%3A%2B[your number with country-code]',  # Replace with the recipient's  WhatsApp number
        'From': 'whatsapp%3A%2B[Twilio WhatsApp number]',  # Replace with your Twilio WhatsApp number
        'Body': msg,  # Message content
    }

    # Manually create the payload string
    payload_string = '&'.join(['{}={}'.format(key, value) for key, value in payload.items()])

    # Send the request
    response = requests.post(twilio_url, headers=headers, auth=(account_sid, auth_token), data=payload_string)
    
    # you can print response to debug  

    print('done sending msg : %s' %msg)




