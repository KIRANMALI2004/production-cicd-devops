from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Production CI/CD DevOps Application",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": "Production CI/CD Pipeline",
        "version": "1.0.0",
        "environment": "production"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)