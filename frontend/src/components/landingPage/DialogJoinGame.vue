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

    mounted() {
        this.$refs.buttonCancel.addEventListener("click", async () => {
            this.hide();
        });

        this.$refs.form.addEventListener("submit", async () => {
            const username = this.$data.username;
            const id = this.$data.id;
            debugger;
        });
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
    },
};
</script>

<template>
    <md-dialog ref="dialog">
        <div slot="headline">Join Game</div>
        <form slot="content" id="joinGameForm" ref="form">
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
            <md-text-button value="cancel" ref="buttonCancel"
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
