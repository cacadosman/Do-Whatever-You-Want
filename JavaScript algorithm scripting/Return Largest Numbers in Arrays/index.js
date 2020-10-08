function largestOfFour(arr) {
    // we return an array using map. which it iterate over the arr argument
    return arr.map(e => {
        // we return the largest numbers inside the each of element. And we use spread operator, because Math.max can't find out the largest number inside of array
        return Math.max(...e)
    });
}

// we log it
console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));