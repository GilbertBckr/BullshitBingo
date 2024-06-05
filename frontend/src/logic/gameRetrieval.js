import axios from "axios";

const baseUrl = "localhost:8000/";
const serverUrl = `http://${baseUrl}`;

const getAvailableGames = async () => {
    let result = await axios.get(serverUrl + "active-games");
    return result.data;
};

export { getAvailableGames };
