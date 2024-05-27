// TODO: Do manual validation.
<script setup></script>
<script>
export default {
    data() {
        return {
            username: "",
            theme: "",
            isPrivate: true,
        };
    },

    mounted() {
        this.$refs.buttonCancel.addEventListener("click", async () => {
            this.hide();
        });

        this.$refs.inputPrivate.addEventListener("change", () => {
            this.$data.isPrivate = this.$refs.inputPrivate.selected;
        });

        this.$refs.form.addEventListener("submit", async (e) => {
            const username = this.$data.username;
            const theme = this.$data.theme;
            const isPrivate = this.$data.isPrivate;
            e.preventDefault();
        });
    },

    methods: {
        show() {
            this.$refs.inputTheme.reset();
            this.$refs.inputUsername.reset();
            this.$data.isPrivate = true;
            this.$refs.inputPrivate.selected = true;
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
        <div slot="headline">Create Game</div>
        <form slot="content" id="createGameForm" ref="form">
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
                ></md-switch>
            </label>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel"
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
