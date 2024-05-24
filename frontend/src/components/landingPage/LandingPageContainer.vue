<script setup>
import GameCardContainer from './GameCardContainer.vue';
import GameCard from './GameCard.vue';
</script>

<script>
export default {
}
</script>
<template>
    <div class="wrapper">
        <h2 class="md-typescale-headline-large">Active Games</h2>
        <div class="container">
            <GameCardContainer>
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
            </GameCardContainer>
        </div>
    </div>
</template>
<style scoped>
h2 {
    margin: 0;
    padding: 30px;
}

.wrapper {
    border-radius: 28px;
    background-color: var(--md-sys-color-surface-container);
    position: relative;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.container {
    position: relative;
    flex-grow: 1;
}
</style>