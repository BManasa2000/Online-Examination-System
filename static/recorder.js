var buttonStop= document.getElementById("Submit");

buttonStop.onCLick= function(){
	// XMLHttpRequest
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false" }));
};
