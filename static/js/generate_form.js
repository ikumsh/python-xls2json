function generateForm() {
	var jsonStringForm = document.getElementById("json_survey").innerHTML;
	// console.log(jsonStringForm);
	var jsonForm = JSON.parse(jsonStringForm);

	// console.log(jsonForm.length);

	text_html = '';

	for (var i=0; i < jsonForm.length; i++) {
		var current_survey_question = jsonForm[i];

		if (current_survey_question["type"] === "text") {
			text_html += createTextField(current_survey_question)
		};


	};

	var formPlaceHolder = document.getElementById("xlsform_survey");
	formPlaceHolder.innerHTML += text_html;

	// console.log(jsonStringForm)
	// console.log(jsonForm)

	// console.log(formhtml)
};

function createTextField(survey_question) {
	text_name = survey_question["name"]
	text_label = survey_question["label"]
	text_hint = survey_question["hint"]
	
	text_required = ''
	if (survey_question["required"]) {
		text_required = 'required'
	}
	text_relevant = survey_question["relevant"]



	text_html = "<br/>"+text_label+" <input type=\"text\" "+
				" name=\""+text_name+"\" hint=\""+text_hint+"\" "+text_required+"/>"+"<br/>"
	return text_html;
}
