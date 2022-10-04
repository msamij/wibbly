import { DOMInputElements } from '@domElements/domElements';
import { state } from '@state/state';
import { RequestBody } from '@ui/requestBody';

export function getAuthFormData(): RequestBody {
  const username: string = DOMInputElements.getUsernameField().value;
  const password1: string = DOMInputElements.getPasswordField().value;
  const password2: string = DOMInputElements.getConfirmPasswordField().value;
  const credit_card_no: number = +DOMInputElements.getCreditCardField().value;

  if (state.authButton === 'login') return { username, password1 };
  else if ((state.authButton = 'signup')) return { username, password1, password2, credit_card_no };
}
