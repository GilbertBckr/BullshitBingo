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

        }
    },
    methods: {
        refreshSocket() {
            this.socket.send("REFRESH");
        },
        changeCell(payload) {
            console.log(payload)
            this.socket.send(`CHANGE_CELL ${JSON.stringify(payload)}`)
        }
    },
    mounted() {
        this.socket = window.data[this.$route.params.game_id]
        if (this.socket == null) {
            alert("Socket was not found")
        }
        this.socket.onmessage = (event) => {
            console.log("Reeived message from token")
            let localGame = JSON.parse(event.data)
            console.log("Local game:")
            console.log(localGame)
            this.game = localGame
        }
        this.refreshSocket()
    }

}
</script>

<template>
    <div>
        <h1>Lobby Game {{ $route.params.game_id }}</h1>
        <template v-if="game != null">
            <PlayerBoard :board="game.players == undefined ? null : game.players[0]" @change-cell="changeCell"></PlayerBoard>

        </template>
    </div>
    <div>
        <PlayersList :game="game"></PlayersList>
    </div>
</template>

<style scoped></style>