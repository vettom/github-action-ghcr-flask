from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "My image in GHCR"

@app.route("/health")
def home():
    return "Success", 200

if __name__ == '__main__':
    app.run()
    