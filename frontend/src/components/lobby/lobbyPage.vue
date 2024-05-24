<script setup>
import playersList from "./playersList.vue";
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
    <h1>Lobby</h1>
    Game {{ $route.params.game_id }}
    <p>{{ game }}</p>
</template>

<style scoped></style>