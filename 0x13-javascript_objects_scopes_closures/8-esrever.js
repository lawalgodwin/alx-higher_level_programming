#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  let l;
  while ((l = list.pop())) reversedList.push(l);
  return reversedList;
};
