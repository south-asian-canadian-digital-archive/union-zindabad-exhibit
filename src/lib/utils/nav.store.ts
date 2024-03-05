import { writable } from "svelte/store";


export const direction = writable<1 | -1>(1);