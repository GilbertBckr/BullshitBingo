// TODO: Do manual validation.
<script setup></script>
<script>
export default {
    data() {
        return {
            username: "",
        };
    },

    mounted() {
        this.$refs.buttonCancel.addEventListener("click", async () => {
            this.hide();
        });

        this.$refs.form.addEventListener("submit", async () => {
            const username = this.$data.username;
        });
    },

    methods: {
        reset() {},

        show() {
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
        <div slot="headline">Enter Username</div>
        <form slot="content" id="usernameForm" ref="form">
            <md-outlined-text-field
                label="Username"
                ref="inputUsername"
                required
                :value="username"
            ></md-outlined-text-field>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel"
                >Cancel</md-text-button
            >
            <md-text-button value="join" form="usernameForm" ref="buttonJoin"
                >Join</md-text-button
            >
        </div>
    </md-dialog>
</template>

<style scoped>
#usernameForm {
    display: flex;
    flex-direction: column;
}

#usernameForm > * {
    margin-bottom: 16px;
}
</style>
