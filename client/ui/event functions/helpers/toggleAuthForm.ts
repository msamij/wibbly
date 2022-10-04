import { DOMElements } from '@domElements/domElements';

/**
 * @param toggle if true it'll render authentication form, else remove it from dom
 */
export function toggleAuthForm(toggle: boolean) {
  let opacity = '0';
  let visibility = 'hidden';
  const form: HTMLDivElement = DOMElements.getForm();
  const overlay: HTMLDivElement = DOMElements.getOverlay();

  if (toggle) {
    opacity = '1';
    visibility = 'visible';
  }
  [form, overlay].forEach(el => {
    el.style.visibility = visibility;
    el.style.opacity = opacity;
  });
}
