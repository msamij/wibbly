import { toggleLogoutButton } from '@eventFunctions/helpers/logoutBtn';
import { toggleAuthForm } from '@eventFunctions/helpers/toggleAuthForm';
import { getAuthFormData } from '@helpers/authFormData';
import { getAuthUrl } from '@helpers/authUrl';
import { HTTP } from '@networking/http';
import { renderError } from '@utils/error';

export async function submitForm(event: Event) {
  event.preventDefault();

  const response = await HTTP.post(getAuthUrl(), getAuthFormData());

  const resposeJson: string = await response.json();

  // Upon signup, will render logout button and remove signup & login buttons.
  if (response.status == 400) renderError(resposeJson);
  else {
    toggleAuthForm(false);
    toggleLogoutButton(true);
  }
}
