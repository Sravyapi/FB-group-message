#To encode your password
import base64
encoded = base64.b64encode(b'<enter your FB password here>')
print(encoded)
data = base64.b64decode(encoded)
print(data.decode("utf-8"))


#Send a message to a group of people via FB chat

from getpass import getpass
from fbchat import Client

encoded_password = base64.b64decode(b'<encoded password here>')
client = Client('<enter your email id here>', encoded_password.decode("utf-8"))
msg = str(input("Message: "))
FriendName = str(input("FriendName: "))
while(FriendName):
    friends = client.searchForUsers(FriendName) 
    friend = friends[0]
    sent = client.send(Message(text= msg), thread_id= friend.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")
    FriendName = str(input("FriendName: "))
