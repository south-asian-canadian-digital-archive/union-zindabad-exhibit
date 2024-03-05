import { writable } from "svelte/store";


export const pageIdx = writable(0);
export const direction = writable<1 | -1>(1);