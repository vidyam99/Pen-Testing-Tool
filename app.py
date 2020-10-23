from flask import Flask, request, render_template, redirect, url_for
from malware_scan import *
from network_scan import *
from credential_audit import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
        return render_template('index.html')

@app.route('/malwareScan',methods = ['GET', 'POST'])
def malware_scan():
    if request.method == 'GET':
        return render_template('malware_scan.html')
    elif request.method == 'POST':
        path = request.form['folder']
        result = main(WebPath = path)
        return render_template('malware_scan.html', result = result, id = 'result')

@app.route('/networkScan', methods=['GET', 'POST'])
def network_scan():
    if request.method == 'GET':
        return render_template('network_scan.html')
    elif request.method == 'POST':
        host = request.form['host']
        result = host_discovery(target = host)
        return render_template('network_scan.html', result = result, id = 'result')

@app.route('/credentialAudit', methods=['GET'])
def credential_audit():
    if request.method == 'GET':
        return render_template('credential_audit.html')

@app.route('/credentialAudit/generateWordlist', methods = ['GET', 'POST'])
def generate():
    if request.method == 'GET':
        return render_template('generate_wordlist.html', id = 'generate')
    elif request.method == 'POST':
        if 'generate' in request.form:
            result = wordlist(targetInfo = request.form)
            return render_template('generate_wordlist.html', result = result, id = 'result')

@app.route('/credentialAudit/checkSecurity', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('check_security.html', id = 'check')
    elif request.method == 'POST':
        if 'check' in request.form:
            server = request.form['server']
            email = request.form['email']
            result = dos(emailID = email, mailServer = server)
            return render_template('check_security.html', result = result, id = 'result')

if __name__ == '__main__':
    app.run(debug=True)