import { event, component } from '../../core/decorators/events/events';

@component
export class Overlay {
  @event('click', overlayMenu)
  getOverlay(): HTMLDivElement {
    return document.querySelector('.overlay');
  }
}

function overlayMenu() {
  const form: HTMLDivElement = document.querySelector('.form');
  const overlay: HTMLDivElement = document.querySelector('.overlay');
  form.style.opacity = '0';
  form.style.visibility = 'hidden';
  overlay.style.visibility = 'hidden';
  overlay.style.opacity = '0';
}
