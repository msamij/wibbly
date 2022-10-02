import 'reflect-metadata';

export function Component(target: Function): void {
  for (let key of Object.getOwnPropertyNames(target.prototype)) {
    const eventType = Reflect.getMetadata('eventType', target.prototype, key);
    const listener = Reflect.getMetadata('listener', target.prototype, key);

    if (eventType && listener) {
      const element: HTMLElement = target.prototype[key]();
      if (element) element.addEventListener(eventType, listener);
    }
  }
}
