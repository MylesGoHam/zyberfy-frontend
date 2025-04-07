import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# 🔐 Paste your actual SendGrid API key and verified sender email below
SENDGRID_API_KEY = "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"  # Replace with your real key
FROM_EMAIL = "hello@zyberfy.com"  # Must be verified in SendGrid

dsend_email(mylescunninghamlesingham@gmail.com, "Hi", "Hello:")
    email = Mail(
        from_email=hello@zyberfy.com,
        to_emails=mylescunnigham0@gmail.com,
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
        "hello@zyberfy.com",  # ← Change to a real test inbox you own
        "Welcome to Zyberfy!",
        "This is a test email from Zyberfy 🚀"
    )
