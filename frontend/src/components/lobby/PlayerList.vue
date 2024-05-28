<script setup></script>

<script>
export default {
    props: ["game"],
    data() {},
    created() {
        this.players = this.game.players;
    },
    methods: {
        watchPlayer(index) {
            console.log("watching..." + index);
        },
    },
};
</script>

<template>
    <div>
        <div
            style="
                max-width: fit-content;
                margin-left: auto;
                margin-right: auto;
            "
        >
            <h2 class="md-typescale-headline-large">Players</h2>
            <md-list
                style="
                    width: 100%;
                    background-color: var(--md-sys-color-surface-container);
                "
            >
                <div
                    v-for="(player, index) in game.players"
                    style="width: 250px"
                    :class="{ won: player.has_bingo }"
                >
                    <!-- TODO: dynamically size the div-->
                    <md-list-item
                        style="width: 100%"
                        @click="$emit('watchPlayer', index)"
                    >
                        <md-outlined-icon-button
                            ><md-icon>check</md-icon></md-outlined-icon-button
                        >
                        {{ player.name }}
                        <md-icon slot="end" :key="index">check</md-icon>
                    </md-list-item>
                    <md-divider></md-divider>
                </div>
            </md-list>
        </div>
    </div>
</template>

<style scoped>
.won {
    background-color: gold;
}

h2 {
    margin: 0;
    padding: 30px;
}
</style>
