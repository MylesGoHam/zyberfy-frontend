import json
import openai
import os

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }

    try:
        body = json.loads(request.body)

        sender = body.get("sender", "")
        recipient = body.get("recipient", "")
        tone = body.get("tone", "Professional")
        email = body.get("email", "")

        prompt = f"""Reply to the following email in a {tone.lower()} tone:

        {email}

        From: {sender}
        To: {recipient}"""

        openai.api_key = os.environ.get("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're an expert email assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content.strip()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"reply": reply})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }