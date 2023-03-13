#!/usr/bin/node

let argsCount = 0;

for (let i = 0; process.argv[i]; i++) argsCount += 1;

if (argsCount === 2) console.log('No argument');

else console.log(process.argv[2]);
