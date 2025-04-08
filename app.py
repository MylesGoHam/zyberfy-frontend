dGrid API client
sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

# Create email components
from_email = Email(SENDER_EMAIL)  # Replace with your sender email
to_email = To(email)  # Send the email to the user who submitted the form
subject = f"Proposal for {service} Service"
content = Content("text/plain", f"""
Hello {name},

Thank you for your inquiry regarding our {service} service. Here is the proposal:
- Budget: {budget}
- Location: {location}
- Special Requests: {special_requests}

Best regards,
Zyberfy Team
""")

# Build and send the email
mail = Mail(from_email, to_email, subject, content)

try:
    response = sg.send(mail)
    print(f"Email sent successfully! Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {str(e)}")
