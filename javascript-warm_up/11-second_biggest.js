#!/usr/bin/node

const args = process.argv.slice(2); // get the array of arguments passed to the script, excluding the first two elements (node and file name)
if (args.length === 0 || args.length === 1) { // check if the array is empty or has only one element
  console.log(0); // print 0 if no argument or only one argument is passed
} else { // otherwise
  let nums = args.map(arg => parseInt(arg)); // map the array of arguments to an array of integers using the parseInt function
  let max = Math.max(...nums); // find the maximum value in the array using the Math.max function with the spread operator
  let secondMax = -Infinity; // initialize a variable to store the second maximum value, starting from -Infinity
  for (let num of nums) { // use a for-of loop to iterate over the array of integers
    if (num < max && num > secondMax) { // check if the current element is less than the maximum value and greater than the second maximum value
      secondMax = num; // update the second maximum value with the current element
    }
  }
  console.log(secondMax); // print the second maximum value using console.log
}
