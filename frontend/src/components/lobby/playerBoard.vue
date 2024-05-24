<script setup>

</script>

<script>
export default {
    props: ["board"],
    emits: ["change-cell-checked"],
    data() {

    },
    created() {
    },
    methods: {
        startGame(){
            
        }
    }
}
</script>

<template>


    <div>
        <div v-if="board != null">
            <h2>{{ board.name }}</h2>
            <table border="1">
                <tr v-for="(row, rowIndex) in board.fields" :key="rowIndex">
                    <td v-for="(elem, colIndex) of row" :key="`${rowIndex};${colIndex}`"
                        @click="$emit('change-cell-checked', { row: rowIndex, col: colIndex, new_checked: !elem.checked, user_id: board.user_id })"
                        :class="{ checked: elem.checked }"> {{ rowIndex }} {{ colIndex }}
                        {{ elem }}

                    </td>
                </tr>
            </table>

        </div>
        <div class="buttons" style="bottom: 20px; position: absolute; right: 30px;">
            <md-outlined-button @click="startGame">
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
</style>