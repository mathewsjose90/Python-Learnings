var http = require('http');
var fs = require('fs');

function send404Response(response) {
    response.writeHead(404, { 'Content-Type': 'text/plain' });
    response.write("Page not found!")
    response.end();
}
//handle user requests
function onRequest(request, response) {
    console.log('Recieved a request:' + request.url);
    if (request.method == 'GET' && request.url == '/') {
        response.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('./index.html').pipe(response);
    } else {
        send404Response(response);
    }

}

http.createServer(onRequest).listen(8888);
console.log("Server is started")