<script setup>
import GameCardContainer from './GameCardContainer.vue';
import GameCard from './GameCard.vue';
</script>

<script>
export default {
}
</script>
<template>
    <div>
        <h2 class="md-typescale-headline-large">Active Games</h2>
        <div class="buttons">
            <md-outlined-button style="margin-right: 13px;">
                Join Game
                <span slot="icon" class="material-symbols-outlined" style="font-size: 18px;">
                    edit
                </span>
            </md-outlined-button>
            <md-filled-button>
                Create New
                <span slot="icon" class="material-symbols-outlined" style="font-size: 18px;">
                    add
                </span>
            </md-filled-button>
        </div>
        <div class="container">
            <GameCardContainer>
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
                <GameCard name="SAP-Tec." playerCount="20" dimensions="3" />
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

.container {
    position: relative;
    flex-grow: 1;
}

.buttons {
    position: absolute;
    top: 30px;
    right: 30px;
}
</style>