import { DOMButtonElements } from '@domElements/domElements';

export function renderLogoutButton() {
  const btnLogout: HTMLButtonElement = DOMButtonElements.getLogoutButton();
  const btnLogin: HTMLButtonElement = DOMButtonElements.getLoginButton();
  const btnSignup: HTMLButtonElement = DOMButtonElements.getSignupButton();
  [btnLogin, btnSignup].forEach(el => {
    el.style.display = 'none';
  });
  btnLogout.style.display = 'block';
}
