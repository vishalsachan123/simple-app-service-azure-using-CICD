from flask import Flask

app = Flask(__name__)



@app.route("/")
def home():
    return "you are at home."

@app.route("/health")
def health():
    return "health is ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
