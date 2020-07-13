const express=require('express');
const bodyParser=require('body-parser');

const app=express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

let people={'person':[{'name':'John Nick'}]}

app.get("/people",(req, res)=>{
    //res.send("People information");
    res.json(people);
    res.end();
});

app.post("/people",(req, res)=>{
    //res.send("People information");
    console.log(req.body.name);
    if(req.body && req.body.name){
        people.person.push({"name":req.body.name})
    }
    res.json(people);
    res.end();
});

//Url part is a variable name . Below example the name part is a variable that can be passed in the URL

app.get('/people/:name',(req, res)=>{
    res.json({'name':req.params.name})
    res.send();
});





app.listen(8888,()=>{
    console.log("Server is started...")
});