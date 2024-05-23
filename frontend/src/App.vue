<script setup>
import { styles as typescaleStyles } from '@material/web/typography/md-typescale-styles.js';
import PageTitle from './components/PageTitle.vue';
import Container from './components/Container.vue';

// Apply material typescale style classes
document.adoptedStyleSheets.push(typescaleStyles.styleSheet);
</script>

<template>
  <header>
    <PageTitle>Bullshit Bingo</PageTitle>
  </header>
  <main>
    <Container title="Active Games"></Container>
  </main>
</template>

<style scoped></style>
