var Matz={
    printmyname:function(){
        console.log('My name is :Matz');
        console.log(this===Matz)
    }
}

Matz.printmyname()

//Default context is global
function somefunc(){
    console.log('Test func')
    console.log(this===global)
}
somefunc();