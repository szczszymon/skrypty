'use strict'

let state = 0;

function cyfry(data) {
    let ctr = 0;

    for (let i = 0; i < data.length; i++) {
        if(!isNaN(parseInt(data[i])))
            ctr += parseInt(data[i]);
    }//for

    return ctr;
}//cyfry()

function litery(data) {
    let ctr = 0;
    for (let i = 0; i < data.length; i++) {
        if(isNaN(parseInt(data[i])))
            ctr ++;
    }//for

    return ctr;
}//litery()

function suma(data) {
    if (!isNaN(parseInt(data)))
        state += parseInt(data);
    return state
}//suma()