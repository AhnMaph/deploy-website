import {Genre} from '../genre/genreDetails';
export interface Manga {
    _id: string;
    title: string;
    author: string;
    description: string;
    cover_image: string;
    blurDataURL?: string;
    created_at: string;
    updated_at: string;
    genres: Genre[];
    source: string;
    numComments: number;
    numViews: number;
    numFavorites: number;
    numChapters: number;
    numLikes: number;
    status: 'completed' | 'ongoing' | 'paused' | 'unverified';
}


