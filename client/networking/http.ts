import { csrfToken } from '@utils/token';

interface RequestBody {
  username?: string;
  password1?: string;
  password2?: string;
  credit_card_no?: number;
}

export class HTTP {
  private static async httpFetch(method: 'GET' | 'POST', url: string, body?: RequestBody): Promise<Response> {
    return await fetch(url, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken('csrftoken'),
      },
      body: JSON.stringify(body),
    });
  }

  static async get(url: string): Promise<Response> {
    return await this.httpFetch('GET', url);
  }

  static async post(url: string, body?: RequestBody): Promise<Response> {
    return await this.httpFetch('POST', url, body);
  }
}
