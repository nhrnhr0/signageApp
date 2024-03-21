
import { BACKEND_URL } from './consts.js';
import authService from './auth';

/**
 * 
 * @param {string} url 
 * @param {RequestInit} options
 * @returns 
 */
async function my_fetch(url, options = undefined) {
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
        options.headers["Authorization"] = `Token ${token}`;
    }
    let ret = await fetch(url, options);
    return ret;
}

class PlaylistsService {
    constructor() {
        this.baseUrl = BACKEND_URL + "/playlists/";
    }

    async getPlaylists() {
        debugger;
        const response = await my_fetch(this.baseUrl);
        return response.json();
    }

    /**
     * 
     * @param {string|number} playlistId 
     * @returns 
     */
    async deletePlaylist(playlistId) {
        const response = await my_fetch(`${this.baseUrl}/${playlistId}`, {
            method: "DELETE",
        });
        return response.json();
    }
    /**
     * 
     * @param {string} uuid 
     * @returns {Promise<Playlist>}
     */
    async getPlaylist(uuid) {
        const response = await my_fetch(`${this.baseUrl}${uuid}`);
        let ret = await response.json();
        return ret;
    }

    /**
     * Removes an asset from a playlist.
     *
     * @param {string} playlistId - The ID of the playlist.
     * @param {string} assetId - The ID of the asset to be removed.
     * @returns {Promise<Object>} - A promise that resolves to the JSON response from the server.
     */
    async removeAssetFromPlaylist(playlistId, assetId) {
        const response = await my_fetch(`${this.baseUrl}${playlistId}/assets/${assetId}`, {
            method: "DELETE",
        });
        return response.json();
    }

    /**
     * Uploads assets to a playlist.
     * 
     * @param {string} playlistId - The ID of the playlist.
     * @param {File} file - The files to be uploaded.
     * @param {string} duration - The duration of the asset.
     * @param {string} type - The type of the asset.
     * @returns {Promise<Object>} - A promise that resolves to the JSON response from the server.
     */
    async uploadAsset(playlistId, file, duration, type) {
        debugger;
        const formData = new FormData();
        formData.append("file", file);
        formData.append("duration", duration);
        formData.append("type", type);
        const response = await my_fetch(`${this.baseUrl}${playlistId}/upload-asset/`, {
            method: "POST",
            body: formData,
        });
        return response.json();
    }
}

export default new PlaylistsService();
