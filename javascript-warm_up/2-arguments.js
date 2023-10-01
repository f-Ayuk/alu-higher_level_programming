#!/usr/bin/node

let args = process.argv.slice(2); // get the array of arguments passed to the script, excluding the first two elements (node and file name)
if (args.length === 0) { // check if the array is empty
  console.log('No argument'); // print "No argument" if no arguments are passed
} else if (args.length === 1) { // check if the array has only one element
  console.log('Argument found'); // print "Argument found" if only one argument is passed
} else { // otherwise
  console.log('Arguments found'); // print "Arguments found" if more than one argument is passed
}
