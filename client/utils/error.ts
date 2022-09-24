export function renderError(message: string) {
  const messageElement: HTMLDivElement = document.querySelector('.message');
  messageElement.style.visibility = 'visible';
  messageElement.style.opacity = '1';
  messageElement.textContent = message;
  setTimeout(function () {
    messageElement.style.visibility = 'hidden';
    messageElement.style.opacity = '0';
  }, 5000);
}
