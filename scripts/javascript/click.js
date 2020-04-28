var mylist = ["watermelon", "pineapple", "apple"];
function go(a, b) {
    alert("This button has not been developed!");
}

mylist.forEach(function(value, index) {
    alert('I have ' +value+ 'in my bag');
});

var times=0;

do {
    console.log("try it", times);
    times++;
} while (times < 10);

for (var i=0; i < mylist.length; i++) {
    alert('My favorite fruit is' + mylist[i]+ ', How about you?');
    prompt('Please tell me your favorite fruit');
}
