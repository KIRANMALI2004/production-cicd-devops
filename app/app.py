from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/health-ui")
def health_ui():
    return render_template("health.html")


@app.route("/api/info")
def info():
    return jsonify({
        "application": "Production CI/CD Pipeline",
        "version": "1.0.0",
        "environment": "production"
    })


@app.route("/api-info-ui")
def api_info_ui():
    return render_template("api_info.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)