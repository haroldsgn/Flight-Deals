import smtplib
from twilio.rest import Client

TWILIO_SID = "ACa3598ab989072b5fdf81c3f507bc7ce2"
TWILIO_AUTH_TOKEN = "1e8feb09e611be206f0a18a9f0dd025a"
TWILIO_VIRTUAL_NUMBER = "+18148139711"
TWILIO_VERIFIED_NUMBER = "+573142261859"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "teinsteim@gmail.com"
MY_PASSWORD = "tncjycvovhunvgob"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )