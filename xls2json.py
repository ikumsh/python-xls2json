from __future__ import print_function
import xlrd, json


xlsform = xlrd.open_workbook("my_xlsform.xls")

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


def print_row(keys,values):
	for key in keys:
		if key in values:
			print(key,":",values[key],'| ',end='')
	print()

# PRINTS ALL ROWS
def print_survey(xlsform_survey):
	n = 2
	for row in xlsform_survey:
		print(n,"| ",end='')
		print_row(form_attributes,row)
		n += 1

xlsform_json = json.dumps(xlsform_survey)


# print_survey(xlsform_survey)
# print(xlsform_json)
# print(type(xlsform_json))
