import { component, event } from '../../core/decorators/events/events';
import { renderOverlay } from '../event functions/renderOverlay';

@component
export class Overlay {
  @event('click', renderOverlay)
  getOverlay(): HTMLDivElement {
    return document.querySelector('.overlay');
  }
}
