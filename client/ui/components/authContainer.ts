import { component, event } from '@eventDecorators/events';
import { renderAuthForm } from '@eventFunctions/authForm';

@component
export class AuthContainer {
  @event('click', renderAuthForm)
  getAuthContainer(): HTMLDivElement {
    return document.querySelector('.header__profile-menu');
  }
}
