from flask import Flask, request

app = Flask(__name__)

@app.route('/jenkins-output', methods=['POST'])
def receive_output():
    data = request.json
    return f"""
    <html>
    <body>
        <h1>Jenkins Output Received</h1>
        <pre>{data}</pre>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)
