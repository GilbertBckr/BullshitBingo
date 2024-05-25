<script setup>

</script>

<script>
export default {
    props: ["board", "game"],
    emits: ["change-cell-checked", "change-cell-text", "start-game"],
    data() {
        return {
        }

    },
    created() {
    },
    methods: {
        getUserId() {
            return window.userIds[this.game.id];
        },
        getValueOfTextField(rowIndex, colIndex) {
            return document.getElementById(`${rowIndex};${colIndex}`).value
        }
    },
    mounted() {

    }
}
</script>

<template>


    <div>
        <div v-if="board != null">
            <h2>{{ board.user_id == getUserId() ? "Du" : board.name }}</h2>
            <table border="1" :class="{won: board.has_bingo}">
                <tr v-for="(row, rowIndex) in board.fields" :key="rowIndex">
                    <td v-for="(elem, colIndex) of row" :key="`${rowIndex};${colIndex}`"> {{ rowIndex }} {{ colIndex }}
                        <template v-if="game.game_state == 'DRAFT'">
                            <form
                                @submit.prevent="$emit('change-cell-text', { row: rowIndex, col: colIndex, new_text: getValueOfTextField(rowIndex, colIndex), user_id: board.user_id })">
                                <input type="text" name="field-content" :id="`${rowIndex};${colIndex}`"
                                    :value="elem.content">
                            </form>

                        </template>
                        <template v-else-if="game.game_state == 'RUNNING'">
                            <div @click="$emit('change-cell-checked', {
                                row: rowIndex, col: colIndex, new_checked:
                                    !elem.checked, user_id: board.user_id
                            })" :class="{ checked: elem.checked }"> {{ rowIndex
                                }} {{ colIndex }}
                                {{ elem }}</div>

                        </template>

                    </td>
                </tr>
            </table>

        </div>
        <div class="buttons" style="bottom: 20px; position: absolute; right: 30px;">
            <md-outlined-button @click="this.$emit('start-game')">
                Start Game
                <span slot="icon" class="material-symbols-outlined" style="font-size: 18px;">
                    edit
                </span>
            </md-outlined-button>
        </div>
    </div>
</template>

<style scoped>
.checked {
    background-color: green;
}

.won {
    background-color: gold;
}
</style>