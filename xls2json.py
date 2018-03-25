from __future__ import print_function
import xlrd, json

def unicode_to_utf8(unicode_row):
	utf8_row = []
	for element in unicode_row:
		if ( type(element) == unicode ):
			utf8_row.append(element.encode("utf-8"))
		else:
			utf8_row.append(element)
	return utf8_row

def generate_json_from(filename):
	xlsform = xlrd.open_workbook(filename)

	survey = xlsform.sheet_by_name("survey");
	choices = xlsform.sheet_by_name("choices");
	settings = xlsform.sheet_by_name("settings");

	choices_attributes = unicode_to_utf8(choices.row_values(0))
	settings_attributes = unicode_to_utf8(settings.row_values(0))

	json_survey = generate_json_survey(survey, filename)
	# json_choices = generate_json_choices(choices)
	# json_settings = generate_json_settings(settings)

	# json_form = {}

	# json_form["survey"] = json_survey
	# json_form["choices"] = json_choices
	# json_form["settings"] = json_settings

	# json_form = json.dumps(xlsform_survey, sort_keys=True,
	# 						indent=4, separators=(',', ': '))
	# return json_form



#make one json file instead of 3

# complete settings conversion

#sys stdout



#xls file name and json file name as command line options

#################

def generate_json_survey(survey, filename):
	survey_attributes = unicode_to_utf8(survey.row_values(0))
	json_survey = []
	make_json_rows(json_survey, survey, survey_attributes, 1)

	xlsform_json = json.dumps(json_survey, sort_keys=True,
								indent=4, separators=(',', ': '))

	#GENERATE JSON FILENAME
	split_filename = filename.split('.')
	del split_filename[-1]
	split_filename.append('json')
	json_filename = ".".join(split_filename)

	#WRITE JSON FILE
	with open(json_filename, 'w') as json_file:
		json_file.write(xlsform_json)

def make_json_rows(result, survey, survey_attributes, current_index):
	while current_index < survey.nrows:
		xls_row = unicode_to_utf8(survey.row_values(current_index))
		json_row = make_survey_row(survey_attributes, xls_row)
		
		if ( 'begin ' == json_row['type'][:6]):
			group_type = json_row['type'].split(' ')[1]

			repeat_group = {}

			fields = []	
			current_index = make_json_rows(fields, survey, survey_attributes, current_index+1)
			
			repeat_group['type'] = group_type
			repeat_group['fields'] = fields

			result.append(repeat_group)
		elif ( 'end ' == json_row['type'][:4]):
			return current_index + 1
		else:
			result.append(json_row)
			current_index += 1
	return current_index

def make_survey_row(attributes, xls_row):
	row = {}
	for form_attr in range(len(attributes)):
		attr = attributes[form_attr]
		if not (xls_row[form_attr] == ''):
			row[attr] = xls_row[form_attr]
	return row

#################

def generate_json_choices(filename,):

	question_types = []

	for x in range(1,choices.nrows):
		question_type = choices.row_values(x)[0]
		if type(question_type) == unicode:
			if question_type.encode("utf-8") not in question_types:
				question_types.append(question_type.encode("utf-8"))
		else:
			if question_type not in question_types:
				question_types.append(question_type)

	xlsform_choices = {}

	for qtype in question_types:
		xlsform_choices[qtype] = []

	for x in range(1,choices.nrows):
		list_name = choices.row_values(x)[0]
		row = {}
		row_utf8 = []
		row_unicode = choices.row_values(x)

		for value in row_unicode:
			if type(value) == unicode:
				row_utf8.append(value.encode("utf-8"))
			else:
				row_utf8.append(value)

		for question_attr in range(1,len(choice_attributes)):
			attr = choice_attributes[question_attr]
			if not (row_utf8[question_attr] == ''):
				row[attr] = row_utf8[question_attr]

		xlsform_choices[list_name].append(row)

	json_choices = json.dumps(xlsform_choices, sort_keys=True,
								indent=4, separators=(',', ': '))

	#GENERATE JSON FILENAME
	split_filename = filename.split('.')
	del split_filename[-1]
	split_filename[-1] += "_choices"
	split_filename.append('json')
	json_filename = ".".join(split_filename)

	#WRITE JSON FILE
	with open(json_filename, 'w') as json_file:
		json_file.write(json_choices)


	return json_choices #RETURN NOT NECESSARY. ONLY SO WE CAN PRINT

# def generate_json_settings(filename):
# 	xlsform = xlrd.open_workbook(filename)

# 	survey = xlsform.sheet_by_index(0)
# 	choices = xlsform.sheet_by_index(1)
# 	settings = xlsform.sheet_by_index(2)

# 	form_attributes = []
# 	attributes = survey.row_values(0)

# 	for attr in attributes:
# 		if type(attr) == unicode:
# 			form_attributes.append(attr.encode("utf-8"))
# 		else:
# 			form_attributes.append(attr)

# 	xlsform_survey = []

# 	for x in range(1,survey.nrows):
# 		row = {}
# 		row_utf8 = []
# 		row_unicode = survey.row_values(x)

# 		for value in row_unicode:
# 			if type(value) == unicode:
# 				row_utf8.append(value.encode("utf-8"))
# 			else:
# 				row_utf8.append(value)

# 		for form_attr in range(len(form_attributes)):
# 			attr = form_attributes[form_attr]
# 			if not (row_utf8[form_attr] == ''):
# 				row[attr] = row_utf8[form_attr]

# 		xlsform_survey.append(row)

# 	xlsform_json = json.dumps(xlsform_survey, sort_keys=True,
# 								indent=4, separators=(',', ': '))

# 	#GENERATE JSON FILENAME
# 	split_filename = filename.split('.')
# 	del split_filename[-1]
# 	split_filename.append('json')
# 	json_filename = ".".join(split_filename)

# 	#WRITE JSON FILE
# 	with open(json_filename, 'w') as json_file:
# 		json_file.write(xlsform_json)


# 	return xlsform_json #RETURN NOT NECESSARY. ONLY SO WE CAN PRINT

# generate_json_survey("my_xlsform.xls")
# generate_json_choices("my_xlsform.xls")





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
