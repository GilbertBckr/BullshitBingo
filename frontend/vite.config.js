import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue({
            template: {
                compilerOptions: {
                    isCustomElement: (tag) =>
                        [
                            "md-elevation",
                            "md-filled-button",
                            "md-dialog",
                            "md-text-button",
                            "md-outlined-button",
                            "md-outlined-text-field",
                            "md-switch",
                            "md-icon",
                            "md-divider",
                            "md-list-item",
                            "md-outlined-icon-button",
                            "md-list",
                            "md-filled-tonal-button",
                            "md-ripple",
                            "md-filled-icon-button",
                        ].includes(tag),
                },
            },
        }),
    ],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
});
