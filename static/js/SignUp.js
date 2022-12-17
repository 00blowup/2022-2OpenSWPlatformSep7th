
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-analytics.js";
  import { getAuth, RecaptchaVerifier, signInWithPhoneNumber } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-auth.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyDvAiPVORTy4O1SCLUFrapA8dYlcya9Fvw",
    authDomain: "osw-eatwha.firebaseapp.com",
    databaseURL: "https://osw-eatwha-default-rtdb.firebaseio.com",
    projectId: "osw-eatwha",
    storageBucket: "osw-eatwha.appspot.com",
    messagingSenderId: "567539050865",
    appId: "1:567539050865:web:b57296f401a8d3414beed0",
    measurementId: "G-HJD8278G04"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);

// reCAPTCHA 검증기 설정
  const auth = getAuth();
  auth.languageCode = 'ko';

    
  window.recaptchaVerifier = new RecaptchaVerifier('sms_button', {
  'size': 'invisible',
  'callback': (response) => {
    // reCAPTCHA solved, allow signInWithPhoneNumber.
    onSignInSubmit();
  }
}, auth);



document
        .getElementById("sms_button")
        .addEventListener("click", (event) => {
          event.preventDefault();

          const phoneNumber = document.getElementById("id").value;
          const appVerifier = window.recaptchaVerifier;

          signInWithPhoneNumber(auth, "+82" + phoneNumber, appVerifier)
            .then((confirmationResult) => {
              alert("인증번호를 전송했습니다");
              // SMS sent. Prompt user to type the code from the message, then sign the
              // user in with confirmationResult.confirm(code).
              window.confirmationResult = confirmationResult;
              console.log(confirmationResult);
              // ...
            })
            .catch((error) => {
              alert("다시 시도해주세요");
              //console.log(error);
              // Error; SMS not sent
              // ...
            });
        });
var success = 0;
document
        .getElementById("confirmcode_button")
        .addEventListener("click", (event) => {
          event.preventDefault();
          const code = document.getElementById("confirmcode").value;
          confirmationResult
            .confirm(code)
            .then((result) => {
              alert("인증이 완료되었습니다");
              // User signed in successfully.
              const user = result.user;
              success = 1;
              console.log(success);
              console.log(user);
              //console.log(result);
              // ...
            })
            .catch((error) => {
              alert("인증번호가 일치하지 않습니다");
              console.log(error);
              // User couldn't sign in (bad verification code?)
              // ...
            });
        });



function click_btn(){
   // if (success == 1){
    document.getElementById("signup_button").style.visibility = "";
    //document.getElementById('signup_button').style.display = 'block';
    //document.getElementById("signup_button").style.visibility = 'inherit';
    //document.getElementById("signup_button").style.visibility="visible";
    //document.getElementById("signup_button").style.visibility='inline';
   // }
}
 
var credential = firebase.auth.PhoneAuthProvider.credential(confirmationResult.verificationId, code);
//console.log(credential);
firebase.auth().signInWithCredential(credential);





