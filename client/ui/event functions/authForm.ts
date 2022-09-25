import { DOMElements, DOMInputElements } from '@domElements/domElements';

export function renderAuthForm(event: Event) {
  const form: HTMLDivElement = DOMElements.getForm();
  const overlay: HTMLDivElement = DOMElements.getOverlay();
  const confirmPasswordField: HTMLInputElement = DOMInputElements.getConfirmPasswordField();
  const creditCardField: HTMLInputElement = DOMInputElements.getCreditCardField();

  if ((event.target as HTMLButtonElement).closest('.btn-login')) {
    confirmPasswordField.style.display = 'none';
    creditCardField.style.display = 'none';
  } else if ((event.target as HTMLButtonElement).closest('.btn-signup')) {
    confirmPasswordField.style.display = 'block';
    creditCardField.style.display = 'block';
  }

  [form, overlay].forEach(el => {
    el.style.visibility = 'visible';
    el.style.opacity = '1';
  });
}
