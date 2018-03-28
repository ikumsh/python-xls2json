from __future__ import print_function
import xlrd, json

#sys stdout

#xls file name and json file name as command line options

def generate_json_from(filename):
	xlsform = xlrd.open_workbook(filename)

	json_form = {}

	survey = xlsform.sheet_by_name("survey");
	json_form["survey"] = generate_json_survey(survey, filename)

	if "choices" in xlsform.sheet_names():
		choices = xlsform.sheet_by_name("choices");
		json_form["choices"] = generate_json_choices(choices, filename)

	if "settings" in xlsform.sheet_names():
		settings = xlsform.sheet_by_name("settings");
		json_form["settings"] = generate_json_settings(settings, filename)

	json_form = json.dumps(json_form, sort_keys=True,
							indent=4, separators=(',', ': '))

	#GENERATE JSON FILENAME
	split_filename = filename.split('.')
	del split_filename[-1]
	split_filename.append('json')
	json_filename = ".".join(split_filename)

	#WRITE JSON FILE
	with open(json_filename, 'w') as json_file:
		json_file.write(json_form)

def unicode_to_utf8(unicode_row):
	utf8_row = []
	for element in unicode_row:
		if ( type(element) == unicode ):
			utf8_row.append(element.encode("utf-8"))
		else:
			utf8_row.append(element)
	return utf8_row

#################

def generate_json_survey(survey, filename):
	survey_attributes = unicode_to_utf8(survey.row_values(0))
	json_survey = []
	make_json_rows(json_survey, survey, survey_attributes, 1)

	return json_survey

def make_json_rows(result, survey, survey_attributes, current_index):
	while current_index < survey.nrows:
		xls_row = unicode_to_utf8(survey.row_values(current_index))
		json_row = make_survey_row(survey_attributes, xls_row)

		row_type = json_row["type"].split(" ")[0]

		if row_type == "select_one" or row_type == "select_multiple":
			json_row["list_name"] = json_row["type"].split(" ")[1]
			json_row["type"] = row_type
		
		if (row_type == 'begin'):
			group_type = json_row['type'].split(' ')[1]

			repeat_group = {}

			fields = []	
			current_index = make_json_rows(fields, survey, survey_attributes, current_index+1)
			
			repeat_group['type'] = group_type
			repeat_group['fields'] = fields

			result.append(repeat_group)
		elif (row_type == 'end'):
			return current_index + 1
		else:
			result.append(json_row)
			current_index += 1
	return current_index

def make_survey_row(attributes, xls_row):
	row = {}
	for attr_index in range(len(attributes)):
		attr = attributes[attr_index]
		if not (xls_row[attr_index] == ''):
			row[attr] = xls_row[attr_index]
	return row

#################

def get_question_types(choices):
	question_types = []
	for row_number in range(choices.nrows):
		row = unicode_to_utf8(choices.row_values(row_number))
		for col_number in range(choices.ncols):
			if row[col_number] == "list_name":
				question_types = unicode_to_utf8(list(set(choices.col_values(col_number))))
				del question_types[question_types.index("list_name")]
	return question_types

def make_choices_row(attributes, xls_row, question_type):
	row = {}
	for attr_index in range(1,len(attributes)):
		attribute = attributes[attr_index]
		if xls_row[attr_index] != '':
			row[attribute] = xls_row[attr_index]
	return row

def generate_json_choices(choices, filename):
	choices_attributes = unicode_to_utf8(choices.row_values(0))

	question_types = get_question_types(choices)

	json_choices = {}
	for q_type in question_types:
		json_choices[q_type] = []
		for row_number in range(1,choices.nrows):
			xls_row = unicode_to_utf8(choices.row_values(row_number))
			if xls_row[0] == q_type:
				json_row = make_choices_row(choices_attributes, xls_row, q_type)
				json_choices[q_type].append(json_row)

	return json_choices

#################

def generate_json_settings(settings, filename):
	settings_attributes = unicode_to_utf8(settings.row_values(0))

	json_settings = {}
	for attr_index in range(len(settings_attributes)):
		attr = settings_attributes[attr_index]
		values = unicode_to_utf8(settings.row_values(1))
		json_settings[attr] = values[attr_index]


	return json_settings


generate_json_from("my_xlsform.xls")



# xlsform = xlrd.open_workbook("my_xlsform.xls")

# survey = xlsform.sheet_by_name("survey");

# print(survey.row_values(0))



# json_survey = generate_json_survey("my_xlsform.xls")
# json_choices = generate_json_choices("my_xlsform.xls")

# print("OUR JSON OBJECT: \n")
# print(json_survey)
# print("\nOUR JSON OBJECT'S TYPE: \n")
# print(type(json_survey))
