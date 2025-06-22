from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # data = request.json
    if request.method == 'GET' and 'validationToken' in request.args:
        return request.args['validationToken'], 200, {'Content-Type': 'text/plain'}
    # Handle real notifications (POST)
    if request.method == 'POST':
        # Your event handling logic here
        return '', 202

if __name__ == "__main__":
    app.run(port=5000)
