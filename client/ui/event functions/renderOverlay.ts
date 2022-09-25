import { DOMElements } from '@domElements/domElements';

export function renderOverlay() {
  const form: HTMLDivElement = DOMElements.getForm();
  const overlay: HTMLDivElement = DOMElements.getOverlay();
  [form, overlay].forEach(el => {
    el.style.visibility = 'hidden';
    el.style.opacity = '0';
  });
}
