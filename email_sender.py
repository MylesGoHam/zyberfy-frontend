import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your actual SendGrid API key and verified sender email
SENDGRID_API_KEY = "SGSG.8vq_cVTlRe6NYULvDj3x3w._aSVmCB-FYjzbftDcgKnoozXakqFSm2sMw-w-K0cZvg"
FROM_EMAIL = "yourname@zyberfy.com"  # Use your verified sender address

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
        "test@example.com",  # Replace with your actual test email
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 🚀"
    )
