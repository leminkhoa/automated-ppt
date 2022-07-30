import smtplib
from email.message import EmailMessage

def send_email(user, pwd, recipient, attachment_path, attachment_name , subject='', body=''):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = recipient
    msg.set_content(body)
    
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="pptx", filename=attachment_name)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.send_message(msg)
        server.close()
        print('successfully sent the email')
    except Exception as e:
        print("failed to send email")
        print(e)