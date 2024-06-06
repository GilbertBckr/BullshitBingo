<script setup>
import { styles as typescaleStyles } from "@material/web/typography/md-typescale-styles.js";
import PageTitle from "./components/PageTitle.vue";

// Apply material typescale style classes
document.adoptedStyleSheets.push(typescaleStyles.styleSheet);
</script>
<script>
export default {
    data() {
        return {
            title: "Bullshit Bingo",
        };
    },
    methods: {
        updateTitle(title) {
            console.log("New Title: " + title);
            this.title = title;
        },
    },
};
</script>

<template>
    <header>
        <PageTitle>{{ title }}</PageTitle>
    </header>
    <main>
        <RouterView @updateTitle="updateTitle" />
    </main>
    <footer>
        <p class="md-typescale-body-small">
            <a href="#" @click="console.log('Open how to play')">How to play</a> · <a href="#" @click="console.log('Open imprint')">Imprint</a>
        </p>
    </footer>
</template>
<style scoped>
main {
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 18px;
    flex-grow: 1;
    height: 100%;
    margin: 12px;
    margin-top: 0;
}

main > *:first-child {
    flex-grow: 1;
}

main > * {
    border-radius: 28px;
    background-color: var(--md-sys-color-surface-container);
    position: relative;
    display: flex;
    flex-direction: column;
}

footer > p {
    margin-top: 0;
    text-align: center;
}

a {
    color: var(--md-sys-color-primary);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
    color: var(--md-sys-color-on-primary-container)
}
</style>
