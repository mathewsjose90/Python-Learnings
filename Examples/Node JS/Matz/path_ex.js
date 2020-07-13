var path = require('path');

var mypath = '/root/mathews/testdata/test.txt';
var mypath2 = '/root/mathews/testdata/test.txt';

console.log(path.basename(mypath));
console.log(path.normalize(mypath2));
console.log(path.dirname(mypath2));
console.log(path.extname(mypath2));