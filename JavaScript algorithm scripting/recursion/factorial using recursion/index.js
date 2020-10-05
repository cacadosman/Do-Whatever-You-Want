
function factorialize(num) {
    // if num is less than or equal to zero
    if (num <= 0)
        return 1;
    else // if num is not equal or less than zero..
        return num * factorialize(num - 1);
}

// call the function
console.log(factorialize(5));