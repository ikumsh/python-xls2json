from __future__ import print_function
import xlrd, json


def generate_json_from_xlsform(filename):
	xlsform = xlrd.open_workbook(filename)

	survey = xlsform.sheet_by_index(0)
	choices = xlsform.sheet_by_index(1)
	settings = xlsform.sheet_by_index(2)

	form_attributes = []
	attributes = survey.row_values(0)

	for attr in attributes:
		if type(attr) == unicode:
			form_attributes.append(attr.encode("utf-8"))
		else:
			form_attributes.append(attr)

	xlsform_survey = []

	for x in range(1,survey.nrows):
		row = {}
		row_utf8 = []
		row_unicode = survey.row_values(x)

		for value in row_unicode:
			if type(value) == unicode:
				row_utf8.append(value.encode("utf-8"))
			else:
				row_utf8.append(value)

		for form_attr in range(len(form_attributes)):
			attr = form_attributes[form_attr]
			if not (row_utf8[form_attr] == ''):
				row[attr] = row_utf8[form_attr]

		xlsform_survey.append(row)

	xlsform_json = json.dumps(xlsform_survey, sort_keys=True,
								indent=4, separators=(',', ': '))

	#GENERATE JSON FILENAME
	split_filename = filename.split('.')
	del split_filename[-1]
	split_filename.append('json')
	json_filename = ".".join(split_filename)

	#WRITE JSON FILE
	with open(json_filename, 'w') as json_file:
		json_file.write(xlsform_json)


	return xlsform_json #RETURN NOT NECESSARY. ONLY SO WE CAN PRINT


xlsform_json = generate_json_from_xlsform("my_xlsform.xls")

print("OUR JSON OBJECT: \n")
print(xlsform_json)
print("\nOUR JSON OBJECT'S TYPE: \n")
print(type(xlsform_json))
