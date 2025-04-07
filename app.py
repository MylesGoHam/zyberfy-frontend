from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    # Extract form data
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    budget = request.form.get('budget')
    location = request.form.get('location')
    special_requests = request.form.get('requests', '')

    # Print for debugging
    print("Name:", name)
    print("Email:", email)
    print("Service:", service)
    print("Budget:", budget)
    print("Location:", location)
    print("Special Requests:", special_requests)

    # Return JSON response for testing
    return jsonify({
        "status": "success",
        "message": "Proposal request received.",
        "data": {
            "name": name,
            "email": email,
            "service": service,
            "budget": budget,
            "location": location,
            "special_requests": special_requests
        }
    })

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
