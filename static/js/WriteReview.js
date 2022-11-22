var eval1_btn = document.getElementById("eval1");
var eval1_star = document.getElementById("eval1_star");
var eval2_btn = document.getElementById("eval2");
var eval2_star = document.getElementById("eval2_star");
var eval3_btn = document.getElementById("eval3");
var eval3_star = document.getElementById("eval3_star");
var eval4_btn = document.getElementById("eval4");
var eval4_star = document.getElementById("eval4_star");
var eval5_btn = document.getElementById("eval5");
var eval5_star = document.getElementById("eval5_star");
var eval6_btn = document.getElementById("eval6");
var eval6_star = document.getElementById("eval6_star");

var eval_btn_list = [eval1_btn, eval2_btn, eval3_btn, eval4_btn, eval5_btn, eval6_btn];
var eval_star_list = [eval1_star, eval2_star, eval3_star, eval4_star, eval5_star, eval6_star];

function click_btn(eval_btn_num){
	for (var i=0; i<6; i++) {
		if ((eval_btn_num-1) == i) {
			click_eval_btn(eval_btn_list[i], eval_star_list[i]);
		}
		else {
			click_other_eval_btn(eval_btn_list[i], eval_star_list[i]);
		}
	}
}


function click_eval_btn(eval_btn, eval_star) {
	eval_btn.style.border = 'solid';
	eval_btn.style.borderColor = '#00462A';
	eval_btn.style.backgroundColor = '#E4F0EB';
	eval_btn.style.color = 'black';
	eval_btn.style.fontweight = 'bold';
	eval_star.style.display ='flex';
	eval_star.style.visibility ='visible';
}

function click_other_eval_btn(eval_btn, eval_star) {
	eval_btn.style.border = 'none';
	eval_btn.style.backgroundColor = '#00462A';
	eval_btn.style.color = 'white';
	eval_btn.style.fontweight = 'normal';
	eval_star.style.display ='none';
	eval_star.style.visibility ='hidden';
}





//$("#file").on('change',function(){
  
//});


function previewImage(targetObj, View_area) {
   var preview = document.getElementById(View_area); //div id
   var ua = window.navigator.userAgent;
    
    var target = document.getElementById('file');
    var target2 = document.getElementById('upload');
    target2.innerHTML = target.files[0].name;

  //ie일때(IE8 이하에서만 작동)
   if (ua.indexOf("MSIE") > -1) {
      targetObj.select();
      try {
         var src = document.selection.createRange().text; // get file full path(IE9, IE10에서 사용 불가)
         var ie_preview_error = document.getElementById("ie_preview_error_" + View_area);


         if (ie_preview_error) {
            preview.removeChild(ie_preview_error); //error가 있으면 delete
         }

         var img = document.getElementById(View_area); //이미지가 뿌려질 곳

         //이미지 로딩, sizingMethod는 div에 맞춰서 사이즈를 자동조절 하는 역할
         img.style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='"+src+"', sizingMethod='scale')";
      } catch (e) {
         if (!document.getElementById("ie_preview_error_" + View_area)) {
            var info = document.createElement("<p>");
            info.id = "ie_preview_error_" + View_area;
            info.innerHTML = e.name;
            preview.insertBefore(info, null);
         }
      }
  //ie가 아닐때(크롬, 사파리, FF)
   } else {
      var files = targetObj.files;
      for ( var i = 0; i < files.length; i++) {
         var file = files[i];
         var imageType = /image.*/; //이미지 파일일경우만.. 뿌려준다.
         if (!file.type.match(imageType))
            continue;
         var prevImg = document.getElementById("prev_" + View_area); //이전에 미리보기가 있다면 삭제
         if (prevImg) {
            preview.removeChild(prevImg);
         }
         var img = document.createElement("img"); 
         img.id = "prev_" + View_area;
         img.classList.add("obj");
         img.file = file;
         img.style.width = '280px'; 
         img.style.height = '220px';
         preview.appendChild(img);
         if (window.FileReader) { // FireFox, Chrome, Opera 확인.
            var reader = new FileReader();
            reader.onloadend = (function(aImg) {
               return function(e) {
                  aImg.src = e.target.result;
               };
            })(img);
            reader.readAsDataURL(file);
         } else { // safari is not supported FileReader
            //alert('not supported FileReader');
            if (!document.getElementById("sfr_preview_error_"
                  + View_area)) {
               var info = document.createElement("p");
               info.id = "sfr_preview_error_" + View_area;
               info.innerHTML = "not supported FileReader";
               preview.insertBefore(info, null);
            }
         }
      }
   }
}
