/**
 * @jest-environment jsdom
 */

import { Event } from '../../core/decorators/events';
import { AuthContainer } from '../../ui/components/authContainer';
import { Form } from '../../ui/components/form';
import { Overlay } from '../../ui/components/overlay';
import { renderAuthForm } from '../../ui/event functions/authForm';
import { submitForm } from '../../ui/event functions/formSubmit';
import { renderOverlay } from '../../ui/event functions/renderOverlay';

describe('Event decorator test', () => {
  let eventDecorator = null;
  let innerDecorator = null;

  beforeAll(() => {
    eventDecorator = jest.fn(Event);
    innerDecorator = jest.fn(eventDecorator.mockReturnValue);
  });

  test('Event decorator get called for each component', () => {
    eventDecorator('submit', submitForm);
    eventDecorator('click', renderOverlay);
    eventDecorator('click', renderAuthForm);
    expect(eventDecorator.mock.calls.length).toBe(3);
  });

  test('Event decorator gets called for form component', () => {
    innerDecorator(Form.prototype, 'getForm');
    expect(innerDecorator.mock.calls.length).toBe(1);
  });

  test('Event decorator gets called for AuthContainer component', () => {
    innerDecorator(AuthContainer.prototype, 'getAuthContainer');
    expect(innerDecorator.mock.calls.length).toBe(1);
  });

  test('Component decorator gets called for Overlay component', () => {
    innerDecorator(Overlay.prototype, 'getOverlay');
    expect(innerDecorator.mock.calls.length).toBe(1);
  });
});
