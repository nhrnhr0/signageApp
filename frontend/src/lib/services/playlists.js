import { BACKEND_URL } from "../consts.js";
import { my_fetch } from "../network.js";

class PlaylistsService {
    constructor() {
        this.baseUrl = BACKEND_URL + "/playlists/";
    }

    async searchPlaylists(query) {
        const response = await my_fetch(`${this.baseUrl}?search=${query}`);
        return response.json();
    }


    async getPlaylists() {
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
=        const formData = new FormData();
        formData.append("file", file);
        formData.append("duration", duration);
        formData.append("type", type);
        const response = await my_fetch(`${this.baseUrl}${playlistId}/upload-asset/`, {
            method: "POST",
            body: formData,
        });
        return response.json();
    }

    /**
     * Updates a playlist.
     * @param {string} playlistId - The ID of the playlist.
     * @param {Object} data - The data to be updated.
     * @returns {Promise<Object>} - A promise that resolves to the JSON response from the server.
     */
    async updatePlaylist(playlistId, data) {
        const response = await my_fetch(`${this.baseUrl}${playlistId}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        return response.json();
    }

    generateNewPlaylist() {
        return {
            name: "",
            is_active: true,
            assets: [],
        };
    }

    async createPlaylist(data) {
=        let ret = await my_fetch(this.baseUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
        let ret2 = await ret.json();
        return ret2;
    }

    async updateOrCreatePlaylist(playlist) {
=        if (playlist?.uuid)
        {
            return this.updatePlaylist(playlist.uuid, playlist);
        } else
        {
            return this.createPlaylist(playlist);
        }
    }
}

export default new PlaylistsService();
