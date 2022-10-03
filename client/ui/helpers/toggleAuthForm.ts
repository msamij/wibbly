import { DOMElements } from '@domElements/domElements';

/**
 * @param toggle if true it'll render authentication form, else remove it from dom
 */
export function toggleAuthForm(toggle: boolean) {
  let opacity = '0';
  let visibility = 'hidden';
  const form: HTMLDivElement = DOMElements.getForm();
  const overlay: HTMLDivElement = DOMElements.getOverlay();

  [form, overlay].forEach(el => {
    if (toggle) {
      visibility = 'visible';
      opacity = '1';
    }
    el.style.visibility = visibility;
    el.style.opacity = opacity;
  });
}
