
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
              // SMS sent. Prompt user to type the code from the message, then sign the
              // user in with confirmationResult.confirm(code).
              window.confirmationResult = confirmationResult;
              console.log(confirmationResult);
              // ...
            })
            .catch((error) => {
              console.log(error);
              // Error; SMS not sent
              // ...
            });
        });

document
        .getElementById("confirmcode_button")
        .addEventListener("click", (event) => {
          event.preventDefault();
          const code = document.getElementById("confirmcode").value;
          confirmationResult
            .confirm(code)
            .then((result) => {
              // User signed in successfully.
              const user = result.user;
              console.log(result);
              // ...
            })
            .catch((error) => {
              console.log(error);
              // User couldn't sign in (bad verification code?)
              // ...
            });
        });











