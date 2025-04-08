@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    # Extract form data
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    budget = request.form.get('budget')
    location = request.form.get('location')
    special_requests = request.form.get('requests')

    # Debug: Print received data
    print(f"Received Proposal Request:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Service: {service}")
    print(f"Budget: {budget}")
    print(f"Location: {location}")
    print(f"Special Requests: {special_requests}")

    # Send email logic (SendGrid integration here)

    return 'Proposal submitted successfully!'
