from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= CAESAR =================
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")


@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])

    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)

    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"


@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])

    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)

    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ================= VIGENERE =================
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")


# ================= PLAYFAIR =================
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")


# ================= RAILFENCE =================
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")


# ================= TRANSPOSITION =================
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")


# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)