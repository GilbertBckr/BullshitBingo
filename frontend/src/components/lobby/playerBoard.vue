<script setup>
import DialogCell from "./DialogCell.vue";
</script>

<script>
export default {
    props: ["board", "game"],
    emits: [
        "change-cell-checked",
        "change-cell-text",
        "start-game",
        "set-ready",
    ],
    data() {
        return {
            focusedColumn: 0,
            focusedRow: 0,
            focusedPlayerID: "",
        };
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
            return !this.game.players.every((value) => value.is_ready);
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
        onCellClick(row, column, element) {
            if (!this.board.is_ready) {
                this.$refs.dialog.show(
                    row,
                    column,
                    this.board.user_id,
                    element.content,
                );
                return;
            }

            if (this.game.game_state === "RUNNING") {
                this.$emit("change-cell-checked", {
                    row: row,
                    col: column,
                    new_checked: !element.checked,
                    user_id: this.board.user_id,
                })
            }
        },
    },
};
</script>

<template>
    <div v-if="board != null">
        <DialogCell
            ref="dialog"
            @change-cell-text="(event) => $emit('change-cell-text', event)"
        ></DialogCell>
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
                    class="md-typescale-body-medium"
                    v-for="(elem, colIndex) of row"
                    :key="`${rowIndex};${colIndex}`"
                    v-on:click="onCellClick(rowIndex, colIndex, elem)"
                    :empty="elem.content === '' ? true : null"
                    :checked="elem.checked ? true : null"
                >
                    <md-ripple></md-ripple>
                    {{ elem.content }}
                </td>
            </tr>
        </table>
        <div
            class="buttons"
            style="bottom: 20px; position: absolute; right: 30px"
            v-if="game.game_state === 'DRAFT'"
        >
            <md-filled-tonal-button
                @click="$emit('set-ready')"
                :disabled="!checkIfAllFieldsHaveContent()"
                :hidden="board.is_ready ? true : null"
            >
                Submit Board
                <md-icon slot="icon"> check </md-icon>
            </md-filled-tonal-button>
            <md-filled-button
                @click="$emit('start-game')"
                :disabled="checkIfEveryOneIsReady()"
            >
                Start Game
                <md-icon slot="icon"> done_all </md-icon>
            </md-filled-button>
        </div>
    </div>
</template>

<style scoped>
table {
    padding: 30px;
    border: 0;
    padding-top: 0;
    border-spacing: 8px;
}

td {
    position: relative;
    width: 100px;
    height: 100px;
    border: 0;
    border-radius: 12px;
    background-color: var(--md-sys-color-surface-container-highest);
    text-align: center;
    padding: 5px;
    transition: background-color .5s;
}

td:hover {
    cursor: pointer;
}

td[empty] {
    background-color: var(--md-sys-color-error-container);
}

td[checked] {
    background-color: #81c784;
}

h2 {
    margin: 0;
    padding: 30px;
}

md-filled-tonal-button[hidden] {
    visibility: collapse;
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
