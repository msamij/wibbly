const container: HTMLDivElement = document.querySelector('.header__profile-menu');
const popupMenu: HTMLDivElement = document.querySelector('.popup-signup-menu');
const overlay: HTMLDivElement = document.querySelector('.overlay');

container.addEventListener('click', function (event: Event) {
  if (
    (event.target as HTMLButtonElement).closest('.btn-signup') ||
    (event.target as HTMLButtonElement).closest('.btn-login')
  ) {
    popupMenu.style.opacity = '1';
    popupMenu.style.visibility = 'visible';
    overlay.style.visibility = 'visible';
    overlay.style.opacity = '1';
  }
});

overlay.addEventListener('click', function (event: Event) {
  popupMenu.style.opacity = '0';
  popupMenu.style.visibility = 'hidden';
  overlay.style.visibility = 'hidden';
  overlay.style.opacity = '0';
});
