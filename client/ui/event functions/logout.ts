import { toggleLogoutButton } from '@helpers/logoutBtn';
import { HTTP } from '@networking/http';
import { Urls } from '@networking/urls';

export async function logout() {
  const response = await HTTP.post(`${Urls.baseUrl}${Urls.authUrl}${Urls.logoutUrl}`);
  console.log(response.status);
  toggleLogoutButton(false);
}
