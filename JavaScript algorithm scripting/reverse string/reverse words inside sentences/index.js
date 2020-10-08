const str = 'Hello World!'


function b(str) {
    // we split the argument which it's a string. so it return: [ 'Hello', 'World!' ]
    return str.split(' ').map(e => {
        // iterate each of the element.

        // now it return ['h', 'e', 'l', 'l', 'o'] because we split it and if we reverse it it will return : [ 'o', 'l', 'l', 'e', 'H' ]. if we join it, we change the array to become a string.
        return e.split('').reverse().join('')
    }).join(' ') /**  we join it because we want change the array become a string **/;
}

// try with your own!

b(str);

// node index.js 
// print out: 
// olleH !dlroW