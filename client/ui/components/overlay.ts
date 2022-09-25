import { component, event } from '@eventDecorators/events';
import { renderOverlay } from '@eventFunctions/renderOverlay';

@component
export class Overlay {
  @event('click', renderOverlay)
  getOverlay(): HTMLDivElement {
    return document.querySelector('.overlay');
  }
}
