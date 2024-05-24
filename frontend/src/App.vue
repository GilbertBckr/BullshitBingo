<script setup>
import { styles as typescaleStyles } from '@material/web/typography/md-typescale-styles.js';
import PageTitle from './components/PageTitle.vue';
import LandingPageContainer from './components/landingPage/LandingPageContainer.vue';

// Apply material typescale style classes
document.adoptedStyleSheets.push(typescaleStyles.styleSheet);
</script>

<template>
  <header>
    <PageTitle>Bullshit Bingo</PageTitle>
  </header>
  <main>
    <LandingPageContainer>
      
    </LandingPageContainer>
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

main>*:first-child {
  flex-grow: 1;
}
</style>
