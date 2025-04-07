import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your real values
SENDGRID_API_KEY = "your_real_api_key_here"
FROM_EMAIL = "your_verified_email@zyberfy.com"

def send_email(to_email, subject, message):
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=message
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(email)
        print(f"✅ Email sent to {to_email} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_email(
        "your_email@yourdomain.com",  # ← your real test email goes here
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 🚀"
    )
