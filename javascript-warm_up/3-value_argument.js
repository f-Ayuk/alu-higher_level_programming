#!/usr/bin/node

let firstArg = process.argv[2]; // get the first argument passed to the script, which is the third element in the process.argv array
if (firstArg === undefined) { // check if the first argument is undefined, which means no arguments are passed
  console.log('No argument'); // print "No argument" if no arguments are passed
} else { // otherwise
  console.log(firstArg); // print the first argument if it exists
}
