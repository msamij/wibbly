import { DOMInputElements } from '@domElements/domElements';
import { toggleLogoutButton } from '@helpers/logoutBtn';
import { HTTP } from '@networking/http';
import { Urls } from '@networking/urls';
import { renderError } from '@utils/error';
import { toggleAuthForm } from '@helpers/toggleAuthForm';

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

  // Upon signup, will render logout button and remove signup & login buttons.
  if (response.status == 400) renderError(resposeJson);
  else {
    toggleAuthForm(false);
    toggleLogoutButton(true);
  }
}
