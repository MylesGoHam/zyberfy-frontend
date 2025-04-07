import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Paste your actual SendGrid API key and verified sender email below
SENDGRID_API_KEY = "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"
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

        # If email is successfully sent
        if response.status_code == 202:
            print("Success! Email has been delivered.")
        else:
            print(f"Error: Something went wrong. Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_email(
        "recipient_email@example.com",  # Replace with the email you want to send to
        "Welcome to Zyberfy!",  # Subject
        "This is a test email from Zyberfy"  # Message content
    )
