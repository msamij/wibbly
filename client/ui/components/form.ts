import { event, component } from '../../core/decorators/events/events';
import { csrfToken } from '../../utils/token';

const inputUsername: HTMLInputElement = document.querySelector('.input__username');
const inputPassword: HTMLInputElement = document.querySelector('.input__password');
const inputConfirmPassword: HTMLInputElement = document.querySelector('.input__confirm-password');
const inputCreditCard: HTMLInputElement = document.querySelector('.input__credit-card-no');

@component
export class FormComponent {
  @event('submit', ajaxData)
  getForm(): HTMLDivElement {
    return document.querySelector('.form');
  }
}

async function ajaxData(event: Event) {
  const username = inputUsername.value;
  const password = inputPassword.value;
  const confirmPassword = inputConfirmPassword.value;
  const creditCardNo = inputCreditCard.value;
  event.preventDefault();

  fetch('http://127.0.0.1:8000/api/v1/auth/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken('csrftoken'),
    },
    body: JSON.stringify({
      username: username,
      password1: password,
      password2: confirmPassword,
      credit_card_no: creditCardNo,
    }),
  }).then(res => {
    res.json().then(r => {
      console.log(r);
      changeBtnTypeOnLogin();
    });
  });
}

function changeBtnTypeOnLogin() {
  console.log('Hello<<<');
}
