("use strict");
var expect = chai.expect;

function cyfry(napis) {
  var numbers = napis.match(/\d/g);                //any digit global
  var sum = 0;

  if (numbers === null) {
    return 0;
  }

  for (let i = 0; i < numbers.length; i++) {
    sum += parseInt(numbers[i]);
  }

  return sum;
}

function litery(napis) {
  var litery = napis.match(/[a-z]/gi);          //a-z case sensitive global

  if (litery === null) {
    return 0;
  }

  return litery.length;
}

function sum(napis) {

  if (napis.match(/^\d+/g)){
    add_for_sum += parseInt(napis.match(/^\d+/g))                    //jezeli napis zaczyna sie od cyfry, potem cokolwiek, globalny
  }

  return add_for_sum;
}

var add_for_sum = 0;
do {
  input = window.prompt("Podaj napis");

  if (input != null){
    console.log(`\t ${cyfry(input)} \t ${litery(input)} \t ${sum(input)}`);                 //output as specified in ex.
  }

} while (input != null);

describe("Funkcja cyfry()", function () {       //cyfry test
  it("Returns 6 for 123", function () {
    expect(cyfry("123")).to.equal(6);
  });

  it("Returns 5 for ascijo^$@1SA111ASDHU^H$#*(SC(VC)S$^1", function () {
    expect(cyfry("ascijo^$@1SA111ASDHU^H$#*(SC(VC)S$^1")).to.equal(5);
  });

  it("Returns 0 for rpotorkeytovpdspokpsod", function () {
    expect(cyfry("rpotorkeytovpdspokpsod")).to.equal(0);
  });

  it("Returns 6 for 123IERIJIOI$#J%(", function () {
    expect(cyfry("123IERIJIOI$#J%(")).to.equal(6);
  });

  it("Returns 0 for empty input", function () {
    expect(cyfry("")).to.equal(0);
  });

});

describe("Funkcja litery()", function () {      //litery test
  it("Returns 0 for 1234567890", function () {
    expect(litery("1234567890")).to.equal(0);
  });
  it("Returns 6 for ABC123456789!@#$EFG", function () {
    expect(litery("ABC123456789!@#$EFG")).to.equal(6);
  });
  it("Returns 8 for abcdABCD", function () {
    expect(litery("abcdABCD")).to.equal(8);
  });

  it("Returns 2 for 1AB2191239032-23$(#!@", function () {
    expect(litery("1AB2191239032-23$(#!@")).to.equal(2);
  });

  it("Returns 0 for empty input", function () {
    expect(litery("")).to.equal(0);
  });

});

describe("Funkcja suma()", function () {        //suma test
  before(function () {                  //runs before all tests in this file
    var add_for_sum = 0;
  });
  beforeEach(function () {              //runs before each test in this block
    add_for_sum = 0;
  });
  afterEach(function () {               //runs after each test in this block - "reseting" add_for_sum
    add_for_sum = 0;
  });

  it("Returns 0 for empty input", function () {
    sum("");
    expect(add_for_sum).to.equal(0);
  });

  it("Returns 111 for 111", function () {
    sum("111");
    expect(add_for_sum).to.equal(111);
  });

  it("Returns 111 for 111 and !111 afterwards", function () {
    sum("111");
    sum("!111");
    expect(add_for_sum).to.equal(111);
  });

  it("Returns 222 for 111 and 111!@#$%ABCDE afterwards", function () {
    sum("111");
    sum("111!@#$%ABCDE");
    expect(add_for_sum).to.equal(222);
  });
});