from flask import Flask, request, render_template
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# SendGrid setup
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        email = request.form.get("email")
        service = request.form.get("service")
        budget = request.form.get("budget")
        location = request.form.get("location")
        
        # Print data for debugging
        print(f"Email: {email}")
        print(f"Service: {service}")
        print(f"Budget: {budget}")
        print(f"Location: {location}")
        
        # Create email content
        subject = f"New request for {service}"
        content = f"""
        Name: {email}
        Service: {service}
        Budget: {budget}
        Location: {location}
        """
        
        # Send email through SendGrid
        send_email(subject, content)
        
        return "Email sent successfully!"
    return render_template("index.html")

def send_email(subject, content):
    from_email = Email("your_verified_email@domain.com")
    to_email = To("recipient_email@domain.com")
    content = Content("text/plain", content)
    mail = Mail(from_email, to_email, subject, content)

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    response = sg.send(mail)
    
    print(f"SendGrid Response: {response.status_code}")
    print(f"Response Body: {response.body}")
    print(f"Response Headers: {response.headers}")

if __name__ == "__main__":
    app.run(debug=True)
