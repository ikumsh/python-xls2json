function generateForm() {
	var jsonXLSForm = JSON.parse(document.getElementById("json_xlsform").innerHTML);

	var jsonSurvey = jsonXLSForm["survey"]
	var jsonChoices = jsonXLSForm["choices"]
	var jsonSettings = jsonXLSForm["settings"]


	// THIS IS WHERE THE FORM HTML IS STORED
	text_html = '';

	// THE FOLLOWING LOOP GENERATES THE FORMS
	for (var i=0; i < jsonSurvey.length; i++) {
		var current_question = jsonSurvey[i];
		var element_id = i+1;
		question_type = current_question["type"].split(" ")[0].trim()
			if ( question_type === "text") {
				text_html += createTextField(element_id, current_question, element_id)
			} else if (question_type === "integer") {
				text_html += createIntegerField(element_id, current_question)
			} else if (question_type === "decimal") {
				text_html += createDecimalField(element_id, current_question)
			} else if (question_type === "date") {
				text_html += createDateField(element_id, current_question)
			} else if (question_type === "time") {
				text_html += createTimeField(element_id, current_question)
			} else if (question_type === "datetime") {
				text_html += createDateTimeField(element_id, current_question)
			} else if (question_type === "image") {
				text_html += createImageField(element_id, current_question)
			}else if (question_type === "note") {
				text_html += createNoteField(element_id, current_question)
			} else if ( question_type === "select_one") {
				text_html += createSelectOneField(element_id, current_question, jsonChoices)
			} else if ( question_type === "select_multiple") {
				text_html += createSelectMultipleField(element_id, current_question, jsonChoices)
			} 
		
	};

	var formPlaceHolder = document.getElementById("xlsform_survey");
	formPlaceHolder.innerHTML += text_html;
};

function createTextField(element_id, survey_question) {
	text_name = survey_question["name"]
	text_label = survey_question["label"]
	text_hint = survey_question["hint"]

	hint_tooltip = "data-toggle=\"tooltip\" title=\""+text_hint+"\" "

	text_required = ''
	if (survey_question["required"]) {
		text_required = 'required'
	}
	text_relevant = survey_question["relevant"]

	$()

	text_html = "<br/><label>"+text_label+"<input id=\""+element_id+
				"\" type=\"text\" "+" name=\""+text_name+"\" "+
				hint_tooltip+text_required+"/></label><br/>"
	return text_html;
};

function createIntegerField(element_id, survey_question) {
	int_name = survey_question["name"]
	int_label = survey_question["label"]



	text_html = "<br/><label>"+int_label+" <input id=\""+element_id+"\" type=\"number\" "+
				" name=\""+int_name+"\" /></label><br/>"
	return text_html;
};

function createDecimalField(element_id, survey_question) {
	decimal_name = survey_question["name"]
	decimal_label = survey_question["label"]
	decimal_hint = survey_question["hint"]
	decimal_constraint = survey_question["constraint"]
	decimal_contstraint_message = survey_question["contstraint_message"]

	hint_tooltip = "data-toggle=\"tooltip\" title=\""+decimal_hint+"\" "

	text_html = "<br/><label>"+decimal_label+" <input id=\""+element_id+"\" type=\"number\" "+
				"step=\"0.01\""+" name=\""+decimal_name+"\" "+hint_tooltip+
				"constraint=\""+decimal_constraint+"\" contstraint_message=\""+
				decimal_contstraint_message+"\" /></label><br/>"
	return text_html;
};

function createCalculateField(element_id, survey_question) {
	calculate_name = survey_question["name"]
	calculate_calculation = survey_question["calculation"]
	result = 0

	// $('[name="ElementNameHere"]').doStuff();


	text_html = "<br/><label>Result: "+result+"<div>"+"</div></label><br/>"
	return text_html;
};

function createDateField(element_id, survey_question) {
	date_name = survey_question["name"]
	date_label = survey_question["label"]

	text_html = "<br/><label>"+date_label+" <input id=\""+element_id+"\" type=\"date\" "+
				" name=\""+date_name+"\" /></label><br/>"
	return text_html;
};

function createTimeField(element_id, survey_question) {
	time_name = survey_question["name"]
	time_label = survey_question["label"]

	text_html = "<br/><label>"+time_label+" <input id=\""+element_id+"\" type=\"time\" "+
				" name=\""+time_name+"\" /></label><br/>"
	return text_html;
};

function createDateTimeField(element_id, survey_question) {
	date_time_name = survey_question["name"]
	date_time_label = survey_question["label"]

	text_html = "<br/><label>"+date_time_label+" <input id=\""+element_id+"\" type=\"datetime-local\" "+
				" name=\""+date_time_name+"\" step=\"60\"/></label><br/>"
	return text_html;
};

