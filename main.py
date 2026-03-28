from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INFINITY_API = "https://zynera.fr/api_login.php"  # ton API InfinityFree

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"error": "Email et mot de passe requis"}), 400

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.post(INFINITY_API, data={"email": email, "password": password}, headers=headers, timeout=10)
        return r.text, r.status_code, {"Content-Type": "application/json"}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
