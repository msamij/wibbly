import { DOMInputElements } from '@domElements/domElements';

/**
 * @param toggle if true it'll render fields for user signup false for user login.
 */
export function toggleInputFields(toggle: boolean) {
  const creditCardField: HTMLInputElement = DOMInputElements.getCreditCardField();
  const confirmPasswordField: HTMLInputElement = DOMInputElements.getConfirmPasswordField();

  [creditCardField, confirmPasswordField].forEach(el => {
    if (toggle) el.style.display = 'block';
    else el.style.display = 'none';
  });
}
