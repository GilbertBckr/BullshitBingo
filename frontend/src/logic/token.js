import axios from "axios";
const sayHello = name => `Hello, ${testVariable}!`;
let testVariable = 0
const baseUrl = "localhost:8000/"
const serverUrl = `http://${baseUrl}`
const socketBaseUrl = `ws://${baseUrl}`

const mutater = () => {
    testVariable++;
}

window.data = {}

const getAccessToken = async () => {
    try {
        let result = await axios.post(serverUrl + "token")
        return result.data.access_token;
    } catch (error) {

    }
}

const createGame = async (username, theme) => {
    try {
        const token = await getAccessToken()
        const socket = new WebSocket(socketBaseUrl + "create-game/" + username,);
        socket.onopen = (event) => {
            socket.send(token);
            socket.send(JSON.stringify({ theme: theme }));
        }
        socket.onerror = (error) => {
            console.log("Error creating game:")
            console.log(error)
        }
        return socket
    } catch (error) {

    }
}

const joinGame = async (gameId, username, callbackAfterConnect) => {
    const token = await getAccessToken()
    const socket = new WebSocket(`${socketBaseUrl}join-game/${gameId}/${username}`)
    socket.onopen = () => {
        socket.send(token);
        saveWebsocket(socket, gameId)
        callbackAfterConnect()
    }
}

const saveWebsocket = (socket, gameId) => {
    window.data[gameId] = socket
}

// Exporting the function
export { sayHello, getAccessToken, createGame, joinGame, saveWebsocket };