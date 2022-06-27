// let driver = prompt('How old are you?',20) 
// if (driver < 18) {
// 	(alert('Sorry, you are too young to drive this car. Powering off'))
// } else if (driver == 18) {
// 	(alert('Congratulations on your first year of driving. Enjoy the ride'))
// } else if (driver > 18) {
// 	(alert('Powering On. Enjoy the ride!'))
// }

// let a = 8;
// let b = 7;
// let c = 6;

// if (a===b) {
// 	console.log('true');
// }
// else if (c<a) {
// 	console.log('yes');
// }
// else if (b>c) {
// 	console.log('no');

// }
// else {
// 	console.log('false');
// }
//  (a===b) ? console.log('yes'):console.log('no');

// let num =  (a===b)? 6:8

// let page = 'Home';


// switch (page) {
// 	case 'Home':
// 	console.log('home');

// 	break;
// 	case 'about':
// 	console.log('about')

// 	break;

// 	default:

// 	console.log('404 page');
// }

// let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

// let a = 3 + 2;

// switch (a) {
//   case 4:
//     alert('Right!');
//     break;

//   case 3: // (*) grouped two cases
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     alert("you are fucking dumb!!!")
//     break;

//   default:
//     alert('The result is strange. Really.');
// }

// let arr = [2,4,5,6]
// let obj = {
// 	name: 'John',
// 	lastname: 'Miller',
// 	age: 24,
// 	single: true,
// 	address: {
// 	street: 'Bezalel',
// 	num: 4,
// 	city: 'Ramat Gan',
// 	zipcode: {
// 		num: 879865
// 	}
// },
// fav: ['banana','kiwi','orange'],
// tv:[
// {name:'friend',year:1997},
// {name:'breaking bad',year:2010},
// {name:'stranger things',year:2018}
// ]
// }
// console.log(obj.tv[1].name);
// console.log(obj.fav[1]);
// console.log(obj.address.zipcode.num);
// console.log(obj.lastname);
// console.log(obj["lastname"]);
// console.log(obj.single);

//Exercise 1
let obj={
	username: 'charlestraubro',
	password: 'trautrau',
}
database=[obj],

newsfeed=[
{username : "charles1", timeline: "zero"},
{username : "charles2", timeline: "one"},
{username : "charles3",timeline: "two"}
]


console.log(database[0].password);
