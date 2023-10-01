#!/usr/bin/node

function add (a, b) { // define a function with the prototype function add(a, b)
  return a + b; // return the sum of the two parameters
}

const arg1 = parseInt(process.argv[2]); // get the first argument passed to the script and try to convert it to an integer
const arg2 = parseInt(process.argv[3]); // get the second argument passed to the script and try to convert it to an integer
const result = add(arg1, arg2); // call the add function with the two arguments and store the result
console.log(result); // print the result using console.log
