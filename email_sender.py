import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "your_real_api_key"  # Replace with your actual SendGrid key
FROM_EMAIL = 'your_verified@zyberfy.com'     # Replace with your verified SendGrid sender
TO_EMAIL = 'your_email@gmail.com'            # Replace with your email to receive the test

def send_email(to_email, subject, message):
    mail = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=message
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(mail)
        print(f"✅ Email sent to {to_email} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_email(TO_EMAIL, "Welcome to Zyberfy!", "This is a test email from the future 🔮")
