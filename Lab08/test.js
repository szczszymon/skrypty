'use strict'

var expect = chai.expect;

function sum(x,y) {
    return x+y;
}

describe('The sum() function', function() {
    it('Returns 4 for 2+2', function() {
        expect(sum(2,2)).to.equal(4);
    });
    it('Returns 0 for -2+2', function() {
        expect(sum(-2,2)).to.equal(0);
    });

    it('Test cyfry()', function () {
        chai.assert.equal(cyfry('111'), 3);
        chai.assert.equal(cyfry('11aa'), 2);
        chai.assert.equal(cyfry('b3345a'), 15);
        chai.assert.equal(cyfry('1a2b3c2d1e'), 9);
        chai.assert.equal(cyfry('123456789'), 45);
        chai.assert.equal(cyfry('abcdef'), 0);
        chai.assert.equal(cyfry(''), 0);
    });

    it('Test litery()', function () {
        chai.assert.equal(litery('111'), 0);
        chai.assert.equal(litery('11aa'), 2);
        chai.assert.equal(litery('b3345a'), 2);
        chai.assert.equal(litery('abcdefgh'), 8);
        chai.assert.equal(litery('1a2b3c2d1e'), 5);
        chai.assert.equal(litery(''), 0);
    });

    it('Test suma()', function () {
        chai.assert.equal(suma('111'), 111);
        chai.assert.equal(suma('11aa'), 122);
        chai.assert.equal(suma('b3345a'), 122);
        chai.assert.equal(suma('1a2b3c2d1e'), 123);
        chai.assert.equal(suma('abcdefgh'), 123);
        chai.assert.equal(suma(''), 123);
        chai.assert.equal(suma('programowanie877'), 123);
        chai.assert.equal(suma('877skryptowe'), 1000);
    });
});