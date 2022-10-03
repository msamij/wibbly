import { Component } from '@decorators/component';
import { Event } from '@decorators/events';
import { DOMButtonElements } from '@domElements/domElements';
import { logout } from '@eventFunctions/logout';

@Component
export class LogoutButton {
  @Event('click', logout)
  getLogoutButton(): HTMLButtonElement {
    return DOMButtonElements.getLogoutButton();
  }
}
