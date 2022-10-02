import { Component } from '@decorators/component';
import { Event } from '@decorators/events';
import { DOMElements } from '@domElements/domElements';
import { renderAuthForm } from '@eventFunctions/authForm';

@Component
export class AuthContainer {
  @Event('click', renderAuthForm)
  getAuthContainer(): HTMLDivElement {
    return DOMElements.getProfileMenu();
  }
}
