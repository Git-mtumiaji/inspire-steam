var x = 20;
var y = 30;
//definition
function add_numbers( x, y){
    sum = x + y;
    return sum;

}
//Calling the function

console.log(add_numbers(x,y));

var sum2 = 0;
var last = 50;
function sum_numbers(last){

    for( var i = 0; i < last; i++){

        sum2 = sum2 + i;
    } 
    return sum2;
}
console.log(sum_numbers(last));