from exchangelib import \
    FileAttachment, ItemAttachment, Message, CalendarItem, HTMLBody, \
    DELEGATE, Account, Credentials, Folder
import os.path

# Login details for email connection + folder name, configured in emaildetails.txt
getEmailDetails = open('emaildetails.txt', 'r')
temp = getEmailDetails.read().splitlines()
emailuser = temp[0]
emailpass = temp[1]
foldername = temp[2]
mailsender = temp[3]

#Connect to autodiscovery to connect to exchange server
credentials = Credentials(emailuser, emailpass)
account = Account(
    primary_smtp_address='rliu@luxoft.com',
    credentials=credentials,
    autodiscover=True,
    access_type=DELEGATE
)

folderlookup = account.root; 'Some Folder'

# Print all attachments in folder
for item in folderlookup.glob(foldername).all():
    if item.sender.name == mailsender:
        for attachment in item.attachments:
            if isinstance(attachment, FileAttachment):
                local_path = os.path.join('./attachments', attachment.name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                print('Saved attachment to', local_path)
            elif isinstance(attachment, ItemAttachment):
                if isinstance(attachment.item, Message):
                    print(attachment.item.subject, attachment.item.body)

