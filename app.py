from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Kavya Rao Sares</h1>
    <h2>Traditional Sarees Collection</h2>
    <p>Powered by Flask + Docker + Kubernetes + ArgoCD</p>
    """

@app.route("/about")
def about():
    return "Kavya Rao Sares Online Store"

@app.route("/contact")
def contact():
    return "Contact: kavya@example.com"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
