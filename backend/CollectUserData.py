from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use an app password here

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()

    name = data.get('name')
    address = data.get('address')
    whatsapp = data.get('whatsapp')
    email = data.get('email')

    msg = EmailMessage()
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Name: {name}\nAddress: {address}\nWhatsApp: {whatsapp}\nEmail: {email}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send email."}), 500

if __name__ == '__main__':
    app.run(debug=True)
