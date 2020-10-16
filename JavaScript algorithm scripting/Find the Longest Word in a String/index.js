function findLongestWordLength(str) {
    // we use Math.max to find out which is the biggest number 
    // we use spread operator to spread out the array, it's become an array because of split operator
    // we return a new array using map (to iterate each of the element inside the array that we split)
    return Math.max(...str.split(" ").map(e => {
        // we return the word length. we make it array first because of split operator.
        return e.split('').length;
    }));
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));

// node index.js
/*
will printout: 6
*/