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
            title: 'Bullshit Bingo'
        }
    },
    methods: {
        updateTitle(title) {
            console.log("New Title: " + title)
            this.title = title;
        }
    }
}
</script>

<template>
    <header>
        <PageTitle>{{ title }}</PageTitle>
    </header>
    <main>
        <RouterView @updateTitle="updateTitle"/>
    </main>
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
</style>
