import "./assets/main.css";
import "@material/web/button/filled-button.js";
import "@material/web/elevation/elevation.js";

import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);
app.mount("#app");
