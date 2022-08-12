import axios from "axios"
import {atom, selector} from "recoil"
import {API_BASE_URL} from "../config";


export let itemState = atom({
    key: "item-state",
    default: " ",
})


export const getItems = selector({
    key: 'get-items',
    get: ({get}) => {
        const {getItems}: any = get(itemState)
        if (getItems === null) {
            return null
        }
        return axios.get(
            API_BASE_URL + "/profile"
        );
    }
})