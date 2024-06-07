import "./assets/main.css";
import "@material/web/button/filled-button.js";
import "@material/web/button/outlined-button.js";
import "@material/web/button/filled-tonal-button.js";
import "@material/web/elevation/elevation.js";
import "@material/web/textfield/outlined-text-field";
import "@material/web/list/list.js";
import "@material/web/list/list-item.js";
import "@material/web/divider/divider.js";
import "@material/web/icon/icon.js";
import "@material/web/iconbutton/outlined-icon-button.js";
import "@material/web/iconbutton/filled-icon-button.js"
import "@material/web/dialog/dialog.js";
import "@material/web/button/text-button.js";
import "@material/web/switch/switch.js";
import "@material/web/ripple/ripple.js"
import { createWebHashHistory, createRouter } from "vue-router";

import { createApp } from "vue";
import App from "./App.vue";
import LandingPageContainer from "./components/landingPage/LandingPageContainer.vue";
import LobbyPageContainer from "./components/lobby/LobbyPageContainer.vue";

const routes = [
    { path: "/", component: LandingPageContainer },
    { path: "/lobby/:game_id", component: LobbyPageContainer },
];
const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

const app = createApp(App);
app.use(router);
app.mount("#app");
