<script setup>
import PlayersList from "./PlayerList.vue";
import PlayerBoard from "./PlayerBoard.vue";
</script>

<script>
export default {
    data() {
        return {
            socket: null,
            game: {},
            playerBoardIndex: 0,
            isFirstListen: true,
        };
    },

    emits: ["updateTitle"],

    methods: {
        refreshSocket() {
            this.socket.send("REFRESH");
        },
        changeCellChecked(payload) {
            payload["game_id"] = this.game.id;
            this.socket.send(`CHANGE_CELL_CHECKED ${JSON.stringify(payload)}`);
        },
        changeCellText(payload) {
            payload["game_id"] = this.game.id;
            this.socket.send(`CHANGE_CELL_TEXT ${JSON.stringify(payload)}`);
        },
        watchPlayer(index) {
            this.playerBoardIndex = index;
        },
        startGame() {
            this.socket.send(`START_GAME ${this.game.id}`);
        },
        setReady() {
            this.socket.send("SET_READY");
        },
        getOwnBoard() {
            let ownId = window.userIds[this.game.id];
            for (let player of this.game.players) {
                if (player.user_id == ownId) {
                    return player;
                }
            }
        },
        checkIfAllFieldsHaveContent() {
            let ownBoard = this.getOwnBoard();
            // sorry chris
            return ownBoard.fields.every((row) =>
                row.every((col) => col.content !== ""),
            );
        },
    },
    mounted() {
        this.socket = window.data[this.$route.params.game_id];
        if (this.socket == null) {
            alert("Socket was not found");
        }
        this.socket.onmessage = (event) => {
            let localGame = JSON.parse(event.data);
            this.game = localGame;
            if (this.isFirstListen) {
                this.playerBoardIndex = this.game.players.length - 1;
                this.isFirstListen = false;
            }

            this.$emit(
                "updateTitle",
                `${this.game.theme} (${this.$route.params.game_id})`,
            );
        };
        this.refreshSocket();
    },
};
</script>

<template>
    <div :key="game.game_state">
        <div v-if="game != null">
            <PlayerBoard
                :board="
                    game.players == undefined
                        ? null
                        : game.players[playerBoardIndex]
                "
                :game="game"
                @change-cell-checked="changeCellChecked"
                @change-cell-text="changeCellText"
                @start-game="startGame"
                @set-ready="setReady"
            >
            </PlayerBoard>
        </div>

        
    </div>

    <div>
        <PlayersList :game="game" @watchPlayer="watchPlayer"></PlayersList>
    </div>
</template>

<style scoped></style>
