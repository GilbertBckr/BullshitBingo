<script setup>
import PlayersList from "./playersList.vue";
import PlayerBoard from "./playerBoard.vue";
</script>

<script>
export default {
    data() {
        return {
            socket: null,
            game: {},
            playerBoardIndex: 0,
            isFirstListen: true,
        }
    },
    methods: {
        refreshSocket() {
            this.socket.send("REFRESH");
        },
        changeCellChecked(payload) {
            payload["game_id"] = this.game.id
            this.socket.send(`CHANGE_CELL_CHECKED ${JSON.stringify(payload)}`)
        },
        changeCellText(payload) {
            console.log(payload);

            payload["game_id"] = this.game.id
            this.socket.send(`CHANGE_CELL_TEXT ${JSON.stringify(payload)}`)
        },
        watchPlayer(index) {
            this.playerBoardIndex = index;
            console.log("watching..." + index);
        },
        startGame() {
            this.socket.send(`START_GAME ${this.game.id}`);
        },
        setReady() {
            this.socket.send("SET_READY");
        },

    },
    mounted() {
        this.socket = window.data[this.$route.params.game_id]
        if (this.socket == null) {
            alert("Socket was not found")
        }
        this.socket.onmessage = (event) => {
            console.log("Reeived message from token")
            let localGame = JSON.parse(event.data)
            console.log("Local game: " + localGame.game_state)
            console.log(localGame)
            this.game = localGame
            if (this.isFirstListen) {
                this.playerBoardIndex = this.game.players.length - 1;
                this.isFirstListen = false;

            }
        }
        this.refreshSocket()

    }
};
</script>

<template>
    <div :key="game.game_state">
        <h1>Lobby Game {{ $route.params.game_id }}</h1>
        <h2>{{ game.theme }}</h2>
        <template v-if="game != null">
            {{ game }}
            <PlayerBoard :board="game.players == undefined ? null : game.players[playerBoardIndex]" :game="game"
                @change-cell-checked="changeCellChecked" @change-cell-text="changeCellText" @start-game="startGame">
            </PlayerBoard>
        </template>

        <md-filled-button @click="setReady">
            Ready
        </md-filled-button>

    </div>

    <div style="width: 30%">
        <PlayersList :game="game" @watchPlayer="watchPlayer"></PlayersList>
    </div>
</template>

<style scoped></style>
