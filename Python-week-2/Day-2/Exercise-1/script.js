
 let x = 5;
 let y = 2;


if (x>y) {
	console.log(alert('x is the biggest number'));
}
else if (x<y) {
	console.log(alert('false'))
}


var newDog = "Chihuahua";
var n = newDog.length; 
console.log(n)
console.log(newDog.toLowerCase())
console.log(newDog.toUpperCase())

if (newDog == "Chihuahua") {
	console.log(alert('I love Chihuahuas, it’s my favorite dog breed'));
}
else {
 console.log(alert('I dont care I prefer cats'))
}

// --------exercise3---------------------------

let number = prompt("Insert a number.");

if (number%2==0) {
	alert(`${number} is an even number`)
}
else if (number%2!=0) {
	alert(`${number} is an odd number`)
}

let numbuser = prompt("Insert number of users.");
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
var name_user1= users[0];
var name_user2= users[1];
var name_user3= numbuser-2;

if (numbuser==0) {
	alert("no one is online.")
} else if (numbuser==1) {
	alert(`${name_user1} is online.`)
} else if (numbuser==2) {
	alert(`${name_user1} and ${name_user2} are online.`)
} else if (numbuser>2) {
	alert(`${name_user1} and ${name_user2} and ${name_user3} are online.`)
} 
