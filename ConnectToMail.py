# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 08:08:42 2014

@author: wgillis
"""
import emailVariables as ev
import imaplib, email, os

FROM = 'danb@cns.bu.edu'
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(ev.BU_USER_NAME, ev.PASSWORD)
mail.select('INBOX')

result, data = mail.search(None, 'UNSEEN', 'FROM', '"{0}"'.format(FROM))
da = data[0].split()

if da:
    for i in da[:2]:
        result, d = mail.fetch(i, "(RFC822)")
        msg = email.message_from_string(d[0][1])
        mail.store(i, '+FLAGS', '\\Flagged')
        if msg.is_multipart():
            for part in msg.walk():
                c_type = part.get_content_type()
                if c_type =='application/pdf':
                    open(os.path.join(ev.DIRECTORY,part.get_filename()), 'wb').write(part.get_payload(decode=True))

mail.close()
mail.logout()