import { Component } from '@decorators/component';
import { Event } from '@decorators/events';
import { DOMElements } from '@domElements/domElements';
import { submitForm } from '@eventFunctions/formSubmit';

@Component
export class Form {
  @Event('submit', submitForm)
  getForm(): HTMLDivElement {
    return DOMElements.getForm();
  }
}
