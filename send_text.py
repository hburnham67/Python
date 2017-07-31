from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8b569c97049538fe62c0ea5cca790f33"
# Your Auth Token from twilio.com/console
auth_token  = "34f379dfc4add9ef9f5b355bcaff116d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19202036910", 
    from_="+19204724116",
    body="I know where the remote is")

print(message.sid)
