import "./assets/main.css";
import "@material/web/button/filled-button.js";
import "@material/web/button/outlined-button.js";
import "@material/web/elevation/elevation.js";
import "@material/web/textfield/outlined-text-field";
import { createWebHashHistory, createRouter } from 'vue-router'

import { createApp } from "vue";
import App from "./App.vue";
import LandingPageContainer from "./components/landingPage/LandingPageContainer.vue"
import Lobby from "./components/lobby/lobbyPage.vue"

const routes = [
    { path: '/', component: LandingPageContainer},
    { path: '/lobby/:game_id', component: Lobby}
];
const router = createRouter({
    history: createWebHashHistory(),
    routes
});

const app = createApp(App);
app.use(router);
app.mount("#app");
