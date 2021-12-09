"use strict"                    //tryb scisly dla calego skryptu
var expect = chai.expect;

let inp = window.prompt('Data');
let total = 0;
while (inp != null){
    console.log(inp);
    total += sum(inp);
    console.log("\t"+numbers(inp)+"\t"+chars(inp)+"\t"+ total);
    inp = window.prompt('Data');
}

function numbers(string){
    let sum = 0;
    let num = string.match(/[0-9]+/g);
    if (num != null) {num.map(function(x){return String(x).split('')}).map(function(n){n.forEach(num => {sum += parseInt(num)})});}
    return sum;
}

function chars(string){
    let sum = 0;
    let num = string.match(/[^0-9]+/g)
    if (num != null){ num.map(function(x){return x.split('')}).map(function(x){x.forEach(c => {sum += 1})});}
    return sum;
}

function sum(string){
    return isNaN(parseInt(string)) ? 0 : parseInt(string);
}


describe('The chars() function', function(){
    it('Returns 3 for a123b4342c', function(){
        expect(chars('a123b4342c')).to.equal(3);
    });
    it('Returns 9 for 0azsdfetr1a', function(){
        expect(chars('0azsdfetr1a')).to.equal(9);
    });
    it('Returns 0 for 01321312', function(){
        expect(chars('01321312')).to.equal(0);
    });
});

describe('The numbers() function', function(){
    it('Returns 3 for 111', function(){
        expect(numbers('111')).to.equal(3);
    })
    it('Returns 0 for asdbvclkj', function(){
        expect(numbers('asdbvclkj')).to.equal(0);
    })
    it('Returns 15 for 5sadasda4dsa1as32', function(){
        expect(numbers('5sadasda4dsa1as32')).to.equal(15);
    })
})

describe('All functions for blank string', function(){
    it('Blank for numbers()', function(){
        expect(numbers('')).to.equal(0);
    })
    it('Blank for chars()', function(){
        expect(chars('')).to.equal(0);
    })
    it('Blank for sum()', function(){
        expect(sum('')).to.equal(0);
    })
})