import { Component } from '@decorators/component';
import { DOMElements } from '@domElements/domElements';
import { renderAuthForm } from '@eventFunctions/authForm';
import { Event } from 'core/decorators/events';

@Component
export class AuthContainer {
  @Event('click', renderAuthForm)
  getAuthContainer(): HTMLDivElement {
    return DOMElements.getProfileMenu();
  }
}
