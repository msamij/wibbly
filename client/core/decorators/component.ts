import 'reflect-metadata';

export function Component(target: Function) {
  for (let key of Object.getOwnPropertyNames(target.prototype)) {
    const eventType = Reflect.getMetadata('eventType', target.prototype, key);
    const listener = Reflect.getMetadata('listener', target.prototype, key);

    if (eventType && listener) {
      const method = target.prototype[key];
      method().addEventListener(eventType, listener);
    }
  }
}
