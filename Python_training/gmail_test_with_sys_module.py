import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

'''
#this will work for sending only message
FROM = 'prashanthx.adaveni@intel.com'
TO = ['prashanthx.adaveni@intel.com'] # must be a list
TYPE_REG = "TYPE_REG"
Model_Path = "Model_Path"
elab_cmd = "elab_cmd"
 
SUBJECT = "Dummy Trail Mail1"

TEXT = "Hi,\n\nInitiated Elab for:- "+TYPE_REG+"\nModel Path:- " + Model_Path + "\nElab Command:- " + elab_cmd + "\n\n*****Elab Failed*****\n\n Failing log path:- " + Model_Path + "\n\nThanks!"
 
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

'''



FROM = 'prashanthx.adaveni@intel.com'
TO = ['prashanthx.adaveni@intel.com'] # must be a list

 
SUBJECT = "PTL hierarchy attachment"

TEXT = "Hi,\n\n i am sending "+sys.argv[1]+" \n\nThanks!"

#This will work for attachment
#Setup the MIME
message = MIMEMultipart()
message['From'] = FROM
message['To'] = ",".join(TO)
message['Subject'] = SUBJECT

#The body and the attachments for the mail
message.attach(MIMEText(TEXT, 'plain'))
if len(sys.argv) >= 2:
    attach_file_name = sys.argv[1]
else:
    attach_file_name = 'gmail_test.py'

attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
message = message.as_string()




# Send the mail
server = smtplib.SMTP()

server.connect()

server.sendmail(FROM, TO, message)

server.quit()


