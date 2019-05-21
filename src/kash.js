//Kash's soccer thingy/helper

function comp(a,b){
    var c = []; 
    for(var i = 0; i <b.length;i++){
        var count=0; 
        for(var j=0; j< a.length;j++){
            if(a[j]<=b[i]){
                count++; 
            } 
        }
        c.push(count);  
    }  
    return c
    }
var a = [1,2,3];
var b = [2,4];
c = comp(a,b);