#!/usr/bin/node
/*
biggest
*/

if (process.argv.length > 3) {
    const arg = process.argv.slice(2);
    arg.sort(function (a, b) { return b - a; });
    console.log((arg[1]));
  } else {
    console.log('0');
  }