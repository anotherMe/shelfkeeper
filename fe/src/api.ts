// src/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

export interface Asset {
  id: number;
  name: string;
  main_image_url: string;
  description?: string;
  images?: { id: number; url: string }[];
}

export const fetchAssets = async (): Promise<Asset[]> => {
  const response = await api.get<Asset[]>('/assets');
  return response.data;
};

export const fetchAssetById = async (id: number): Promise<Asset> => {
  const response = await api.get<Asset>(`/assets/${id}`);
  return response.data;
};
