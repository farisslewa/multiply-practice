const num1El = document.getElementById("number1");
const num2El = document.getElementById("number2");
const resultEl = document.getElementById("result");
const JresultOutputEl = document.getElementById("JresultOutput");

getResult = async () => {
	const baseURL = "http://127.0.0.1:8000/multiply";
	const value1 = num1El.value;
	const value2 = num2El.value;
	if (!value1 | isNaN(value1)) {
		alert("please enter a valid number in number1 field");
		return 0;
	}
	if (!value2 | isNaN(value2)) {
		alert("please enter a valid number in number2 field");
		return 0;
	}
	endURL = baseURL + "?param1=" + value1 + "&param2=" + value2;
	try {
		const fetchResponse = await fetch(endURL);
		const data = await fetchResponse.json();
		resultEl.value = data["result"];
		JresultOutputEl.innerHTML = JSON.stringify(data);
	} catch (e) {
		return e;
	}
};
