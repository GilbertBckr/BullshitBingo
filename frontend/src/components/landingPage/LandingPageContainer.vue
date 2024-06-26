<script setup>
import GameCardContainer from "./GameCardContainer.vue";
import GameCard from "./GameCard.vue";
import { getAvailableGames } from "../../logic/gameRetrieval";
import { createGame, saveGameData } from "../../logic/token";
import DialogJoinGame from "./DialogJoinGame.vue";
import DialogCreateGame from "./DialogCreateGame.vue";
import DialogUsername from "./DialogUsername.vue";
</script>

<script>
import { createApp } from "vue";

export default {
    data() {
        return {
            isPopupVisible: false,
            isPrivateGameJoinVisible: false,
            formData: {
                theme: "",
                username: "",
                gameVisibility: "",
            },
            privateGameUsername: "",
            privateGameId: "",
            games: [],
            renderCreateGameDialog: false,
            renderJoinGameDialog: false,
            renderUsernameDialog: false,
        };
    },

    mounted() {
        this.$emit('updateTitle', 'Bullshit Bingo')
        this.$refs.gameCardContainer.centerContainer();
    },

    methods: {
        onJoinPrivateGame() {
            this.$refs.joinGameDialog.show();
        },

        async updateGames() {
            this.games = await getAvailableGames();
            if (this.$refs.gameCardContainer === null) {
                return;
            }
            
            this.$nextTick(() => {
                this.$refs.gameCardContainer.centerContainer();
            })
        },
        onEnterUsername(gameID) {
            this.$refs.enterNameDialog.show(gameID);
        },
    },
    async created() {
        this.interval = setInterval(() => {
            this.updateGames();
        }, 8000);
        this.updateGames();
    },
};
</script>
<template>
    <div ref="container">
        <DialogCreateGame ref="createGameDialog" />
        <DialogJoinGame ref="joinGameDialog" />
        <DialogUsername ref="enterNameDialog"></DialogUsername>
        <h2 class="md-typescale-headline-large">Active Games</h2>
        <div class="buttons">
            <md-outlined-button
                style="margin-right: 12px"
                @click="$refs.joinGameDialog.show"
            >
                Join Game
                <md-icon slot="icon"> edit </md-icon>
            </md-outlined-button>

            <md-filled-button @click="$refs.createGameDialog.show">
                Create New
                <md-icon slot="icon"> add </md-icon>
            </md-filled-button>
        </div>
        <div class="container">
            <GameCardContainer ref="gameCardContainer">
                <GameCard
                    v-for="game in games"
                    :name="game.theme"
                    :playerCount="game.players.length"
                    :dimensions="game.dimensions"
                    :key="game.id"
                    :gameId="game.id"
                    @onJoinGame="onEnterUsername"
                />
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
