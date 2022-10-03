import { toggleAuthForm } from '@helpers/toggleAuthForm';

export function removeOverlay() {
  toggleAuthForm(false);
}
