function fail_mypage(){
    var result = confirm("로그인 후 이용가능한 페이지입니다. 로그인하시겠습니까?");
        
    if(result)
    {
        location.href='/login';
    }
    else
    {
        location.href='/index';
    }
        
}

//데이터 수정, 삭제 시 사용. 로그인하지 않겠다고 선택하면 현재 페이지에 머무름
function fail_datachange(){
    var result = confirm("로그인 후에 가능합니다. 로그인하시겠습니까?");
        
    if(result)
    {
        location.href='/login';
    }
    else
    {
        location.href=window.location.href;
    }
        
}

function click_btn(){
    document.getElementById("recommend").style.visibility="";
    setTimeout(() => {
        window.location.reload(); 
      }, 3000)
    
}
var clicked=0;
function show_drop(){
    if(clicked==0){
        document.getElementById("dropdown").style.display="flex";
        document.getElementById("down_btn").innerHTML="▲";
        clicked=1;
    }
    
    else{
        document.getElementById("dropdown").style.display="none";
        document.getElementById("down_btn").innerHTML="▼";
        clicked=0;
       
    }
}


document.addEventListener('mouseup', function(e) {
    var container = document.getElementById("dropdown");
    var btn=document.getElementById("down_btn");
    if (!btn.contains(e.target)&& !container.contains(e.target)) {
        container.style.display = "none";
        document.getElementById("down_btn").innerHTML="▼";
        clicked=0;
    }
});


//찜하기
function fail_shop_like(){
    var result = confirm("찜 기능은 로그인 후 이용가능합니다. 로그인하시겠습니까?");
        
    if(result)
    {
        location.href='/login';
    }
    else
    {
        location.href='/index';
    }
        
}




var shoplike_img0 = document.getElementById("shop_like0");

function click_shoplike0(){
    if (shoplike_img0.value == "1") {
        shoplike_img0.src = "/static/img/unlike.png";
        shoplike_img0.value = "0";
    }
    else {
        shoplike_img0.src = "/static/img/like.png";
        shoplike_img0.value = "1";
    }
}

var shoplike_img1 = document.getElementById("shop_like1");

function click_shoplike1(){
    if (shoplike_img1.value == "1") {
        shoplike_img1.src = "/static/img/unlike.png";
        shoplike_img1.value = "0";
    }
    else {
        shoplike_img1.src = "/static/img/like.png";
        shoplike_img1.value = "1";
    }
}

var shoplike_img2 = document.getElementById("shop_like2");

function click_shoplike2(){
    if (shoplike_img2.value == "1") {
        shoplike_img2.src = "/static/img/unlike.png";
        shoplike_img2.value = "0";
    }
    else {
        shoplike_img2.src = "/static/img/like.png";
        shoplike_img2.value = "1";
    }
}

