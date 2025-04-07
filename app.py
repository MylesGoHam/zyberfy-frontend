from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
import os
import openai
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# 1. Load your .env file
load_dotenv()

# 2. Retrieve environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

app = Flask(__name__)

# In-memory storage for proposals (for testing)
proposal_logs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    budget = request.form.get('budget')
    location = request.form.get('location')
    special_requests = request.form.get('requests', '')

    # Compose a prompt
    prompt = (
        f"Generate a professional, elegant, and personalized proposal for a client:\n\n"
        f"Name: {name}\n"
        f"Service Type: {service}\n"
        f"Budget: {budget}\n"
        f"Location: {location}\n"
        f"Special Requests: {special_requests}\n\n"
        "The proposal should reflect a luxury service experience."
    )

    # Generate proposal with OpenAI
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )
        proposal_text = response.choices[0].text.strip()
    except Exception as e:
        return jsonify({"error": f"Error generating proposal: {str(e)}"}), 500

    # Send the email with SendGrid
    try:
        message = Mail(
            from_email=SENDER_EMAIL,
            to_emails=email,
            subject="Your Personalized Proposal from Zyberfy",
            html_content=(
                f"<p>Hi {name},</p>"
                "<p>Thank you for your inquiry. Please find your personalized proposal below:</p>"
                f"<p>{proposal_text}</p>"
                "<p>Best regards,<br>Zyberfy Team</p>"
            )
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        return jsonify({"error": f"Error sending email: {str(e)}"}), 500

    # Log the proposal (for now, stored in memory)
    proposal_logs.append({
        "name": name,
        "email": email,
        "service": service,
        "budget": budget,
        "location": location,
        "proposal": proposal_text
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
