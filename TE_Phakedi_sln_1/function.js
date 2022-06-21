let btnValidate = document.querySelector('button');
let Validation = document.querySelector('h1');

let inputDay = document.querySelector('#bday');
let inputMonth = document.querySelector('#bmonth');
let inputYear = document.querySelector('#byear');

//Accepting values entered by user to verify the correct format
btnValidate.addEventListener('click', () =>{
	let bday=inputDay.value;
	let bmonth=inputMonth.value;
	let byear=inputYear.value;

	validation.innerText=moment('${bday}/${bmonth}/${byear}'. 'mm/dd/YYYY',true).isValid();
})