const binarySearch = (array, target, base = 0) => {
  if (array.length === 1 && array[0] !== target) return -1;

  const centerIndex = Math.floor(array.length / 2);
  const centerValue = array[centerIndex];

  if (centerValue === target) return centerIndex + base;

  if (target < centerValue) {
    return binarySearch(array.slice(0, centerIndex), target, base);
  }
  if (target > centerValue) {
    return binarySearch(
      array.slice(centerIndex, array.length),
      target,
      base + centerIndex
    );
  }

  return -1;
};

const array = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 999, 32,
];

array.sort((a, b) => a - b);

// console.log(array);

console.log(binarySearch(array, 1));
console.log(binarySearch(array, 2));
console.log(binarySearch(array, 3));
console.log(binarySearch(array, 4));
console.log(binarySearch(array, 5));
console.log(binarySearch(array, 6));
console.log(binarySearch(array, 7));
console.log(binarySearch(array, 8));
console.log(binarySearch(array, 9));
console.log(binarySearch(array, 10));
console.log(binarySearch(array, 11));
console.log(binarySearch(array, 12));
console.log(binarySearch(array, 13));
console.log(binarySearch(array, 14));
console.log(binarySearch(array, 15));
console.log(binarySearch(array, 16));
console.log(binarySearch(array, 999));
console.log(binarySearch(array, 32));
