<script setup></script>

<script>
export default {
    props: ["board", "game"],
    emits: ["change-cell-checked", "change-cell-text", "start-game", "set-ready"],
    data() {
        return {};
    },
    created() {},
    methods: {
        getUserId() {
            return window.userIds[this.game.id];
        },
        getValueOfTextField(rowIndex, colIndex) {
            return document.getElementById(`${rowIndex};${colIndex}`).value;
        },
        checkIfUserIsAdmin() {
            return this.getUserId() == this.game.admin_id;
        },
        checkIfEveryOneIsReady() {
            if (this.game == undefined || this.game.players == undefined) {
                return true;
            }
            console.log(this.game);
            return !this.game.players.every((value) => value.is_ready);
        },

        getOwnBoard() {
            let ownId = window.userIds[this.game.id];
            console.log(this.game.players);
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
};
</script>

<template>
    <div v-if="board != null">
        <h2 class="md-typescale-headline-large">
            {{
                board.user_id == getUserId()
                    ? `${board.name} (You)`
                    : board.name
            }}
        </h2>
        <table border="1" :class="{ won: board.has_bingo }">
            <tr v-for="(row, rowIndex) in board.fields" :key="rowIndex">
                <td
                    v-for="(elem, colIndex) of row"
                    :key="`${rowIndex};${colIndex}`"
                >
                    <template v-if="game.game_state == 'DRAFT'">
                        <template v-if="board.user_id !== getUserId()">
                            <span> {{ elem.content }}</span>
                        </template>
                        <input
                            v-else
                            type="text"
                            name="field-content"
                            :id="`${rowIndex};${colIndex}`"
                            @change.prevent="
                                $emit('change-cell-text', {
                                    row: rowIndex,
                                    col: colIndex,
                                    new_text: getValueOfTextField(
                                        rowIndex,
                                        colIndex,
                                    ),
                                    user_id: board.user_id,
                                })
                            "
                            :value="elem.content"
                        />
                    </template>
                    <template v-else-if="game.game_state == 'RUNNING'">
                        <div
                            @click="
                                $emit('change-cell-checked', {
                                    row: rowIndex,
                                    col: colIndex,
                                    new_checked: !elem.checked,
                                    user_id: board.user_id,
                                })
                            "
                            :class="{ checked: elem.checked }"
                        >
                            {{ elem.content }}
                        </div>
                    </template>
                </td>
            </tr>
        </table>
        <div
            class="buttons"
            style="bottom: 20px; position: absolute; right: 30px"
            v-if="this.game.game_state === 'DRAFT'"
        >
            <md-filled-tonal-button
                @click="this.$emit('set-ready')"
                :disabled="!checkIfAllFieldsHaveContent()"
            >
                Submit Board
                <md-icon slot="icon"> check </md-icon>
            </md-filled-tonal-button>
            <md-filled-button
                @click="this.$emit('start-game')"
                :disabled="checkIfEveryOneIsReady()"
            >
                Start Game
                <md-icon slot="icon"> done_all </md-icon>
            </md-filled-button>
        </div>
    </div>
</template>

<style scoped>
h2 {
    margin: 0;
    padding: 30px;
}

.checked {
    background-color: green;
}

.won {
    background-color: gold;
}

.buttons {
    position: absolute;
    display: flex;
    flex-direction: row;
    bottom: 30px;
    right: 30px;
}

.buttons > * {
    margin-left: 18px;
}
</style>
