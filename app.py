from flask import Flask, request, render_template
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app (Ensure this line is here)
app = Flask(__name__)

# Initialize SendGrid API Client
sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))

# Import and configure CORS
from flask_cors import CORS
CORS(app)  # This will allow all origins by default

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    # Debugging: Print received data
    print("Received POST request:")
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    budget = request.form.get('budget')
    location = request.form.get('location')
    special_requests = request.form.get('requests')

    # Debug print statements
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Service: {service}")
    print(f"Budget: {budget}")
    print(f"Location: {location}")
    print(f"Special Requests: {special_requests}")

    # Send email using SendGrid
    from_email = Email(os.getenv("SENDER_EMAIL"))
    to_email = To(email)
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

    return "Proposal submitted successfully!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Ensure this line is here
