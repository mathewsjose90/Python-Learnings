function User(){
    this.name="";
    this.life=100;
    this.giveLife=function giveLife(targetPlayer){
        targetPlayer.life+=1;
        console.log(this.name +" gave 1 life to "+targetPlayer.name);
    }
}

var Matz=new User();
var Nick=new User();
Matz.name="matz";
Nick.name="nick";

Matz.giveLife(Nick);
console.log("Matz:"+Matz.life);
console.log("Nick:"+Nick.life);

//Prototyping a new property
User.prototype.supershot=function supershot(targetPlayer) {
    console.log(this.name+" took a superhot on "+targetPlayer.name);
    targetPlayer.life-=3;
}

Nick.supershot(Matz);
console.log("Matz:"+Matz.life);
console.log("Nick:"+Nick.life);

//We can add new properties to objects
User.prototype.magic=50;
console.log(Matz.magic);
console.log(Nick.magic);