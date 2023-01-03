#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write(char);
      }
      process.stdout.write('\n');
    }
  }
};