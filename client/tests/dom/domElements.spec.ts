import { DOMButtonElements, DOMElements, DOMInputElements } from '../../core/dom/domElements';

describe('DOMElements Class Test', () => {
  test('DOMElements Class should have these methods', () => {
    expect(DOMElements.getForm).toBeInstanceOf(Function);
    expect(DOMElements.getOverlay).toBeInstanceOf(Function);
    expect(DOMElements.getProfileMenu).toBeInstanceOf(Function);
  });
});

describe('DOMButtonElements Class Test', () => {
  test('DOMButtonElements Class should have these methods', () => {
    expect(DOMButtonElements.getLoginButton).toBeInstanceOf(Function);
    expect(DOMButtonElements.getSignupButton).toBeInstanceOf(Function);
    expect(DOMButtonElements.getLogoutButton).toBeInstanceOf(Function);
  });
});

describe('DOMInputElements Class Test', () => {
  test('DOMInputElements Class should have these methods', () => {
    expect(DOMInputElements.getUsernameField).toBeInstanceOf(Function);
    expect(DOMInputElements.getPasswordField).toBeInstanceOf(Function);
    expect(DOMInputElements.getConfirmPasswordField).toBeInstanceOf(Function);
    expect(DOMInputElements.getCreditCardField).toBeInstanceOf(Function);
  });
});
