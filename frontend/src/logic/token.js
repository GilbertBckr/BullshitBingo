import axios from "axios";
let testVariable = 0;
const baseUrl = "localhost:8000/";
const serverUrl = `http://${baseUrl}`;
const socketBaseUrl = `ws://${baseUrl}`;

window.data = {};
window.userIds = {};

const getAccessToken = async () => {
    try {
        let result = await axios.post(serverUrl + "token");
        return result.data;
    } catch (error) {}
};

const createGame = async (username, theme, isPrivate) => {
    try {
        const credentials = await getAccessToken();
        const socket = new WebSocket(socketBaseUrl + "create-game/" + username);
        socket.onopen = (event) => {
            console.log(credentials);
            socket.send(credentials.access_token);
            console.log("Send token: " + credentials.access_token);
            socket.send(JSON.stringify({ theme: theme, private: isPrivate }));
        };
        socket.onerror = (error) => {
            console.log("Error creating game:");
            console.log(error);
        };
        return [socket, credentials.user_id];
    } catch (error) {}
};

const joinGame = async (gameId, username) => {
    return new Promise((resolve) => {
        getAccessToken().then((credentials) => {
            const socket = new WebSocket(
                `${socketBaseUrl}join-game/${gameId}/${username}`,
            );
            socket.onopen = () => {
                socket.send(credentials.access_token);
                saveGameData(socket, gameId, credentials.user_id);
                resolve();
            };
        });
    });
};

const saveGameData = (socket, gameId, user_id) => {
    window.data[gameId] = socket;
    window.userIds[gameId] = user_id;
};

// Exporting the function
export { createGame, joinGame, saveGameData };
