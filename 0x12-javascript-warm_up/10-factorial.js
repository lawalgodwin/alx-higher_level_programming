#!/usr/bin/node

function factorial (n) {
  if (!n || !parseInt(n)) {
    return (1);
  }
  n = parseInt(n);
  return (n * factorial(n - 1));
}

console.log(factorial(process.argv[2]));
