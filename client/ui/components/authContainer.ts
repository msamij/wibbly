import { event, component } from '../../core/decorators/events/events';

@component
export class AuthContainer {
  @event('click', authMenu)
  getAuthContainer(): HTMLDivElement {
    return document.querySelector('.header__profile-menu');
  }
}

function authMenu(event: Event) {
  const form: HTMLDivElement = document.querySelector('.form');
  const overlay: HTMLDivElement = document.querySelector('.overlay');
  if (
    (event.target as HTMLButtonElement).closest('.btn-signup') ||
    (event.target as HTMLButtonElement).closest('.btn-login')
  ) {
    form.style.opacity = '1';
    form.style.visibility = 'visible';
    overlay.style.visibility = 'visible';
    overlay.style.opacity = '1';
  }
}
