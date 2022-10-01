/**
 * @jest-environment jsdom
 */

import { Component } from '../../core/decorators/component';
import { FormComponent } from '../../ui/components/form';

describe('Component decorator test', () => {
  test('Component decorator gets called for form component', () => {
    const componentDecorator = jest.fn(Component);
    componentDecorator(FormComponent);
    expect(componentDecorator.mock.calls.length).toBe(1);
  });
});
