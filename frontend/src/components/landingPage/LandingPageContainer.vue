<script setup>
import GameCardContainer from './GameCardContainer.vue';
import GameCard from './GameCard.vue';
import { getAvailableGames } from '../../logic/gameRetrieval'
import { createGame, saveWebsocket } from '../../logic/token'
</script>

<script>
export default {
    data() {
        return {
            isPopupVisible: false,
            isPrivateGameJoinVisible: false,
            formData: {
                theme: '',
                username: ''
            },
            privateGameUsername: '',
            privateGameId: "",
            games: []
        }
    },
    methods: {
        showPopup() {
            this.isPopupVisible = true;
        },
        closePopup() {
            this.formData.theme = '';
            this.formData.username = '';

            this.isPopupVisible = false;
        },

        async submitForm() {
            let socket = await createGame(this.formData.username);
            socket.onmessage = (event) => {
                console.log(event.data);
                let game = JSON.parse(event.data);
                console.log(game)
                let id = game.id

                this.$router.push('/lobby/' + id);

            }
            this.games = await getAvailableGames();
            this.closePopup();
        },

        async submitPrivateGame(){
            this.isPrivateGameJoinVisible = false;
            joinGame(this.privateGameId, this.privateGameUsername);
            this.$router.push('/lobby/' + this.privateGameId);
        },
        closePopupPrivateGame(){
            this.isPrivateGameJoinVisible = false;
        },

        async onJoinedPrivateGame() {
            for (let i = 0; i < this.games.length; i++) {
                if (this.games[i].id == this.privateGameId) {
                    this.isPrivateGameJoinVisible = true;
                }
            }
            
        },
        async updateGames() {
            this.games = await getAvailableGames();
        }
    },
    async created() {
        this.interval = setInterval(() => {
            this.updateGames();
            console.log("Data from landing page");
            console.log(window.data);
        }, 8000)
        this.updateGames();
    }
}
</script>
<template>
    <div>
        <h2 class="md-typescale-headline-large">Active Games</h2>
        <div class="buttons">
            <input v-model="privateGameId" style="width: 10px;" />
            <md-outlined-text-field label="Game ID" class="gameid-textfield" v-model="privateGameId">
            </md-outlined-text-field>
            <md-outlined-button style="margin-right: 13px;" @click="onJoinedPrivateGame()">
                Join Game
                <span slot="icon" class="material-symbols-outlined" style="font-size: 18px;">
                    edit
                </span>
            </md-outlined-button>

            <md-filled-button @click="showPopup">
                Create New
                <span slot="icon" class="material-symbols-outlined" style="font-size: 18px">
                    add
                </span>
            </md-filled-button>

        </div>

        <div v-if="isPopupVisible" class="popup">
            <form @submit.prevent="submitForm" class="dialog">
                <h2 class="dialog-title">Create New Game</h2>

                <div class="dialog-content">
                    <label for="gameVisibility">Visibility:</label>
                    <select name="gameVisibility" id="gameVisibility" v-model="formData.gameVisibility">
                        <option value="private">Private</option>
                        <option value="public">Public</option>
                    </select>

                    <label for="theme">Theme:</label>
                    <input type="text" id="theme" v-model="formData.theme" required />

                    <label for="username">Username:</label>
                    <input type="text" id="username" v-model="formData.username" required />
                </div>

                <div class="dialog-actions">
                    <button type="submit" class="mdc-button mdc-button--raised">Submit</button>
                    <button type="button" class="mdc-button mdc-button--outlined" @click="closePopup">Close</button>
                </div>
            </form>
        </div>

        <div v-if="isPrivateGameJoinVisible" class="popup">
            <form @submit.prevent="submitPrivateGame" class="dialog">
            <h2 class="dialog-title">Join Game</h2>

            <div class="dialog-content">
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="privateGameUsername" required />
            </div>

            <div class="dialog-actions">
                <button type="submit" class="mdc-button mdc-button--raised">Join Game</button>
                <button type="button" class="mdc-button mdc-button--outlined" @click="closePopupPrivateGame">Close</button>
            </div>
            </form>
        </div>


        <div class="container">
            <GameCardContainer>
                <GameCard v-for="(game) in games" :name="game.theme" :playerCount="game.players.length"
                    :dimensions="game.dimensions" :key="game.id" :gameId="game.id" />
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

.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.3);
    z-index: 1000;
}

.dialog {
    background: white;
    border-radius: 4px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    width: 100%;
    padding: 20px;
    box-sizing: border-box;
}

.dialog-title {
    margin-top: 0;
    margin-bottom: 16px;
    font-size: 24px;
    text-align: center;
}

.dialog-content label {
    display: block;
    margin-top: 8px;
}

.dialog-content input,
.dialog-content select {
    width: calc(100% - 24px);
    margin: 8px 0;
    padding: 8px 12px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.dialog-actions {
    display: flex;
    justify-content: flex-end;
    margin-top: 24px;
}

.mdc-button {
    font-size: 14px;
    padding: 0 16px;
    line-height: 36px;
    border-radius: 4px;
    text-transform: uppercase;
}

.mdc-button--raised {
    background-color: #6200ea;
    color: white;
    margin-right: 8px;
}

.mdc-button--outlined {
    border: 1px solid #6200ea;
    color: #6200ea;
}

.gameid-textfield {
    height: 40px;
    padding-right: 10px;
}
</style>
