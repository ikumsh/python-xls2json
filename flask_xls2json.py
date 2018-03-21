from flask import Flask, render_template

app = Flask(__name__)

def open_json(json_filename):
	with open(json_filename, 'r') as json_file:
		json_form = json_file.read()
		# print(json_form)
		return json_form

open_json("my_xlsform.json")

#renders forms
@app.route('/my_xlsform')
def render_form():
	json_form = open_json("my_xlsform.json")
	print(json_form[0])
	return render_template('xls2json.html', json_survey=json_form)

@app.route('/')
def foods():
	food = ['pizza','beer']
	return render_template('thebestdiet.html', food=food)

app.run(debug=True)