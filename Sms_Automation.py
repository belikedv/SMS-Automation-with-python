import requests
import json
import pandas as pd

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

df = pd.read_excel('contacts.xlsx')
contact = df['Contacts'].values

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
for tel in contact
    response = sendPostRequest(URL, 'API-KEY', 'SECRET-KEY', 'stage', tel , 'email-logined', 'Text message' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)