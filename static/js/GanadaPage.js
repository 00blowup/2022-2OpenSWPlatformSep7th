/*function print_nameGa(ga_data){
    
    i=0;
    while(ga_data[i]){
        const Atag = document.createElement('a');
        Atag.setAttribute('src', "#");
        const textNode=document.createTextNode(ga_data[i]);

        Atag.appendChild(textNode);
        document.querySelector('li ga').appendChild(Atag);
        i++;
    }
       
}

print_nameGa(ga_data);*/


function print_Ga(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("gaa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Na(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("naa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Da(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("daa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ra(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("raa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ma(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("maa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ba(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("baa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Sa(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("saa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Aa(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("aaa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ja(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("jaa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Cha(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("chaa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ka(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("kaa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ta(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("taa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Fa(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("faa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

function print_Ha(ga) {
    i=0;
    while(i<ga.length){
        var Atag = document.createElement("a");
        Atag.setAttribute('src', "#");
        Atag.setAttribute('class', 'astyle');
        var textNode = document.createTextNode(ga[i]);
        Atag.appendChild(textNode);
        var parent= document.getElementById("haa");
        parent.appendChild(Atag); 
        i+=1;
    }  
}

print_Ga(ga_list);
print_Na(na_list);
print_Da(da_list);
print_Ra(ra_list);
print_Ma(ma_list);
print_Ba(ba_list);
print_Sa(sa_list);
print_Aa(aa_list);
print_Ja(ja_list);
print_Cha(cha_list);
print_Ka(ka_list);
print_Ta(ta_list);
print_Fa(Fa_list);
print_Ha(Ha_list);


