


// { "id": 27, "name": "ראשי", "playlists": [{ "uuid": "08c40774-3af8-46ad-a1f6-c751bd4a3831", "name": "מפרסם: קובי", "assets": [{ "id": 41, "name": "מתוקן_קובי.jpg", "media": "/media/assets/%D7%9E%D7%AA%D7%95%D7%A7%D7%9F_%D7%A7%D7%95%D7%91%D7%99.jpg", "type": "image", "duration": 10 }] }, { "uuid": "2df551db-bdf1-4adc-9375-8bd9f8ed164d", "name": "מפרסם: נינג'ה", "assets": [{ "id": 40, "name": "ninja.jpg", "media": "/media/assets/ninja.jpg", "type": "image", "duration": 10 }] }, { "uuid": "ef0bd71e-7965-4bc6-a35b-41fcbbe7f34c", "name": "מסך ראשי גנרי לכולם", "assets": [{ "id": 33, "name": "11מתוקן1.jpg", "media": "/media/assets/11%D7%9E%D7%AA%D7%95%D7%A7%D7%9F1.jpg", "type": "image", "duration": 5 }, { "id": 34, "name": "Artboaמתוקןrd_1_copy_4_1.jpg", "media": "/media/assets/Artboa%D7%9E%D7%AA%D7%95%D7%A7%D7%9Frd_1_copy_4_1.jpg", "type": "image", "duration": 5 }, { "id": 35, "name": "Artboמתוקןard_1_copy_6_1.jpg", "media": "/media/assets/Artbo%D7%9E%D7%AA%D7%95%D7%A7%D7%9Fard_1_copy_6_1.jpg", "type": "image", "duration": 5 }, { "id": 36, "name": "genericמתוקן_toilet_new.jpg", "media": "/media/assets/generic%D7%9E%D7%AA%D7%95%D7%A7%D7%9F_toilet_new.jpg", "type": "image", "duration": 10 }, { "id": 37, "name": "WhatsApp_Image_מתוקן2023-08-10_at_12.22.48_1 (1).jpg", "media": "/media/assets/WhatsApp_Image_%D7%9E%D7%AA%D7%95%D7%A7%D7%9F2023-08-10_at_12.22.48_1_1.jpg", "type": "image", "duration": 5 }, { "id": 38, "name": "כללית_1מתוקן.jpg", "media": "/media/assets/%D7%9B%D7%9C%D7%9C%D7%99%D7%AA_1%D7%9E%D7%AA%D7%95%D7%A7%D7%9F.jpg", "type": "image", "duration": 5 }, { "id": 39, "name": "מתוקן_1.jpg", "media": "/media/assets/%D7%9E%D7%AA%D7%95%D7%A7%D7%9F_1.jpg", "type": "image", "duration": 5 }] }] }
// export Island as the above type to be used as `@type {import('$lib/types').Island}`

export interface screen {
    name: string;
    uuid: string;
    is_active: boolean;
    layout: string;
    islands: Island[];
}
export interface Island {
    id: number;
    name: string;
    playlists: Playlist[];
}


export interface Asset {
    id: number;
    name: string;
    media: string;
    type: string;
    duration: number;
}



export interface Playlist {
    uuid: string;
    name: string;
    assets_count: number;
    is_active: boolean;
    created_at: string;
    updated_at: string;
    schedule: {
        type: string;
        data: any; // You can specify a more specific type if known
    };
}

export interface TableHeader {
    label: string;
    url_key: string;
    orderable: boolean;
    display: string | ((handler: TableHandlerFunction) => string);
}

type TableHandlerFunction = (playlist: Playlist, header: TableHeader) => any; // You can specify a more specific return type if known
