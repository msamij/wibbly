import { DOMButtonElements } from '@domElements/domElements';

/**
 * @param toggle if true, it'll render logout button and remove signup and login buttons, does opposite on false.
 */
export function toggleLogoutButton(toggle: boolean) {
  const btnLogout: HTMLButtonElement = DOMButtonElements.getLogoutButton();
  const btnLogin: HTMLButtonElement = DOMButtonElements.getLoginButton();
  const btnSignup: HTMLButtonElement = DOMButtonElements.getSignupButton();

  if (toggle) btnLogout.style.display = 'block';
  else btnLogout.style.display = 'none';

  [btnLogin, btnSignup].forEach(el => {
    if (toggle) el.style.display = 'none';
    else el.style.display = 'block';
  });
}
