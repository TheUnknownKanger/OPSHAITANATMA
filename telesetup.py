from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print(""" Welcome To OP SHAITAN String Generator By SHAITAN""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = '1524422'
API_HASH = "5c6bfcc9415ac5bda5fa03df2dec5c8e"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` And Ask ShaitanFor Any Help !")
      print("You telegram String session successfully stored in your telegram, please check your Telegram Saved Messages ")
      print("Store it safe !!")
      print("Thanks For Choosing LEGEND Service. Hope that You will Have a Goodtime With Us!....)
  except:
   print ("")
   print ("Wrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry")
   print ("")
   continue
  break
