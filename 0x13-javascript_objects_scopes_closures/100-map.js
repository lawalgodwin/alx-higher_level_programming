#!/usr/bin/node

const { list } = require('./100-data');

const newList = list.map((e, idx) => (e * idx));

console.log(list);
console.log(newList);
