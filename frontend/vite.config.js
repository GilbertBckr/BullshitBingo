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
