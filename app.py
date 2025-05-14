from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import os
from openpyxl import Workbook, load_workbook
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__, static_folder='statics', template_folder='templates')
CORS(app)

EMAIL_ADDRESS = "swarajbehera.8673@gmail.com"
EMAIL_PASSWORD = "vkwdrwkrsjfjadpc"

SHEET_NAME = 'Client Data'  # Name of your Google Sheet
CREDENTIALS_FILE = 'quixotic-tesla-459406-u5-b0653b0e1c15.json'  # Path to your service account credentials

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rooftopsolarpanel')
def rooftopsolarpanel():
    return render_template('RooftopSolarPanel.html')

@app.route('/ongridsolarsystem')
def ongridsolarsystem():
    return render_template('OnGridSolarSystem.html')

@app.route('/offgridsolarsystem')
def offgridsolarsystem():
    return render_template('OffGridSolarSystem.html')

@app.route('/largescalesolarpanels')
def largescalesolarpanels():
    return render_template('LargeScaleSolarPanels.html')

@app.route('/mountingsystems')
def mountingsystems():
    return render_template('MountingSystems.html')

@app.route('/auxillarytransformers')
def auxillarytransformers():
    return render_template('AuxillaryTransformers.html')

@app.route('/monitoringandcontrolsystems')
def monitoringandcontrolsystems():
    return render_template('MonitoringAndControlSystems.html')

@app.route('/homebatterystoragesystems')
def homebatterstoragesystems():
    return render_template('HomeBatteryStorageSystem.html')

@app.route('/highcapacitybatterystorage')
def highcapacitybatterystoragesystem():
    return render_template('HighCapacityBatteryStorageSystem.html')

@app.route('/integratedinverterandbatterysystems')
def integratedinverterandbatterysystem():
    return render_template('IntegratedInverterAndBatterySystem.html')

@app.route('/energymanagementsystems')
def energymanagementsystem():
    return render_template('EnergyManagementSystem.html')

@app.route('/product-enquiry', methods=['POST'])
def product_enquiry():
    productData = request.get_json()

    name = productData.get('name')
    phone = productData.get('phone')
    productChoice = productData.get('productChoice')
    email = productData.get('email')
    address = productData.get('address')

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).worksheet("Product_Enquiry")  # Replace with your sheet name

    # Append data to the sheet
    sheet.append_row([name, phone, productChoice, email, address])

    # Get the sheet URL
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet.spreadsheet.id}/edit"
    # === GOOGLE SHEETS LOGIC END ===

    msg = EmailMessage()
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Name: {name}\nPhone: {phone}\nProduct: {productChoice}\nEmail: {email}\nAddress: {address}\nGoogle Sheet Link: {sheet_url}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"message": "Thank you for the enquiry. We will reach out to you soon!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "We are facing some issues at the moment. Please try again. Sorry for the inconvenience."}), 500

@app.route('/freesitesurvey')
def freesitesurvey():
    return render_template('FreeSiteSurveyAndConsultation.html')

@app.route('/feasibilitystudy')
def feasibilitystudy():
    return render_template('FeasibilityStudy&ROIAnalysis.html')

@app.route('/installationandcommissioning')
def installationandcommissioning():
    return render_template('Installation&Commissioning.html')

@app.route('/customerengineeringandprocurement')
def customerengineeringandprocurement():
    return render_template('CustomEngineering&Procurement.html')

@app.route('/maintenanceandcleaning')
def maintenanceandcleaning():
    return render_template('Maintenance&CleaningPackage.html')

@app.route('/endtoendepcservices')
def endtoendepcservices():
    return render_template('EPCServices.html')

@app.route('/operationandmaintenancecontracts')
def operationandmaintenancecontracts():
    return render_template('O&MContracts.html')

@app.route('/storagesystemsizinganddesign')
def storagesystemsizinganddesign():
    return render_template('StorageSystemSizing&Design.html')

@app.route('/gridindependenceconsulting')
def gridindependenceconsulting():
    return render_template('GridIndependenceConsulting.html')

@app.route('/warrantyandreplacementsupport')
def warrantyandreplacementsupport():
    return render_template('Warranty&ReplacementSupport.html')

@app.route('/storageretrofitting')
def storageretrofitting():
    return render_template('StorageRetrofitting.html')

@app.route('/service-enquiry', methods=['POST'])
def service_enquiry():
    data = request.get_json()

    name = data.get('name')
    phone = data.get('phone')
    serviceChoice = data.get('serviceChoice')
    email = data.get('email')
    address = data.get('address')

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).worksheet("Service_Enquiry")  # Replace with your sheet name

    # Append data to the sheet
    sheet.append_row([name, phone, serviceChoice, email, address])

    # Get the sheet URL
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet.spreadsheet.id}/edit"
    # === GOOGLE SHEETS LOGIC END ===

    msg = EmailMessage()
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Name: {name}\nPhone: {phone}\nService: {serviceChoice}\nEmail: {email}\nAddress: {address}\nGoogle Sheet Link: {sheet_url}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"message": "Thank you for the enquiry. We will reach out to you soon!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "We are facing some issues at the moment. Please try again. Sorry for the inconvenience."}), 500

@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact-form', methods=['POST'])
def contact_form():
    data = request.get_json()

    name = data.get('name')
    address = data.get('address')
    whatsapp = data.get('whatsapp')
    email = data.get('email')

    # === GOOGLE SHEETS LOGIC START ===
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).worksheet("Contact_Form")  # Replace with your sheet name

    # Append data to the sheet
    sheet.append_row([name, address, whatsapp, email])

    # Get the sheet URL
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet.spreadsheet.id}/edit"
    # === GOOGLE SHEETS LOGIC END ===

    msg = EmailMessage()
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Name: {name}\nAddress: {address}\nWhatsApp: {whatsapp}\nEmail: {email}\nGoogle Sheet Link: {sheet_url}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"message": "Email and Excel attachment sent successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send email."}), 500
    


if __name__ == '__main__':
    app.run(debug=True)
