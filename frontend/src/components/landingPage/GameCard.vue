<script setup>
import DialogUsername from "./DialogUsername.vue";
</script>

<script>
import { joinGame } from "@/logic/token";
export default {
    props: ["name", "playerCount", "dimensions", "gameId"],
    data() {
        return {
            isPopupVisible: false,
            formData: {
                username: "",
            },
        };
    },
    methods: {
        showPopup() {
            this.isPopupVisible = true;
        },
        closePopup() {
            this.formData.username = "";
            this.isPopupVisible = false;
        },
        joinGame() {
            console.log(this.formData);
            console.log(this.gameId);
            // TODO: check if username is already used
            joinGame(this.gameId, this.formData.username, () => {
                this.$router.push("/lobby/" + this.gameId);
            });
            this.closePopup();
        },
    },
};
</script>
<template>
    <DialogUsername ref="dialog" :id="gameId"></DialogUsername>

    <div class="card">
        <md-elevation></md-elevation>
        <h4 class="name md-typescale-title-large">{{ name }}</h4>
        <p class="info md-typescale-label-medium">
            {{ playerCount }} Player · {{ dimensions }}x{{ dimensions }}
        </p>
        <md-filled-button class="button" @click="$refs.dialog.show"
            >Join</md-filled-button
        >
    </div>
</template>
<style scoped>
.card {
    position: relative;
    width: calc(200px - 24px);
    height: calc(200px - 24px);
    padding: 12px;
    border-radius: 12px;
    background-color: var(--md-sys-color-surface-container-highest);
    --md-elevation-level: 1;
}

.name,
.info {
    margin: 0;
}

.button {
    position: absolute;
    bottom: 12px;
    right: 12px;
}
</style>
