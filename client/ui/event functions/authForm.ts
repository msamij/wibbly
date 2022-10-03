import { toggleAuthForm } from '@helpers/toggleAuthForm';
import { toggleInputFields } from '@helpers/toggleInputFields';

export function renderAuthForm(event: Event) {
  const eventTarget = event.target as HTMLButtonElement;

  // Only render on signup or login button event.
  if (eventTarget.closest('.btn-login') || eventTarget.closest('.btn-signup')) toggleAuthForm(true);

  if (eventTarget.closest('.btn-login')) {
    toggleInputFields(false);
  } else if (eventTarget.closest('.btn-signup')) {
    toggleInputFields(true);
  }
}
