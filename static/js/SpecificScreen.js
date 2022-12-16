//지도
var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
var options = { //지도를 생성할 때 필요한 기본 옵션
	center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
	level: 2 //지도의 레벨(확대, 축소 정도)
};

var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();

var address = document.getElementById('location').innerText;

var name = document.getElementById('restaurant_name').innerText;

// 주소로 좌표를 검색합니다
geocoder.addressSearch(address, function(result, status) {

    // 정상적으로 검색이 완료됐으면 
     if (status === kakao.maps.services.Status.OK) {

        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
         
        // 결과값으로 받은 위치를 마커로 표시합니다
        var marker = new kakao.maps.Marker({
            map: map,
            position: coords
        });

        // 인포윈도우로 장소에 대한 설명을 표시합니다
        var infowindow = new kakao.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:6px 0;font-size:20px;">' + name + '</div>'
        });
        infowindow.open(map, marker);

        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
        map.setCenter(coords);
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
        location.href='/specificscreen/' + name + '/';
    }
        
}




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
      title: name, // 보여질 제목
      description: "Eat화에서 " + name + "을 공유했어요", // 보여질 설명'/specificscreen/' + name + '/'
      imageUrl: "http://eatwha-97.run.goorm.io/specificscreen/" + name + "/", // 콘텐츠 URL
      link: {
         mobileWebUrl: "http://eatwha-97.run.goorm.io/specificscreen/" + name + "/",
         webUrl: "http://eatwha-97.run.goorm.io/specificscreen/" + name + "/"
      }
    }
  });
}




