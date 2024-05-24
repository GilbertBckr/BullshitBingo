import axios from "axios";
const sayHello = name => `Hello, ${testVariable}!`;
let testVariable = 0
const baseUrl = "localhost:8000/"
const serverUrl = `http://${baseUrl}`
const socketBaseUrl = `ws://${baseUrl}`

const mutater = () => {
    testVariable++;
}


const getAccessToken = async () => {
    try {
        let result = await axios.post(serverUrl + "token")
        return result.data.access_token;
    } catch (error) {

    }
}

const createGame = async (username) => {
    try {
        const token = await getAccessToken()
        const socket = new WebSocket(socketBaseUrl + "create-game/" + username,);
        socket.onopen = (event) => {
            socket.send(token);
            socket.send(JSON.stringify({ theme: "Test Theme" }));
        }
        socket.onmessage = (event) => {
            console.log(event);
        }
        socket.onerror = (error) => {
            console.log("Error creating game:")
            console.log(error)
        }
    } catch (error) {

    }
}

const joinGame = async (username) => {
    const token = await getAccessToken()
    socket = new WebSocket
}

// Exporting the function
export { sayHello, getAccessToken, createGame, };