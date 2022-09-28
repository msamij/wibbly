import { FormComponent } from '../../ui/components/form';

describe('Form class test', () => {
  test('It should have a method called getForm', () => {
    expect(new FormComponent().getForm).toBeInstanceOf(Function);
  });
});
