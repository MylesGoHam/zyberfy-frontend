from flask import Flask, request, render_template
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize SendGrid API client
sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    # 1. Extract form data
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    budget = request.form.get('budget')
    location = request.form.get('location')
    special_requests = request.form.get('requests')

    # 2. Debug: Print received data to terminal
    print(f"Received Proposal Request:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Service: {service}")
    print(f"Budget: {budget}")
    print(f"Location: {location}")
    print(f"Special Requests: {special_requests}")

    # 3. Send email using SendGrid
    from_email = Email(os.getenv("SENDER_EMAIL"))  # Your email address
    to_email = To(email)  # Email entered by the user
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

    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.send(mail)
        print(f"Email sent successfully! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

    return 'Proposal submitted successfully!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
