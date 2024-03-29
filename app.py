from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Function to initialize Google Sheets client
def init_gspread_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("carman-401622-51cd525af142.json", scope)
    client = gspread.authorize(creds)
    return client.open("carmandata").sheet1

@app.route('/', endpoint='index')
def home():
    return render_template('index.html')

@app.route('/design', methods=['GET', 'POST'])
def design():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        try:
            # Attempt to save to Google Sheets
            sheet = init_gspread_client()
            sheet.append_row([name, email, message])
            
            # Attempt to redirect
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error: {e}")
            return f"There was an error: {e}"
        
    return render_template('design.html')

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    if request.method == 'POST':
        name = request.form['name']
        odometer = request.form['odometer']
        rego = request.form['rego']
        issues = request.form['issues']
        dateTime = request.form['dateTime']
        
        try:
            # Attempt to save to Google Sheets
            sheet = init_gspread_client()
            sheet.append_row([name, odometer, rego, issues, dateTime])
            
            # Attempt to redirect
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error: {e}")
            return f"There was an error: {e}"
        
    return render_template('signout.html')

if __name__ == '__main__':
    app.run(debug=True)
