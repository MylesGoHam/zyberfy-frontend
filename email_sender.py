import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# 🔐 Paste your actual SendGrid API key and verified sender email below
SENDGRID_API_KEY = "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"  # Replace with your real key
FROM_EMAIL = "hello@zyberfy.com"  # Must be verified in SendGrid

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
        "your_personal_email@gmail.com",  # ← Change to a real test inbox you own
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 🚀"
    )
