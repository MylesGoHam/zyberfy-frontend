import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Your real API key and verified sender email
SENDGRID_API_KEY = "SSG.OIchAJn-TZOJ1kbCeAf83g.n-5hVrweXtPl8FI6OqP3XzNtHRkB1tYS0htORbr7ji8"  # paste your actual API key here
FROM_EMAIL = "hello@zyberfy.com"

def send_email(to_email, subject, message):
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=message,
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(email)
        print(f"✅ Email sent to {to_email} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_email(
        "your_email@yourdomain.com",  # replace with your real destination email
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 💌"
    )
