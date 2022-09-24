export function renderOverlay() {
  const form: HTMLDivElement = document.querySelector('.form');
  const overlay: HTMLDivElement = document.querySelector('.overlay');
  [form, overlay].forEach(el => {
    el.style.visibility = 'hidden';
    el.style.opacity = '0';
  });
}
