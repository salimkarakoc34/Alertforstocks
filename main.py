import twilio
import os
from twilio.rest import Client
import news
import stocksapi


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC4eaf0dcf50cdbbbe7d9f6e42f67bb1bb"
auth_token = "b1f395c83629a12c9bc6d9263b819208"
client = Client(account_sid, auth_token)

if stocksapi.percentage>0.5:
  message = client.messages.create(
  body=f"{news.message}",
  from_="+18507539690",
  to="+12066876856")
else:
  print('error ')