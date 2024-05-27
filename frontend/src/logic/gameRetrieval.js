import axios from "axios";

const baseUrl = "localhost:8000/";
const serverUrl = `http://${baseUrl}`;

const getAvailableGames = async () => {
    try {
        let result = await axios.get(serverUrl + "active-games");
        return result.data;
    } catch (error) {
        console.log(error);
    }
};

export { getAvailableGames };
