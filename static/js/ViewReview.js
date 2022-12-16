//리뷰 작성하기
function fail_write_review(){
    var result = confirm("리뷰 작성은 로그인 후 이용가능합니다. 로그인하시겠습니까?");
        
    if(result)
    {
        location.href='/login';
    }
    else
    {
        location.href='/viewreview/' + name + '/';
    }
}

