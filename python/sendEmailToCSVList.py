import yagmail
from decouple import config
import pandas

sender = config('SENDER')
subject = "This is the Subject CSV"

df = pandas.read_csv('contacts.csv')

for inex, row in df.iterrows():
  contents = f"""
  Hi {row['name']}!
  Here is the content of the email!!!
  """
  print(row['email'])
  # yag = yagmail.SMTP(user=sender, password=config('PASSWORD'))
  # yag.send(to=row['email'], subject=subject, contents=contents)
  # print("Email sent!!!")

