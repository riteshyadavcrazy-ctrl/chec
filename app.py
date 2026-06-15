import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    # Default to Hugging Face Spaces port 7860 if PORT is not set
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
