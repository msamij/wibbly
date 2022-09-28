import 'reflect-metadata';

export function Event(eventType: string, listener: Function): Function {
  return function (target: any, key: string) {
    Reflect.defineMetadata('eventType', eventType, target, key);
    Reflect.defineMetadata('listener', listener, target, key);
  };
}
