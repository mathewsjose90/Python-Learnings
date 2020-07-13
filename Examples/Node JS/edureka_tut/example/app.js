var express=require('express');
var routes=require('./routes');
var http=require('http');
var path=require('path');
var urlencoded=require('url');
var bodyParser=require('body-parser');
var json=require('json');
var logger=require('logger');
var methodOverride=require('method-override');

var couchuser='admin';
var couchpass='admin1234';
var nano=require('nano')('http://'+couchuser+':'+couchpass+'@localhost:5948')
var db=nano.use('address');

var app=express();

app.set('port',process.env.PORT||8888);
app.set('views',path.join(__dirname,'views'));
app.set('view engine','jade');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(methodOverride());
app.use(express.static(path.join(__dirname,'public')));


//app.get('/',routes.index);
app.get('/', function (req, res) {

    res.render('index',{title:'Express'});

});

app.post('/createdb',function(req, res){
    nano.db.create(req.body.dbname,function(err,body){
        if(err){
            res.send('Error creating Database '+req.body.dbname +'Err: '+err);
            return ;
        }
        res.send('Database '+req.body.dbname + ' created successfuly');
    });
});

app.post('/new_contacts',function(req, res){
    var name=req.body.name;
    var phone=req.body.phone;
    db.insert({name:name,phone:phone,crazy:true},phone,function (err,body,header){
        if(err){
            res.send('Error creating contact');
            return;
        }
        res.send('User contacts created successfully');
    });
});


app.post('/view_contact',function (req, res){
    var alldoc="Below are the contact details:";
    db.get(req.body.phone,{revs_info:true},function (err, body){
        if(!err){
            console.log(body);

        }
        if(body){
            alldoc+="Name:"+body.name+"<br>Phone:"+body.phone;
            
        }
        else{
            alldoc="No Records found";
        }
        res.send(alldoc);
    });
});


app.post('/delete_contact',function (req, res){
    db.get(req.body.phone,{revs_info:true},function (err, body){
        if(!err){
            db.destroy(req.body.phone,body._rev,function(err,body){
                if(err){
                    res.send('Error deleting contacts');
                }
                res.send('Contact deleted successfully');
            })
        }
    });
});

http.createServer(app).listen(app.get('port'),function(){
    console.log('Express server is started on port:'+app.get('port'));
});





