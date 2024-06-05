<script setup></script>
<script>
export default {
    emits: ["change-cell-text"],

    data() {
        return {
            cell: "",
            row: 0,
            column: 0,
            userID: '',
        };
    },

    methods: {
        show(row, column, userID, currentText) {
            this.$refs.inputCell.reset();
            this.$refs.dialog.show();
            this.row = row;
            this.column = column;
            this.userID = userID;

            this.$nextTick(() => {
                this.cell = currentText;
            })
        },

        hide() {
            this.$refs.dialog.close();
        },

        onFormSubmit() {
            this.$emit("change-cell-text", {
                row: this.row,
                col: this.column,
                new_text: this.cell,
                user_id: this.userID,
            });
            this.hide();
        },
    },
};
</script>

<template>
    <md-dialog ref="dialog">
        <div slot="headline">Board Cell</div>
        <form slot="content" id="cellForm" @submit.prevent="onFormSubmit">
            <md-outlined-text-field
                label="Cell"
                ref="inputCell"
                required
                v-model="cell"
            ></md-outlined-text-field>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel" @click="hide"
                >Cancel</md-text-button
            >
            <md-text-button value="join" form="cellForm" ref="buttonJoin"
                >Ok</md-text-button
            >
        </div>
    </md-dialog>
</template>

<style scoped>
#cellForm {
    display: flex;
    flex-direction: column;
}

#cellForm > * {
    margin-bottom: 16px;
}
</style>
