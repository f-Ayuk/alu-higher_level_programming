#!/usr/bin/node

function factorial (n) { // define a function with the prototype function factorial(n)
  if (isNaN(n) || n < 0) { // check if the parameter is NaN or negative, which are invalid inputs
    return 1; // return 1 as the default value for invalid inputs
  }
  if (n === 0 || n === 1) { // check if the parameter is 0 or 1, which are the base cases
    return 1; // return 1 as the factorial of 0 or 1
  }
  return n * factorial(n - 1); // return the product of n and the factorial of n - 1, which is the recursive case
}

const arg = parseInt(process.argv[2]); // get the first argument passed to the script and try to convert it to an integer
const result = factorial(arg); // call the factorial function with the argument and store the result
console.log(result); // print the result using console.log
