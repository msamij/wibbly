import { toggleLogoutButton } from '@eventFunctions/helpers/logoutBtn';
import { HTTP } from '@networking/http';
import { Urls } from '@networking/urls';

export async function logout() {
  await HTTP.post(`${Urls.baseUrl}${Urls.authUrl}${Urls.logoutUrl}`);
  toggleLogoutButton(false);
}
