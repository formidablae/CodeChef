// this is the solution i have submitted
process.stdin.resume();
process.stdin.setEncoding('utf-8');

var inputData = "";

process.stdin.on('data', function(chunk) {
  inputData += chunk;
});

process.stdin.on('end', function() {
  inputDataArray = inputData.split("\n");
  while (inputDataArray.length > 0) {
      let x = inputDataArray.shift();
      if (x === "42") {break;}
      console.log(x)
  }
});
