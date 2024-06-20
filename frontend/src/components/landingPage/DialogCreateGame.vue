<script setup></script>
<script>
import { saveGameData, createGame } from "../../logic/token";

export default {
    data() {
        return {
            username: "",
            theme: "",
            isPrivate: true,
        };
    },

    methods: {
        show() {
            this.$refs.inputTheme.reset();
            this.$refs.inputUsername.reset();
            this.isPrivate = true;
            this.$refs.inputPrivate.selected = true;
            this.$refs.dialog.show();
        },

        hide() {
            this.$refs.dialog.close();
        },

        async onFormSubmit() {
            const username = this.username;
            const theme = this.theme;
            const isPrivate = this.isPrivate;

            let [socket, user_id] = await createGame(
                username,
                theme,
                isPrivate,
            );
            socket.onmessage = (event) => {
                let game = JSON.parse(event.data);
                let id = game.id;
                this.$router.push("/lobby/" + id);
                saveGameData(socket, id, user_id);
            };

            this.hide();
        },
    },
};
</script>

<template>
    <md-dialog ref="dialog">
        <div slot="headline">Create Game</div>
        <form slot="content" id="createGameForm" @submit.prevent="onFormSubmit">
            <md-outlined-text-field
                label="Theme"
                ref="inputTheme"
                required
                v-model="theme"
            ></md-outlined-text-field>
            <md-outlined-text-field
                label="Your Username"
                ref="inputUsername"
                required
                v-model="username"
            ></md-outlined-text-field>
            <label class="md-typescale-body-large">
                Private
                <md-switch
                    ref="inputPrivate"
                    selected
                    icons
                    show-only-selected-icon
                    @change="this.isPrivate = this.$refs.inputPrivate.selected"
                ></md-switch>
            </label>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel" @click="hide"
                >Cancel</md-text-button
            >
            <md-text-button value="join" form="createGameForm" ref="buttonJoin"
                >Create</md-text-button
            >
        </div>
    </md-dialog>
</template>

<style scoped>
#createGameForm {
    display: flex;
    flex-direction: column;
}

#createGameForm > * {
    margin-bottom: 16px;
}

label {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
</style>
