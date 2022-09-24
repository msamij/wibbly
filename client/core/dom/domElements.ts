export class DOMElements {
  static getForm(): HTMLDivElement {
    return document.querySelector('.form');
  }

  static getProfileMenu(): HTMLDivElement {
    return document.querySelector('.header__profile-menu');
  }

  static getOverlay(): HTMLDivElement {
    return document.querySelector('.overlay');
  }
}

export class DOMButtonElements {
  static getLoginButton(): HTMLButtonElement {
    return document.querySelector('.btn-login');
  }

  static getSignupButton(): HTMLButtonElement {
    return document.querySelector('.btn-signup');
  }

  static getLogoutButton(): HTMLButtonElement {
    return document.querySelector('.btn-logout');
  }
}

export class DOMInputElements {
  static getUsernameField(): HTMLInputElement {
    return document.querySelector('.input__username');
  }

  static getPasswordField(): HTMLInputElement {
    return document.querySelector('.input__password');
  }

  static getConfirmPasswordField(): HTMLInputElement {
    return document.querySelector('.input__confirm-password');
  }

  static getCreditCardField(): HTMLInputElement {
    return document.querySelector('.input__credit-card-no');
  }
}
