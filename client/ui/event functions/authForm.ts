import { toggleAuthForm } from '@eventFunctions/helpers/toggleAuthForm';
import { toggleInputFields } from '@eventFunctions/helpers/toggleInputFields';
import { state } from '@state/state';

export function renderAuthForm(event: Event) {
  const eventTarget = event.target as HTMLButtonElement;
  // Only render on signup or login button event.
  if (eventTarget.closest('.btn-login') || eventTarget.closest('.btn-signup')) toggleAuthForm(true);

  // Will only show username and password fields for login.
  if (eventTarget.closest('.btn-login')) {
    state.authButton = 'login';
    toggleInputFields(false);
  } else if (eventTarget.closest('.btn-signup')) {
    state.authButton = 'signup';
    toggleInputFields(true);
  }
}
