#!/usr/bin/node

/*const arg = process.argv[2]; 
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
}*/

// Get the first argument as a number
let size = Number(process.argv[2]);
// Check if the argument is a valid positive integer
if (isNaN(size) || size <= 0) {
  // Print "Missing size"
  console.log("Missing size");
} else {
  // Initialize an empty string to store the output
  let output = "";
  // Loop from 0 to size - 1
  for (let i = 0; i < size; i++) {
    // Loop from 0 to size - 1
    for (let j = 0; j < size; j++) {
      // Append the character X to the output
      output += "X";
    }
    // Append a newline character to the output
    output += "\n";
  }
  // Print the output
  console.log(output);
}