// NEEDS WORK & CAMERA FUNCTION ON PHONE
function createImageField(element_id, survey_question) {
	image_name = survey_question["name"]
	image_label = survey_question["label"]

			// <input type="file" accept="image/*" capture="camera">

			// var myInput = document.getElementById('myFileInput');

			// function sendPic() {
			//     var file = myInput.files[0];

			//     // Send file here either by adding it to a `FormData` object 
			//     // and sending that via XHR, or by simply passing the file into 
			//     // the `send` method of an XHR instance.
			// }

			// myInput.addEventListener('change', sendPic, false);

	// text_html = "<br/>"+image_label+" <input type=\"file\" "+
	// 			" name=\""+image_name+"\" />"+"<br/>"

	// text_html = "<br/><input id=\"myFileInput\" type=\"file\" accept=\"image/*;capture=camera\"><br/>"

	text_html = "<br/><label>"+image_label+"<input id=\""+element_id+"\" type=\"file\" accept=\"image/*\" "+
				"capture=\"camera\"></label><br/>"

	return text_html;
};

function createNoteField(element_id, survey_question) {
	note_name = survey_question["name"]
	note_label = survey_question["label"]
	note_hint = survey_question["hint"]
	note_hint_chinese = survey_question["hint::chinese"]
	note_label_chinese = survey_question["label::chinese"]
	note_image = survey_question["image"]
	note_audio = survey_question["audio"]
	note_image_english = survey_question["image::english"]
	note_media_audio_chinese = survey_question["media::audio::chinese"]
	note_media_video = survey_question["media::video"]

	hint_tooltip = "data-toggle=\"tooltip\" title=\""+note_hint+"\" "



	text_html = "<br/><label>"+note_label+"<div id=\""+
				element_id+"\" name=\""+note_name+"\" "
				+hint_tooltip+" ></div></label><br/>"
	return text_html;
};

function createSelectOneField(element_id, survey_question, choices) {
	list_name = survey_question["type"].split(" ")[1].trim()

	select_one_name = survey_question["name"]
	select_one_label = survey_question["label"]
	select_one_hint = survey_question["hint"]
	select_one_appearance = survey_question["appearance"]

	if (select_one_hint === undefined) {
		hint_tooltip = ""
	} else {
		hint_tooltip = "data-toggle=\"tooltip\" title=\""+select_one_hint+"\" "
	};

	choices_html = ""
	all_choices = choices[list_name]

	for (var i = 0; i < all_choices.length; i++) {
		name = choices[list_name][i]["name"]
		label = choices[list_name][i]["label"]
		image = choices[list_name][i]["image"]
		label_chinese = choices[list_name][i]["label::chinese"]

		name_radio = "name=\""+select_one_name+"\" ";
		value_radio = "value=\""+name+"\" ";
		label_radio = label;
		image_radio = "image=\""+image+"\" ";
		label_chinese_radio = "label_chinese=\""+label_chinese+"\" ";

		if (name === undefined) {
			value_radio = "";
		}
		if (label === undefined) {
			label_radio = "";
		}
		if (image === undefined) {
			image_radio = "";
		}
		if (label_chinese === undefined) {
			label_chinese_radio = "";
		}

		choice_id = element_id+((i+1)*0.1)

		choices_html += "<br/><label><input id=\""+choice_id+
						"\" type=\"radio\" "+name_radio+value_radio+
						"/>"+label_radio+"</label>"
	};

	full_html = "<br/><label>"+select_one_label+"<div id=\""
				+element_id+"\" name=\""+select_one_name+
				"\" "+hint_tooltip+" "+"appearance=\""
				+select_one_appearance+"\" >"+choices_html+
				"</div></label><br/>"

	return full_html;
};

function createSelectMultipleField(element_id, survey_question, choices) {
	list_name = survey_question["type"].split(" ")[1].trim()

	select_multiple_name = survey_question["name"]
	select_multiple_label = survey_question["label"]
	select_multiple_hint = survey_question["hint"]
	select_multiple_appearance = survey_question["appearance"]

	if (select_multiple_hint === undefined) {
		hint_tooltip = ""
	} else {
		hint_tooltip = "data-toggle=\"tooltip\" title=\""+select_multiple_hint+"\" "
	};

	choices_html = ""
	all_choices = choices[list_name]

	for (var i = 0; i < all_choices.length; i++) {
		name = choices[list_name][i]["name"]
		label = choices[list_name][i]["label"]
		image = choices[list_name][i]["image"]
		label_chinese = choices[list_name][i]["label::chinese"]

		name_html = "name=\""+name+"\" ";
		label_html = label;
		image_html = "image=\""+image+"\" ";
		label_chinese_html = "label_chinese=\""+label_chinese+"\" ";

		if (name === undefined) {
			name_html = "";
		}
		if (label === undefined) {
			label_html = "";
		}
		if (image === undefined) {
			image_html = "";
		}
		if (label_chinese === undefined) {
			label_chinese_html = "";
		}

		choices_html += "<br/><label><input id=\""+choice_id+"\" type=\"checkbox\" "+name_html+
						image_html+label_chinese_html+" />"+label_html+"</label>"
	};

	full_html = "<br/><label>"+select_multiple_label+
				"<div id=\""+element_id+"\" name=\""+
				select_multiple_name+"\" "+hint_tooltip+
				"appearance=\""+select_multiple_appearance+
				"\" >"+choices_html+"</div></label><br/>"

	return full_html;
};
