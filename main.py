from flask import Flask, request
import base64
import json

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    envelope = request.get_json()
    if not envelope or 'message' not in envelope:
        return 'Bad Request: no Pub/Sub message received', 400

    pubsub_message = envelope['message']

    # Decode the Pub/Sub message data (base64)
    if 'data' in pubsub_message:
        message_data = base64.b64decode(pubsub_message['data']).decode('utf-8')
        try:
            event_data = json.loads(message_data)
        except Exception:
            event_data = {"raw": message_data}
    else:
        event_data = {}

    print("Received Pub/Sub event:", event_data)
    # TODO: Add your automation logic here (e.g., fetch new Gmail messages, process attachments)
    return '', 200


if __name__ == "__main__":
    app.run(port=5000)
