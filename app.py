import random
import jwt
import datetime
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "dev-secret-key"

with open("keys/private.pem", "rb") as f:
    PRIVATE_KEY = f.read()

with open("keys/public.pem", "rb") as f:
    PUBLIC_KEY = f.read()

def verify_jwt(token):
    try:
        payload = jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=["RS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")

        # Basic validation
        if not email or "@" not in email or "." not in email:
            return "Invalid email address", 400

        session["email"] = email

        otp = str(random.randint(100000, 999999))
        session["otp"] = otp

        print(f"[DEBUG] OTP for {email}: {otp}")

        return redirect(url_for("otp"))

    return render_template("login.html")

@app.route("/otp", methods=["GET", "POST"])
def otp():
    if "email" not in session or "otp" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        user_otp = request.form.get("otp")

        if user_otp == session.get("otp"):
            session.pop("otp", None)

            payload = {
                "sub": session.get("email"),
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
            }

            token = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")
            session["token"] = token

            return redirect(url_for("dashboard"))

        return "Invalid OTP", 400

    return render_template("otp.html")

@app.route("/dashboard")
def dashboard():
    token = session.get("token")
    email = session.get("email")

    if not token or not email:
        return redirect(url_for("login"))

    return render_template("dashboard.html", token=token, email=email)

@app.route("/api/protected")
def protected_api():
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return {"error": "Missing or invalid Authorization header"}, 401

    token = auth_header.split(" ")[1]

    payload = verify_jwt(token)

    if not payload:
        return {"error": "Invalid or expired token"}, 401

    return {
        "message": "Access granted to protected resource",
        "user": payload.get("sub")
    }


if __name__ == "__main__":
    app.run(debug=True)
