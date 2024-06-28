<script setup></script>
<script>
import { joinGame } from "@/logic/token";

export default {
    methods: {
        show() {
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
        <div slot="headline">How to Play</div>
        <div slot="content">
            <h3>Start to play!</h3>
            <ul>
                <li>Press "Create Game" to create a new Game! The private option lets you specify if players need the game code to join or if the game can be accessed from the list.</li>
                <li>Join a private game with the "Join Game" button and enter the code provided to you.</li>
                <li>Or choose a game from the list of public games and start the fun!</li>
            </ul>
            <h3>Create your bingo board!</h3>
            <ul>
                <li>Click on the fields of your bingo board to enter a value.</li>
                <li>If all fields are filled press on "Submit Board" to finish editing.</li>
                <li>Watch your opponents by clicking on them in the Player List!</li>
            </ul>
            <h3>BINGOOOO!</h3>
            <ul>
                <li>If something you wrote happens, click on the field to check it!</li>
                <li>Once 3 fields in a row, column or diagonal are checked you WIN! Don't forget to shout "BINGOOO"!</li>
                <li>Watch your opponents by clicking on them in the player List!</li>
            </ul>
            <h3>Leave the game!</h3>
            <ul>
                <li>If your mama raised a quitter just close the tab.</li>
                <li>We will continue to display your board, so the others can still see it.</li>
            </ul>
        </div>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel" @click="hide"
                >Close</md-text-button
            >
        </div>
    </md-dialog>
</template>

<style scoped>
</style>
