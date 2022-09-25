import { DOMElements } from '@domElements/domElements';
import { component, event } from '@eventDecorators/events';
import { submitForm } from '@eventFunctions/formSubmit';

@component
export class FormComponent {
  @event('submit', submitForm)
  getForm(): HTMLDivElement {
    return DOMElements.getForm();
  }
}
