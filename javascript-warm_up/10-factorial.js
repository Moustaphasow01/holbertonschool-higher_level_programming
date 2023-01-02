#!/usr/bin/node
/*
factoriel
*/

function facto (a) {
    let res = 1;
    for (let i = 0; i < a; i++) {
      res *= (i + 1);
    }
    return res;
  }
  console.log(facto(parseInt(process.argv[2])));