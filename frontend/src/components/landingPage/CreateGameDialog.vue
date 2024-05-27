// TODO: Do manual validation.
<script setup>
</script>
<script>
export default {
    data() {
        return {
            username: '',
            theme: '',
            private: true,
        }
    },

    mounted() {
        this.$refs.buttonCancel.addEventListener('click', async () => {
            await this.$refs.dialog.close();
        });

        this.$refs.form.addEventListener('submit', async () => {
            const username = this.$data.username;
            const id = this.$data.id;
        })
    }


}
</script>

<template>
    <md-dialog open ref="dialog">
        <div slot="headline">
            Create Game
        </div>
        <form slot="content" id="form" ref="form">
            <md-outlined-text-field label="Theme" ref="inputTheme" required :value="theme"></md-outlined-text-field>
            <md-outlined-text-field label="Your Username" ref="inputUsername" required
                :value="username"></md-outlined-text-field>
            <label class="md-typescale-body-large">
                Private
                <md-switch :selected="private" icons show-only-selected-icon></md-switch>
            </label>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel">Cancel</md-text-button>
            <md-text-button value="join" form="form" ref="buttonJoin">Create</md-text-button>
        </div>
    </md-dialog>
</template>

<style scoped>
#form {
    display: flex;
    flex-direction: column;
}

#form>* {
    margin-bottom: 16px;
}

label {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center; 
}
</style>