export function authMenu(event: Event) {
  const form: HTMLDivElement = document.querySelector('.form');
  const overlay: HTMLDivElement = document.querySelector('.overlay');
  const confirmPasswordField: HTMLInputElement = document.querySelector('.input__confirm-password');
  const creditCardField: HTMLInputElement = document.querySelector('.input__credit-card-no');

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
