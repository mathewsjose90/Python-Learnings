function place_an_order(ordernumber){
    console.log('Customer order  received:',ordernumber);

    coook_and_deliver(function(){
        console.log("Cooked and delivered order no:",ordernumber)
    });
}

//Simulate a 5 secs operation
function coook_and_deliver(callback){
    setTimeout(callback,5000);
}

//Simulate Users
place_an_order(1)
place_an_order(10)
place_an_order(20)
place_an_order(30)
place_an_order(40)