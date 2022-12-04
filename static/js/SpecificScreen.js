//지도
var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
var options = { //지도를 생성할 때 필요한 기본 옵션
	center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
	level: 3 //지도의 레벨(확대, 축소 정도)
};

var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴


//찜하기
var shoplike_img = document.getElementById("shop_like");

function click_shoplike(){
    if (shoplike_img.value == "1") {
        shoplike_img.src = "/static/img/unlike.png";
        shoplike_img.value = "0";
    }
    else {
        shoplike_img.src = "/static/img/like.png";
        shoplike_img.value = "1";
    }
}





//카카오톡 공유하기

// 사용할 앱의 JavaScript 키 설정
Kakao.init('689fdc991fdc596b7b88c99c12e8efa5');
 
// SDK 초기화 여부를 판단합니다.
console.log(Kakao.isInitialized());

function shareKakao() { 
  // 카카오링크 버튼 생성
  Kakao.Link.sendDefault({
    objectType: 'feed',
    content: {
      title: "식당 이름", // 보여질 제목
      description: "Eat화에서 식당 이름을 공유했어요", // 보여질 설명
      imageUrl: "https://www.google.com/", // 콘텐츠 URL
      link: {
         mobileWebUrl: "https://www.google.com/",
         webUrl: "https://www.google.com/"
      }
    }
  });
}




//주소 클립보드 복사
function clipboardShare() {

    var content = document.getElementById("location");

    var t = document.createElement("location").value;
    document.body.appendChild(t);
    t.value = text;
    t.select();
    document.execCommand('copy');
    document.body.removeChild(t);
    alert("복사되었습니다.")
}
