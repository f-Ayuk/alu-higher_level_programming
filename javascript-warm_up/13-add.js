#!/usr/bin/node

function add (a, b) { // define a function with the prototype function add(a, b)
  return a + b; // return the sum of the two parameters
}

exports.add = add; // export the function as a property of the exports object, which makes it visible from outside
