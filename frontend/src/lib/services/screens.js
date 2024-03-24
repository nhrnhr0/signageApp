import { my_fetch } from "../network";
import { BACKEND_URL } from "../consts";

class ScreensService {
    constructor() {
        this.baseUrl = BACKEND_URL + "/screens/";
    }

    async getScreens() {
        const response = await my_fetch(this.baseUrl);
        return response.json();
    }

    /**
     * 
     * @param {string|number} screenId 
     * @returns 
     */
    async deleteScreen(screenId) {
        const response = await my_fetch(`${this.baseUrl}/${screenId}`, {
            method: "DELETE",
        });
        return response.json();
    }
    /**
     * 
     * @param {string} uuid 
     * @returns {Promise<Screen>}
     */
    async getScreen(uuid) {
        const response = await my_fetch(`${this.baseUrl}${uuid}`);
        let ret = await response.json();
        return ret;
    }

    /**
     * Removes an asset from a screen.
     *
     * @param {string} screenId - The ID of the screen.
     * @param {string} assetId - The ID of the asset to be removed.
     * @returns {Promise<Object>} - A promise that resolves to the JSON response from the server.
     */
    async removeAssetFromScreen(screenId, assetId) {
        const response = await my_fetch(`${this.baseUrl}${screenId}/assets/${assetId}`, {
            method: "DELETE",
        });
        return response.json();
    }

    /**
     * Uploads assets to a screen.
     * 
     * @param {string} screenId - The ID of the screen.
     * @param {File} file - The files to be uploaded.
     * @param {string} duration - The duration of the asset.
     * @param {string} type - The type of the asset.
     * @returns {Promise<Object>} - A promise that resolves to the JSON response from the server.
     */
    async uploadAsset(screenId, file, duration, type) {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("duration", duration);
        formData.append("type", type);
        const response = await my_fetch(`${this.baseUrl}${screenId}/upload-asset/`, {
            method: "POST",
            body: formData,
        });
        return response.json();
    }

    async getAllScreensAndIslands() {
        const response = await my_fetch(BACKEND_URL + "/screens-islands/");
        return response.json();
    }

    async getScrenDisplayByCode(code) {
        const response = await my_fetch(`${this.baseUrl}display/${code}/`);
        return response.json();
    }

    async updateScreen(screen) {
        const response = await my_fetch(`${this.baseUrl}${screen.uuid}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(screen),
        });
        return response.json();
    }
}

export default new ScreensService();
