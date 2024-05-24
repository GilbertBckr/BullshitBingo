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
            this.game = JSON.parse(event.data);
        }
    }

}
</script>

<template>
    <h1>Lobby</h1>
    Game {{ $route.params.game_id }}
    {{ game }}
</template>

<style scoped></style>