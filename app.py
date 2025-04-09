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
        try:
            # Get form data
            email = request.form.get("email")
            service = request.form.get("service")
            budget = request.form.get("budget")
            location = request.form.get("location")
            
            # Print form data for debugging
            print(f"Email: {email}, Service: {service}, Budget: {budget}, Location: {location}")
            
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
        
        except Exception as e:
            # If an error occurs, catch it and print it in the console for debugging
            print(f"Error: {e}")
            return f"An error occurred: {e}"
    
    return render_template("index.html")

def send_email(subject, content):
    try:
        from_email = Email("hello@zyberfy.com")
        to_email = To("mylescunningham0@gmail.com")
        content = Content("text/plain", content)
        mail = Mail(from_email, to_email, subject, content)

        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        response = sg.send(mail)
        
        # Debugging output
        print(f"SendGrid Response: {response.status_code}")
        print(f"Response Body: {response.body}")
        print(f"Response Headers: {response.headers}")
    
    except Exception as e:
        # Catch any exceptions in sending the email
        print(f"SendGrid error: {e}")
        raise e  # Re-raise the error to be caught in the index route

if __name__ == "__main__":
    app.run(debug=True)
