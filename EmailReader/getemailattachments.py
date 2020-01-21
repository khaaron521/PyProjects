import email
import getpass, imaplib
import os
import sys

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

# Server: outlook.office365.com
# Port: 993
# Encryption: TLS

# Server: owa.luxoft.com
# Port: 443
# Encryption: SSL

userName = 'aaron.521@hotmail.com'
passwd = 'microsofthearts123'
Folder = 'Archive'

imapSession = imaplib.IMAP4_SSL('outlook.office365.com')
typ, accountDetails = imapSession.login(userName, passwd)
if typ != 'OK':
    raise Exception('Unable to sign in')

imapSession.select(Folder)
typ, data = imapSession.search(None, 'ALL')
if typ != 'OK':
    raise Exception('Cant find folder')

# Iterating over all emails
for msgId in data[0].split():
    typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
    if typ != 'OK':
        raise Exception('Incorrect data')

    rawemailBody = messageParts[0][1]
    emailBody = rawemailBody.decode('utf-8')
    mail = email.message_from_string(emailBody)
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            # print part.as_string()
            continue
        if part.get('Content-Disposition') is None:
            # print part.as_string()
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(detach_dir, 'attachments', fileName)
            if not os.path.isfile(filePath) :
                print(fileName)
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
imapSession.close()
imapSession.logout()
