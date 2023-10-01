#!/usr/bin/node

const x = parseInt(process.argv[2]); // get the first argument passed to the script and try to convert it to an integer
if (isNaN(x)) { // check if the result is NaN, which means the argument can't be converted to an integer
  console.log('Missing number of occurrences'); // print "Missing number of occurrences" if the argument can't be converted
} else { // otherwise
  for (let i = 0; i < x; i++) { // use a for loop to iterate x times
    console.log('C is fun'); // print "C is fun" in each iteration
  }
}
