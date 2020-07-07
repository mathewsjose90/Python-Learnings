const nano = require("nano")

exports.create=function(req, res){
    nano.db.create(req.body.dbname,function (err) {
        if(err){
            res.send("Error creating the DB");
            return ;
        }
        res.send('database created successfully');
        });
};