import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify, send_file)
import json
import azure_oai_connector

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html') # Render index page

@app.route('/uploads', methods=['POST'])
def process_xml():
    try:
        xml_file = request.files['file']
        xml_content = xml_file.read()  # Read the XML content

        # Call Azure OAI and process the response
        # (Replace this with your actual logic)
        # For demonstration purposes, we'll return a dummy response
        azure_oai_response = azure_oai_connector.process_xml_data(xml_content)
        
        print("response")
        print(azure_oai_response)

        # Save the response as a JSON file (optional)
        with open('azure_oai_response.json', 'w') as json_file:
            json.dump(azure_oai_response, json_file, indent=4)

        # Inside your process_xml route
        return jsonify({'message': 'Processing successful. Download the JSON file:', 'file_link': '/download/response.json'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/response.json')
def download_response():
    return send_file('azure_oai_response.json', as_attachment=True)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
