// TODO: Do manual validation.
<script setup></script>
<script>
export default {
    data() {
        return {
            username: "",
        };
    },

    methods: {
        show() {
            this.$refs.inputUsername.reset();
            this.$refs.dialog.show();
        },

        hide() {
            this.$refs.dialog.close();
        },

        onFormSubmit() {
            const username = this.$data.username;
        },
    },
};
</script>

<template>
    <md-dialog ref="dialog">
        <div slot="headline">Enter Username</div>
        <form slot="content" id="usernameForm" @submit.prevent="onFormSubmit">
            <md-outlined-text-field
                label="Username"
                ref="inputUsername"
                required
                v-model="username"
            ></md-outlined-text-field>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel" @click="hide"
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
