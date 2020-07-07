var connect=require('connect');
var http=require('http');

var app=connect();

function do_first(request,response,next){
    console.log('Matz');
    next();
}

function do_second(request,response,next){
    console.log(' Hiii Matz');
}

function profile(request, response){
    console.log('Profile details')
}
function forum(request, response){
    console.log('Forum details');
}
// app.use(do_first);
// app.use(do_second);
app.use('/profile',profile);
app.use('/forum',forum);

http.createServer(app).listen(8888);
console.log("Server is started")