from flask_frozen import Freezer
from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys

app = Flask(__name__)
freezer = Freezer(app)

# Configure Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/kaedingraham/Downloads/carman-401622-51cd525af142.json", scope)
client = gspread.authorize(creds)
sheet = client.open("carmandata").sheet1

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/design', methods=['GET', 'POST'])
def design():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save data to Google Sheet
        sheet.append_row([name, email, message])
        return redirect(url_for('home'))
    return render_template('design.html')

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    if request.method == 'POST':
        name = request.form['name']
        odometer = request.form['odometer']
        rego = request.form['rego']
        issues = request.form['issues']
        dateTime = request.form['dateTime']
        
        # Save data to Google Sheet
        sheet.append_row([name, odometer, rego, issues, dateTime])
        return redirect(url_for('home'))
    return render_template('signout.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)

