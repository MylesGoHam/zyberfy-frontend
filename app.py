from flask import Flask, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
import os
import openai
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys (dummy keys are fine for now)
openai.api_key = os.getenv("OPENAI_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

app = Flask(__name__)

# In-memory storage for proposal logs (for testing)
proposal_logs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    print("Submit proposal route triggered!")

    # Extract form data
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    budget = request.form.get('budget')
    location = request.form.get('location')
    special_requests = request.form.get('requests', '')

    # --- For Testing: Commented Out API Calls ---
    # The following code is commented out because you're using dummy keys.
    # Once you have actual keys, you can uncomment these lines.
    #
    # try:
    #     prompt = (
    #         f"Generate a professional, elegant, and personalized proposal for a client with the following details:\n\n"
    #         f"Name: {name}\n"
    #         f"Service Type: {service}\n"
    #         f"Budget: {budget}\n"
    #         f"Location: {location}\n"
    #         f"Special Requests: {special_requests}\n\n"
    #         "The proposal should reflect a luxury service experience."
    #     )
    # 
    #     response = openai.Completion.create(
    #         engine="text-davinci-003",
    #         prompt=prompt,
    #         max_tokens=300,
    #         temperature=0.7
    #     )
    #     proposal_text = response.choices[0].text.strip()
    # except Exception as e:
    #     print("OpenAI error:", e)
    #     proposal_text = "Default proposal text due to error."
    # 
    # try:
    #     message = Mail(
    #         from_email=SENDER_EMAIL,
    #         to_emails=email,
    #         subject="Your Personalized Proposal from Zyberfy",
    #         html_content=(
    #             f"<p>Hi {name},</p>"
    #             "<p>Thank you for your inquiry. Please find your personalized proposal below:</p>"
    #             f"<p>{proposal_text}</p>"
    #             "<p>Best regards,<br>Zyberfy Team</p>"
    #         )
    #     )
    #     sg = SendGridAPIClient(SENDGRID_API_KEY)
    #     sg.send(message)
    #
