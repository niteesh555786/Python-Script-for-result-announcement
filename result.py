from twilio.rest import Client #SMS API Package
import urllib.request as urllib2
import re
import os
import time
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

account_sid = "your id" #Your Twilio account ID
auth_token = "your apitoken"    #Your secret API Token
 
client = Client(account_sid, auth_token)
 
while 1:
 
    html_content = urllib2.urlopen('http://results.unipune.ac.in/').read().decode('utf-8') 
 
    matches_2012 = re.findall('TE2012', html_content);
    matches_2014 = re.findall('TE2014', html_content);
    matches_2008 = re.findall('TE2008', html_content);  
 	
    if ((len(matches_2008) == 0) and (len(matches_2012) == 0) and (len(matches_2014) == 0)) :       
       print("notify-send 'Yeah' 'Result is not declared yet'")
       time.sleep(9)
 
    else:
       msg = client.messages.create(to="yournumber", from_="twilio_number", body="Jai Mata Di !! RESULT AAGYA") #Will send SMS to your phone number
       print ("SMS Sent")
       quit()