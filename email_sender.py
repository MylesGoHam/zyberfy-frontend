import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Paste your actual SendGrid API key and verified sender email below
SENDGRID_API_KEY = "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"
FROM_EMAIL = "hello@zyberfy.com"  # This is the sender email

def send_email(to_email, subject, message):
    # Create email object
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=message
    )

    try:
        # Initialize SendGrid client with your API key
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        # Send email
        response = sg.send(email)
        print(f"Email sent to {to_email} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"X Error sending email: {e}")

if __name__ == "__main__":
    # Replace with actual subject and message
    send_email(
        "mylescunningham0@gmail.com",  # Recipient email
        "Welcome to Zyberfy!",  # Subject
        "This is a test email from Zyberfy!"  # Message
    )
