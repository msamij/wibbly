import 'reflect-metadata';

export function component(target: Function) {
  for (let key of Object.getOwnPropertyNames(target.prototype)) {
    const eventType = Reflect.getMetadata('eventType', target.prototype, key);
    const listener = Reflect.getMetadata('listener', target.prototype, key);

    if (eventType && listener) {
      const method = target.prototype[key];
      method().addEventListener(eventType, listener);
    }
  }
}

export function event(eventType: string, listener: Function): Function {
  return function (target: any, key: string, desc: PropertyDescriptor) {
    Reflect.defineMetadata('eventType', eventType, target, key);
    Reflect.defineMetadata('listener', listener, target, key);
  };
}
