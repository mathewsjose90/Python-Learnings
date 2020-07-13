var express=require('express');
var http=require('http');
var fs=require('fs');



var app=express();
var server=http.createServer(app);

app.get('/',(req,res)=>{
    res.send('Hello from Express');
    res.end();
})

app.get('/tasks',(req, res)=>{
    fs.readFile('./db.json',(err,data)=>{
        console.log(data.toString());
        var tasks=JSON.parse(data.toString()).tasks;
        res.json(tasks);
        res.end();
    })
})

server.listen(8888,()=>{
    console.log('Server listens on 3000')
})
