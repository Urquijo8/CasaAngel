# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import serial
import time
import web
import os
import pyautogui
ser = serial.Serial('COM4', 9600)
time.sleep(10)



# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC058de48cd75a5c0d56ac80581bcbb341'
auth_token = 'df09bab6753aade7f6f33f064d1a09c9'
client = Client(account_sid, auth_token)
print("Alarma Activada")
while True:
    while ser.inWaiting():
        a=ser.readline()
        print(a)
        if a:
                            
            messageTosend="Alerta!!! Intruso detectado"
            message = client.messages.create(
                                body=messageTosend,
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+5213320114623'
                            )
            web.mail()
            a = ""           
            print("Intruso")
            print(message.sid)


