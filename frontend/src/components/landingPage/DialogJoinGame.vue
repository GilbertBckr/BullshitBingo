// TODO: Do manual validation.
<script setup></script>
<script>
export default {
    data() {
        return {
            username: "",
            id: "",
        };
    },

    methods: {
        show() {
            this.$refs.inputID.reset();
            this.$refs.inputUsername.reset();
            this.$refs.dialog.show();
        },

        hide() {
            this.$refs.dialog.close();
        },

        onFormSubmit() {
            const username = this.$data.username;
            const id = this.$data.id;
        },
    },
};
</script>

<template>
    <md-dialog ref="dialog">
        <div slot="headline">Join Game</div>
        <form slot="content" id="joinGameForm" @submit.prevent="onFormSubmit">
            <md-outlined-text-field
                label="Game ID"
                ref="inputID"
                required
                minLength="5"
                maxLength="5"
                v-model="inputID"
            ></md-outlined-text-field>
            <md-outlined-text-field
                label="Username"
                ref="inputUsername"
                required
                v-model="inputUsername"
            ></md-outlined-text-field>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel" @click="hide"
                >Cancel</md-text-button
            >
            <md-text-button value="join" form="joinGameForm" ref="buttonJoin"
                >Join</md-text-button
            >
        </div>
    </md-dialog>
</template>

<style scoped>
#joinGameForm {
    display: flex;
    flex-direction: column;
}

#joinGameForm > * {
    margin-bottom: 16px;
}
</style>
