#!/usr/bin/node

const size = parseInt(process.argv[2]); // get the first argument passed to the script and try to convert it to an integer
if (isNaN(size)) { // check if the result is NaN, which means the argument can't be converted to an integer
  console.log('Missing size'); // print "Missing size" if the argument can't be converted
} else { // otherwise
  let square = ""; // create an empty string to store the square
  for (let i = 0; i < size; i++) { // use a for loop to iterate over the rows of the square
    for (let j = 0; j < size; j++) { // use another for loop to iterate over the columns of the square
      square += "X"; // append an "X" character to the square string for each column
    }
    square += "\n"; // append a newline character to the square string for each row
  }
  console.log(square); // print the square string using console.log
}
