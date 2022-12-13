var questions=document.getElementsByTagName("dt");
var answers=document.getElementsByTagName("dd");
var advancedlinks=document.getElementById("advancedlinks");
var answerlinks=document.getElementById("answerlinks");
var prevquestions=new Array();
var question=0;
var date=new Date();
var rand=0;
var queuenum=-1;

var questions_asked=new Array();

function next_question () {
	if ( questions.length != answers.length ) {
		window.alert("Numbers of questions and answers are different.");
	}

	if ( questions.length == 0 ) {
		window.alert("No questions currently available.");
	}

	queuenum++;
	questions[question].className="hidden";
	answers[question].className="hidden";
	if ( queuenum < prevquestions.length ) {
		question=prevquestions[queuenum];
	} else {
		var numasked=0;
		for ( i=0 ; i < questions_asked.length ; i++ ) {
			if ( questions_asked[i] == 1 ) {
				numasked++;
			}
		}
		if ( numasked == questions.length ) {
			window.alert("All questions have been asked.");
		} else {
			do {
			  question=Math.floor(Math.random() * questions.length);
			} while ( questions_asked[question] == 1 );
		}
		prevquestions.push(question);
	}
	questions[question].className="visible";
}

function show_answerlinks () {
	answerlinks.className="visible";
}

function hide_answerlinks () {
	answerlinks.className="hidden";
}

function show_all () {
	for ( i=0 ; i < questions.length ; i++ ) {
		questions[i].className="visible";
		answers[i].className="visible";
	}
}

function show_advanced () {
	advancedlinks.className="visible";
}

function toggle_answer () {
	if ( answers[question].className == "visible" ) {
		answers[question].className="hidden";
	} else {
		answers[question].className="visible";
	}
}

function prev_question () {
	questions[question].className="hidden";
	answers[question].className="hidden";
	if ( queuenum > 0 ) {
		queuenum--;
		question=prevquestions[queuenum];
	} else {
		window.alert("This is the first question.");
	}
	questions[question].className="visible";
}

function back_in_deck () {
	questions_asked[question]=0;
	next_question();
}

function out_of_deck () {
	questions_asked[question]=1;
	next_question();
}
