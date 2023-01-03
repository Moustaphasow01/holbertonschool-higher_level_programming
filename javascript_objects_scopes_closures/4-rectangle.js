#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
  
    rotate () {
      const x = this.height;
      this.height = this.width;
      this.width = x;
    }
  
    double () {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
  module.exports = Rectangle;