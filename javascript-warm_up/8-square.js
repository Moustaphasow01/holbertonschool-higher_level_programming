#!/usr/bin/node
/*
square
*/

const arg = process.argv[2];
if (arg === undefined || isNaN(arg)) {
  console.log('Missing size');
}
for (let i = 0; i < arg; i++) {
  for (let i = 0; i < arg; i++) {
    process.stdout.write('X');
  }
  process.stdout.write('\n');
}