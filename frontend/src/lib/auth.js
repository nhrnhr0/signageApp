import { browser } from '$app/environment';
import { goto } from '$app/navigation';
import { BACKEND_URL } from './consts';
import { writable } from 'svelte/store';
import { get } from 'svelte/store';
// export auth store:

class AuthService {
    is_logged_in = writable(browser ? localStorage.getItem('token') !== null : true);
    /**
     * 
     * @param {string} username
     * @param {string} password 
     * @returns {Promise<boolean>}
     */
    async login(username, password) {
        const response = await fetch(`${BACKEND_URL}/api-token-auth/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        if (response.status === 200)
        {
            const data = await response.json();
            if (browser)
            {
                localStorage.setItem('token', data.token);
            }
            this.is_logged_in.set(true);
            return true;
        } else
        {
            return false;
        }
    }

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
            return localStorage.getItem('token');
        }
    }

    /**
     * 
     * @param {string|undefined} url 
     */
    protected_route(url = undefined) {

        if (browser && !get(this.is_logged_in))
        {
            if (url === undefined)
            {
                url = window.location.pathname;
            }
            goto('/dashboard/login?next=' + url);
        }
    }
}

const authService = new AuthService();
export default authService;

export const isLoggedIn = authService.is_logged_in;

