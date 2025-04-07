import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load from env or directly paste your key here for now
SENDGRID_API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your real key
FROM_EMAIL = 'yourname@zyberfy.com'     # Replace with your verified sender email

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
        print(f"Email sent to {to_email} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Test it
if __name__ == "__main__":
    send_email("test@example.com", "Welcome to Zyberfy!", "This is a test email from Zyberfy 🚀")