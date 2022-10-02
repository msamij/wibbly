import { Component } from '@decorators/component';
import { Event } from '@decorators/events';
import { DOMElements } from '@domElements/domElements';
import { renderOverlay } from '@eventFunctions/renderOverlay';

@Component
export class Overlay {
  @Event('click', renderOverlay)
  getOverlay(): HTMLDivElement {
    return DOMElements.getOverlay();
  }
}
