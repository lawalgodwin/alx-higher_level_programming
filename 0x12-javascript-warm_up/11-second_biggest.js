#!/usr/bin/node

if (process.argv.length <= 3) console.log(0);

else {
  const numArrays = process.argv.slice(2);
  numArrays.sort((a, b) => (b - a));
  console.log(numArrays[1]);
}
