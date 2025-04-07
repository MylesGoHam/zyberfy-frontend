import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key and sender email from environment
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = "your_verified_sender@zyberfy.com"  # Replace with your verified sender email

# DEBUG: Check if API key is loaded properly
print("✅ API Key Loaded:", "Yes" if SENDGRID_API_KEY else "❌ No API key found")

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
        print(f"📬 Email sent to {to_email} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_email(
        "your_email@yourdomain.com",  # Replace with your actual test email
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 🚀"
    )
