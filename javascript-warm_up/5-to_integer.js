#!/usr/bin/node

let arg = process.argv[2]; // get the first argument passed to the script, which is the third element in the process.argv array
let num = parseInt(arg); // try to convert the argument to an integer using the parseInt function
if (isNaN(num)) { // check if the result is NaN, which means the argument can't be converted to an integer
  console.log("Not a number"); // print "Not a number" if the argument can't be converted
} else { // otherwise
  console.log("My number: " + num); // print "My number: " followed by the converted integer
}
