import { browser } from '$app/environment';
import { goto } from '$app/navigation';
import { BACKEND_URL, SSO_FRONTEND_URL } from './consts';
import { writable } from 'svelte/store';
import { get } from 'svelte/store';
// export auth store:

class AuthService {
    is_logged_in = writable(browser ? localStorage.getItem('token') !== null : true);
    // /**
    //  * 
    //  * @param {string} username
    //  * @param {string} password 
    //  * @returns {Promise<boolean>}
    //  */
    // async login(username, password) {
    //     const url = `${BACKEND_URL}/api-token-auth/`
    //     const response = await fetch(url, {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify({ username, password })
    //     });
    //     if (response.status === 200)
    //     {
    //         const data = await response.json();
    //         if (browser)
    //         {
    //             localStorage.setItem('token', data.token);
    //         }
    //         this.is_logged_in.set(true);
    //         return true;
    //     } else
    //     {
    //         return false;
    //     }
    // }

    logout() {
        if (browser)
        {
            this.is_logged_in.set(false);
            localStorage.removeItem('token');
        }
    }

    // isLoggedIn() {
    //     if (browser)
    //     {
    //         this.is_logged_in.set(localStorage.getItem('token') !== null);
    //         return localStorage.getItem('token') !== null;
    //     }
    // }

    getToken() {
        if (browser)
        {
            let token = JSON.parse(localStorage.getItem('token'));
            return token?.token || undefined;
        }
    }

    try_login_from_page_auth() {
        debugger;
        if (browser)
        {
            const token_b64Safe = new URLSearchParams(window.location.search).get('auth_token');
            if (token_b64Safe !== null)
            {
                // encode token
                // let auth_b64 = window.btoa(JSON.stringify($auth_token));
                // let auth_b64Safe = encodeURIComponent(auth_b64);
                // let url = `${data.url}/display/?screen_id=${screen_id}&auth_token=${auth_b64Safe}`;
                // decode token
                const token = JSON.parse(window.atob(decodeURIComponent(token_b64Safe)));

                localStorage.setItem('token', JSON.stringify(token));
                this.is_logged_in.set(true);

                // remove token from url
                let url = window.location.href;
                let new_url = new URL(url);
                new_url.searchParams.delete('auth_token');
                window.history.replaceState({}, document.title, new_url);
                return true;
            }
            return false;
        }
    }

    /**
     * 
     * @param {string|undefined} url 
     */
    protected_route(url = undefined) {
        if (browser && !get(this.is_logged_in))
        {
            if (this.try_login_from_page_auth())
            {
                return;
            }

            if (url === undefined)
            {
                url = window.location;
            }
            window.location = SSO_FRONTEND_URL + '/login?next=' + url;
        }
    }
}

const authService = new AuthService();
export default authService;

export const isLoggedIn = authService.is_logged_in;

