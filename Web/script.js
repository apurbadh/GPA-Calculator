
function marksInGPA(marks){
	let numInStr = new String(marks);
	let allGPA = [0,0.8,1.2,1.6,2,2.4,2.8,3.2,3.6,4];
	if (numInStr.length == 1){
		return 0.8;
	}
	let firstChar = Number(numInStr[0]);
	console.log( allGPA[firstChar])
	return allGPA[firstChar];

}





function submit(){
	var eng = (document.getElementById("eng").value/75)*100;
	var nep = (document.getElementById("nep").value/75)*100;
	var eng = (document.getElementById("eng").value/75)*100;
	var sci = (document.getElementById("sci").value/75)*100;
	var soc = (document.getElementById("soc").value/75)*100;
	var mat = document.getElementById("mat").value;
	var opt = document.getElementById("opt").value;
	var com = document.getElementById("com").value*2; 
	let allVar = [Number(eng), Number(nep), Number(eng), Number(sci),Number(soc), Number(mat), Number(opt), Number(com)];
	let varInG = [];
	var totalGPA = 0;
	for (let i=0; i < allVar.length; i++ ){
		var subGPA = marksInGPA(allVar[i]);
		totalGPA = totalGPA + subGPA;

	}
	const gpa = (totalGPA/8).toFixed(2);
	var thatDv = document.getElementById('added');
	thatDv.innerHTML = "Your GPA is " + String(gpa);



}