import { component, event } from '../../core/decorators/events/events';
import { submitForm } from '../event functions/formSubmit';

@component
export class FormComponent {
  @event('submit', submitForm)
  getForm(): HTMLDivElement {
    return document.querySelector('.form');
  }
}
