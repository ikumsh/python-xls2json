from flask import Flask, render_template

app = Flask(__name__)

def open_json(json_filename):
	with open(json_filename, 'r') as json_file:
		json_object = json_file.read()
		return json_object

#renders forms
@app.route('/my_xlsform')
def render_form():
	json_xlsform = open_json("my_xlsform.json")
	return render_template('xls2json.html', json_xlsform=json_xlsform)

app.run(debug=True)