#!/usr/bin/node

const arg1 = process.argv[2]; // get the first argument passed to the script, which is the third element in the process.argv array
const arg2 = process.argv[3]; // get the second argument passed to the script, which is the fourth element in the process.argv array
console.log(arg1 + ' is ' + arg2); // print the two arguments concatenated with " is " in between
