import { Urls } from '@networking/urls';
import { state } from '@state/state';

export function getAuthUrl(): string {
  const url = `${Urls.baseUrl}${Urls.authUrl}`;
  if (state.authButton === 'login') return `${url}${Urls.loginUrl}`;
  else if (state.authButton === 'signup') return `${url}${Urls.signupUrl}`;
}
