<script setup>
import { styles as typescaleStyles } from '@material/web/typography/md-typescale-styles.js';
import PageTitle from './components/PageTitle.vue';
import Container from './components/Container.vue';
import GameCardContainer from './components/landingPage/GameCardContainer.vue'
import GameCard from './components/landingPage/GameCard.vue'

// Apply material typescale style classes
document.adoptedStyleSheets.push(typescaleStyles.styleSheet);
</script>

<template>
  <header>
    <PageTitle>Bullshit Bingo</PageTitle>
  </header>
  <main>
    <Container title="Active Games">
      <GameCardContainer>
        <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
      </GameCardContainer>
    </Container>
  </main>
</template>

<style scoped>
main {
  position: relative;
  display: flex;
  flex-direction: row;
  gap: 18px;
  height: max-content;
  flex-grow: 1;
  margin: 30px;
  margin-top: 0;
}

main>*:first-child {
  flex-grow: 1;
}
</style>
