import { Component } from '@decorators/component';
import { DOMElements } from '@domElements/domElements';
import { renderOverlay } from '@eventFunctions/renderOverlay';
import { Event } from '@decorators/events';

@Component
export class Overlay {
  @Event('click', renderOverlay)
  getOverlay(): HTMLDivElement {
    return DOMElements.getOverlay();
  }
}
