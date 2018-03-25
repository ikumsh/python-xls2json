from flask import Flask, render_template

app = Flask(__name__)

def open_json(json_filename):
	with open(json_filename, 'r') as json_file:
		json_object = json_file.read()
		return json_object

#renders forms
@app.route('/my_xlsform')
def render_form():
	json_survey = open_json("my_xlsform_survey.json")
	json_choices = open_json("my_xlsform_choices.json")
	print(json_survey[0])
	return render_template('xls2json.html', json_survey=json_survey, json_choices=json_choices)

app.run(debug=True)