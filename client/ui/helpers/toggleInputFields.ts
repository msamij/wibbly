import { DOMInputElements } from '@domElements/domElements';

export function toggleInputFields(toggle: boolean) {
  const creditCardField: HTMLInputElement = DOMInputElements.getCreditCardField();
  const confirmPasswordField: HTMLInputElement = DOMInputElements.getConfirmPasswordField();

  [creditCardField, confirmPasswordField].forEach(el => {
    if (toggle) el.style.display = 'block';
    else el.style.display = 'none';
  });
}
