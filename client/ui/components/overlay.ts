import { Component } from '@decorators/component';
import { Event } from '@decorators/events';
import { DOMElements } from '@domElements/domElements';
import { removeOverlay } from '@eventFunctions/renderOverlay';

@Component
export class Overlay {
  @Event('click', removeOverlay)
  getOverlay(): HTMLDivElement {
    return DOMElements.getOverlay();
  }
}
