// I'm confused where to start
/*

Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.

chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2) should return [[0, 1], [2, 3], [4, 5]]

*/

function chunkArrayInGroups(arr, size) {
    var newArray = [];
    for (let i = 0; i < arr.length; i++) {
        // console.log(i)
        if (i == 0) {
            newArray.push(arr.slice(i, size))
        } else if (i % size == 0 && i != 0) {
            // console.log('HEY!')
            // console.log(arr[i])
            // console.log(arr.indexOf(arr[i]))
            let x = arr.indexOf(arr[i])
            console.log(x)
            x = arr.slice(x, x + size)
            newArray.push(x)
        }
    }
    return newArray;
}

console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4));