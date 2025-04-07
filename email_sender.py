import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your actual SendGrid API key and verified sender email
SENDGRID_API_KEY = "SG.xxxxxx...your_api_key_here"
FROM_EMAIL = "support@zyberfy.com"  # Use the verified email in your SendGrid account

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
        "your_email@yourdomain.com",  # ← test email goes here
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 🚀"
    )
