import { component, event } from '../../core/decorators/events/events';
import { authMenu } from '../event functions/authMenu';

@component
export class AuthContainer {
  @event('click', authMenu)
  getAuthContainer(): HTMLDivElement {
    return document.querySelector('.header__profile-menu');
  }
}
