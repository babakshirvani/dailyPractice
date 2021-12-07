import yagmail
from decouple import config


sender = config('SENDER')
receiver = config('RECEIVER')

subject = "This is the Subject"

contents = ["""
Here is the content of the email!!!
Hi!
""", 'text.txt']

yag = yagmail.SMTP(user=sender, password=config('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email sent!!!")
  
