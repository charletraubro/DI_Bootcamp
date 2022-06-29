let n = 6;
let string = "";
for (let i = 1; i <= n; i++) {

	for (let x = 0; x < i; x++) {

		string += "*";
	}
	
	string += "\n";
}
console.log(string);