import axios from "axios";
const sayHello = name => `Hello, ${testVariable}!`;
let testVariable = 0
const baseUrl = "localhost:8000/"
const serverUrl = `http://${baseUrl}`
const sockerBaseUrl = `ws://${baseUrl}`

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
        const socket = new WebSocket(sockerBaseUrl);
        socket.no
    } catch (error) {

    }
}

// Exporting the function
export { sayHello, getAccessToken };