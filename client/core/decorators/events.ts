import 'reflect-metadata';

export function Event(eventType: string, listener: Function): (target: any, key: string) => void {
  return function (target: any, key: string): void {
    Reflect.defineMetadata('eventType', eventType, target, key);
    Reflect.defineMetadata('listener', listener, target, key);
  };
}
