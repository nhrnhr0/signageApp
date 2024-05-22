
import authService from './auth';


/**
 * 
 * @param {string} url 
 * @param {RequestInit} options
 * @returns 
 */
export async function my_fetch(url, options = undefined) {
    const token = authService.getToken();
    if (token)
    {
        if (!options)
        {
            options = {};
        }
        if (!options.headers)
        {
            options.headers = {};
        }
        options.headers["Authorization"] = `Bearer ${token}`;
    }
    let ret = await fetch(url, options);
    return ret;
}

