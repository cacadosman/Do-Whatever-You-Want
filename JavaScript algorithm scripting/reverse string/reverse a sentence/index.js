const str = 'Hello World!'

function b(str) {
    // so we return an array because of split method, then we reverse the element inside the array, after that we use join method to change the array become a string.

    // visualization :
    /*
    ['hello', 'world!'] because we split it
    ['wolrd!', 'hello'] because we reverse it using reverse method
    world! hello it become a string because of join.

    so what means of join method? Join method means we change the coma[s] in an array depends on the join argument

    for example:
    ['HEY!', 'YO!', 'HALLO'].join('-') become : HEY!-YO!-HALLO
    if we did not join it, and if we console it, it will prints out: ['HEY!', 'YO!', 'HALLO']
    */
    return str.split(' ').reverse().join(' ');
}

b(str)


// node index.js