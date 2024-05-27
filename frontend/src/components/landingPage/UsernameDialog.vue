// TODO: Do manual validation.
<script setup>
</script>
<script>
export default {
    data() {
        return {
            username: '',
        }
    },

    mounted() {
        this.$refs.buttonCancel.addEventListener('click', async () => {
            await this.$refs.dialog.close();
        });

        this.$refs.form.addEventListener('submit', async () => {
            const username = this.$data.username;
        })
    }


}
</script>

<template>
    <md-dialog open ref="dialog">
        <div slot="headline">
            Enter Username
        </div>
        <form slot="content" id="form" ref="form">
            <md-outlined-text-field label="Username" ref="inputUsername" required :value="username"></md-outlined-text-field>
        </form>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel">Cancel</md-text-button>
            <md-text-button value="join" form="form" ref="buttonJoin">Join</md-text-button>
        </div>
    </md-dialog>
</template>

<style scoped></style>