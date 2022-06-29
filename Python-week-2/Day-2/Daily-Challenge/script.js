
<<<<<<< HEAD
let sentence ="Adam Taieb is not that bad, but he has a little penis";
let sentence1= prompt("Do a sentence with the word not and bad","The movie is not that bad, I like it")
let wordNot = sentence1.indexOf("not");
let wordBad = sentence1.indexOf("bad");
let sentence2= sentence.substring(0 ,wordNot-1);
let sentence3 =sentence.substring(wordBad +3,sentence.length)
=======
let sentence ="The movie is not that bad, I like it";
//let sentence1= prompt("Do a sentence with the word not and bad","The movie is not that bad, I like it")
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
let sentence2= sentence1.substring(0 ,wordNot-1);
let sentence3 =sentence1.substring(wordBad +3,sentence1.length)
>>>>>>> f51fad1fcaf81fdc5a95bff7db4cb6c5821d2eaa
let var1= "good";
console.log(wordNot);
console.log(wordBad);
if (wordBad>wordNot) {
	console.log(`${sentence2} ${var1} ${sentence3}`)
}
else if (wordBad<wordNot) {
	console.log(`${sentence}`)
}

