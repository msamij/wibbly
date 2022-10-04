import { toggleAuthForm } from '@eventFunctions/helpers/toggleAuthForm';

export function removeOverlay() {
  toggleAuthForm(false);
}
