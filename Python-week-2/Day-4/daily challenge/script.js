let bottles = 0;
for (let i = 99; i > 0; i -= bottles) {
  bottles++;
  console.log(`${i} bottles of beer on the wall`);
  console.log(`${i} bottles of beer`);
  if(i>bottles){
    console.log(`Take ${bottles} down, pass it around`);
    console.log(`${i-bottles} bottles of beer on the wall`);
  }
  else{
    console.log(`Take ${i} down, pass it around`);
    console.log(`0 bottles of beer on the wall`);
  }
  console.log('#######################################');
}