#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(3, 3);
console.log('Rectangle 'r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(3, -3);
console.log('Rectangle 'r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(3);
console.log('Rectangle 'r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(0, 3);
console.log('Rectangle 'r4);
console.log(r4.width);
console.log(r4.height);

const r5 = new Rectangle();
console.log('Rectangle 'r5);
console.log(r5.width);
console.log(r5.height);