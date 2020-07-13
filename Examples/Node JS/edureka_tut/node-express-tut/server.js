const express=require('express');

const app=express();

app.get("/",(req, res)=>{
    res.send('Hello from Matz in express');
})

app.post("/",(req,res)=>{
    res.send("Post method received :HOME");
})

var port=8888;
app.listen(port,()=>{
    console.log("Server is started at ",port )
});