#!/usr/bin/node
/*
integer
*/

const n = parseInt(process.argv[2]);

if (Number.isInteger(n)) {
  console.log('My number: %s', process.argv[2]);
} else {
  console.log('Not a number');
}