#!/usr/bin/node

exports.converter = function (base) {
  return (n) => Math.abs(n).toString(base);
};
