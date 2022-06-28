
let sentence ="The movie is not that bad, I like it";
let sentence1= prompt("Do a sentence with the word not and bad","The movie is not that bad, I like it")
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
let sentence2= sentence1.substring(0 ,wordNot-1);
let sentence3 =sentence1.substring(wordBad +3,sentence1.length)
let var1= "good";
console.log(wordNot);
console.log(wordBad);
if (wordBad>wordNot) {
	console.log(`${sentence2} ${var1} ${sentence3}`)
}
else if (wordBad<wordNot) {
	console.log(`${sentence1}`)
}

