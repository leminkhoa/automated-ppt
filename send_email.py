import sys
import pendulum
from helpers.email_actions import send_email

today = pendulum.now("Asia/Bangkok").to_date_string()

user, pwd, recipient = sys.argv[1:]
subject = f'Gold Price Report - date {today}'
body = 'Hi, Khoa ! Your daily report is ready to serve'
attachment_path = 'output/report.pptx'
attachment_name = f'Gold Price Report_date_{today}.pptx'


send_email(user, pwd, recipient, attachment_path, attachment_name, subject, body)