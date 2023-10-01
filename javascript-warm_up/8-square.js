#!/usr/bin/node

const arg = process.argv[2]; 
if (isNaN(arg)) { // check if the result is NaN, which means the argument can't be converted to an integer
  console.log('Missing size'); // print "Missing size" if the argument can't be converted
} else { // otherwise
  const size = parseInt(arg, 10);
  if (size < 1){
	// Size is less than 1; no square to print
  } else {
    for (let j = 0; j < size; j++) { // use a loop to iterate
      console.log(square); // print the square string using console.log
      }
  }
}
