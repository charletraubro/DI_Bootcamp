// for (let i = 0; i < 16; i++)
// 	if (i % 2 == 0) {
// 		console.log(i, "is even")
// 	}
// 	else {
// 		console.log  (i, "is odd")
// 	}



// let names= ["john", "sarah", 23, "Rudolf",34]
// for (let i = 0; i < names.length; i++) {
// 	if( isNaN(names[i]) && names[i].charAt(0).toLowerCase() === names[i].charAt(0)){
// 		names[i] = names[i].charAt(0).toUpperCase() + names[i].slice(1);
// 	}
// 	else {
// 		names.splice (i,1)
// 	}
// }
// console.log(names);

//------exercise 1 --------------
// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift();//removes first element
// people[2]= 'Jason';
// people[3]= 'Charles';
// let last = people[3]

// let arrayLength = people.length;
// for (var i = 0; i < arrayLength; i++) {
// 	if (i===3){
// 		break;
// 	}
// 	console.log(people[i]);
// }



// console.log (last)
// console.log(people.indexOf('Foo')); //it is -1 because it is not found in the array
// console.log(people.slice(1, 3));
// console.log(people.indexOf('Mary'));
// console.log (people)

// /let b = 3, d = b, u = b;

// const tree = ++d * d*b * b++ +
//  + --d+ + +b-- +
//  + +d*b+ +
//  u

// console.log(tree); // 163
//--------exercise 2-------------------------------

// let colors = ["Blue", "White", "Gold", "Black", "Silver"];
// let i = 0;
// while (i < colors.length){
// 	console.log("My #1 choice is " + colors[i]);
// 	i++; 
// }
//----------exercise 3-----------------------

// let ex = prompt('chose a number')
// let num = Number(ex)
// while (typeof num == 'number' && num < 10){
// 	ex = prompt ('chose a number')
// 	num = Number(ex)
// 	console.log ('number')
// }

//----------exercise 4 ----------------------


// let building = {
// 	numberOfFloors : 4,
// 	numberOfAptByFloor : {
// 		firstFloor : 3,
// 		secondFloor : 4,
// 		thirdFloor : 9,
// 		fourthFloor : 2,
// 	},
// 	nameOfTenants : ["Sarah", "Dan", "David"],
// 	numberOfRoomsAndRent:  {
// 		sarah: [3, 990],
// 		dan :  [4, 1000],
// 		david : [1, 500],
// 	},
// }

// console.log (building.numberOfFloors)
// console.log (building.numberOfAptByFloor.firstFloor)
// console.log (building.numberOfAptByFloor.thirdFloor)
// console.log (building.nameOfTenants [1], building.numberOfRoomsAndRent.dan [0])
// console.log	(building.numberOfRoomsAndRent.sarah[1],building.numberOfRoomsAndRent.david [1] )
// building.numberOfRoomsAndRent.dan[1]=1200
// console.log (building.numberOfRoomsAndRent.dan[1])
//------------exercise 5---------------------------



// let family = {
// 	brother: 'david',
// 	sister: 'limor',
// 	father: 'erez'
// };

// // for (const property in family) {
// // 	console.log (`${family[property]}`);

// // }

// for (const property in family) {
// 	console.log(`${property}:`);
// }

///-----------exercise 6 -------------