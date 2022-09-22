// const container: HTMLDivElement = document.querySelector('.header__profile-menu');
// const form: HTMLDivElement = document.querySelector('.form');
// const overlay: HTMLDivElement = document.querySelector('.overlay');
// const inputUsername: HTMLInputElement = document.querySelector('.input__username');
// const inputPassword: HTMLInputElement = document.querySelector('.input__password');
// const inputConfirmPassword: HTMLInputElement = document.querySelector('.input__confirm-password');
// const inputCreditCard: HTMLInputElement = document.querySelector('.input__credit-card-no');

// container.addEventListener('click', function (event: Event) {
//   if (
//     (event.target as HTMLButtonElement).closest('.btn-signup') ||
//     (event.target as HTMLButtonElement).closest('.btn-login')
//   ) {
//     form.style.opacity = '1';
//     form.style.visibility = 'visible';
//     overlay.style.visibility = 'visible';
//     overlay.style.opacity = '1';
//   }
// });

// overlay.addEventListener('click', function (event: Event) {
//   form.style.opacity = '0';
//   form.style.visibility = 'hidden';
//   overlay.style.visibility = 'hidden';
//   overlay.style.opacity = '0';
// });

// function csrfToken(name: string): string {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== '') {
//     const cookies = document.cookie.split(';');
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + '=') {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }

// form.addEventListener('submit', function (event: Event) {
//   event.preventDefault();
//   ajaxData();
// });

// async function ajaxData() {
//   const username = inputUsername.value;
//   const password = inputPassword.value;
//   const confirmPassword = inputConfirmPassword.value;
//   const creditCardNo = inputCreditCard.value;

//   fetch('http://127.0.0.1:8000/api/v1/auth/signup', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': csrfToken('csrftoken'),
//     },
//     body: JSON.stringify({
//       username: username,
//       password1: password,
//       password2: confirmPassword,
//       credit_card_no: creditCardNo,
//     }),
//   }).then(res => {
//     res.json().then(r => {
//       console.log(r);
//       changeBtnTypeOnLogin();
//     });
//   });
// }

// function changeBtnTypeOnLogin() {
//   console.log('Hello<<<');
// }
