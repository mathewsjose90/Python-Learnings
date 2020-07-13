var http=require('http');
var events=require('events');


var eventEmitter=new events.EventEmitter();



eventEmitter.on('test-event',()=>{
    console.log('Some request happened on the web page');
});




var server=http.createServer((req,res)=>{
    eventEmitter.emit('test-event');
    res.write("Hello from matz");
    res.end();

});

server.listen(8888,()=>{
    console.log('Server started on 8888')
})