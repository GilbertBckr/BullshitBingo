<script setup>

</script>

<script>
export default {
    props: ["board"],
    emits: ["change-cell"],
    data() {

    },
    created() {
    }
}
</script>

<template>

    <div>
        <div v-if="board != null">
            <table border="1">
                <tr v-for="(row, rowIndex) in board.fields" :key="rowIndex">
                    <td v-for="(elem, colIndex) of row" :key="`${rowIndex};${colIndex}`"
                        @click="$emit('change-cell', { row: rowIndex, col: colIndex, newCheckedValue: !elem.checked })"
                        :class="{ checked: elem.checked }"> {{ rowIndex }} {{ colIndex }}
                        {{ elem }}

                    </td>
                </tr>
            </table>

        </div>
    </div>
</template>

<style scoped>
.checked {
    background-color: green;
}
</style>