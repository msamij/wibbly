/**
 * @jest-environment jsdom
 */

import { Component } from '../../core/decorators/component';
import { AuthContainer } from '../../ui/components/authContainer';
import { Form } from '../../ui/components/form';
import { Overlay } from '../../ui/components/overlay';

describe('Component decorator test', () => {
  let componentDecorator: jest.Mock<void, [target: Function]> = null;

  beforeAll(() => {
    componentDecorator = jest.fn(Component);
  });

  test('Component decorator gets called for form component', () => {
    componentDecorator(Form);
    expect(componentDecorator.mock.calls.length).toBe(1);
  });

  test('Component decorator gets called for AuthContainer component', () => {
    componentDecorator(AuthContainer);
    expect(componentDecorator.mock.calls.length).toBe(1);
  });

  test('Component decorator gets called for Overlay component', () => {
    componentDecorator(Overlay);
    expect(componentDecorator.mock.calls.length).toBe(1);
  });
});
