import { component, event } from '../../core/decorators/events/events';
import { submitForm } from '../event functions/formSubmit';
import { DOMElements } from '../../core/dom/domElements';

@component
export class FormComponent {
  @event('submit', submitForm)
  getForm(): HTMLDivElement {
    return DOMElements.getForm();
  }
}
