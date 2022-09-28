import { Component } from '@decorators/component';
import { renderAuthForm } from '@eventFunctions/authForm';
import { Event } from 'core/decorators/events';

@Component
export class AuthContainer {
  @Event('click', renderAuthForm)
  getAuthContainer(): HTMLDivElement {
    return document.querySelector('.header__profile-menu');
  }
}
