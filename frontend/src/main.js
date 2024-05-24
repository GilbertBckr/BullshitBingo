import "./assets/main.css";
import "@material/web/button/filled-button.js";
import "@material/web/button/outlined-button.js";
import "@material/web/elevation/elevation.js";
import "@material/web/textfield/outlined-text-field";


import { createApp } from "vue";
import App from "./App.vue";


const app = createApp(App);
app.mount("#app");
