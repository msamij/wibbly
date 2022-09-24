import { HTTP } from '../../networking/http';
import { renderError } from '../../utils/error';
import { Urls } from '../../networking/urls';
import { DOMButtonElements, DOMInputElements } from '../../core/dom/domElements';

export async function submitForm(event: Event) {
  event.preventDefault();

  const username: HTMLInputElement = DOMInputElements.getUsernameField();
  const password1: HTMLInputElement = DOMInputElements.getPasswordField();
  const password2: HTMLInputElement = DOMInputElements.getConfirmPasswordField();
  const creditCardNo: HTMLInputElement = DOMInputElements.getCreditCardField();

  const response = await HTTP.post(`${Urls.baseUrl}${Urls.authUrl}${Urls.signupUrl}`, {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    credit_card_no: parseInt(creditCardNo.value),
  });

  const resposeJson: string = await response.json();

  if (response.status == 400) renderError(resposeJson);
  else toggleLogoutButton();
}

function toggleLogoutButton() {
  const btnLogout: HTMLButtonElement = DOMButtonElements.getLogoutButton();
  const btnLogin: HTMLButtonElement = DOMButtonElements.getLoginButton();
  const btnSignup: HTMLButtonElement = DOMButtonElements.getSignupButton();
  [btnLogin, btnSignup].forEach(el => {
    el.style.display = 'none';
  });
  btnLogout.style.display = 'block';
}
