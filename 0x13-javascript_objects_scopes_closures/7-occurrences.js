#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const searchItemList = list.filter((e) => e === searchElement);
  return searchItemList.length;
};
