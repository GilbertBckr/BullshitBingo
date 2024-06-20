<script setup></script>

<script>
export default {
    emits: ["watchPlayer"],
    props: ["game"],
    data() {
        return {};
    },
    created() {
        this.players = this.game.players;
    },
};
</script>

<template>
    <div>
        <h2 class="md-typescale-headline-large">Players</h2>
        <md-list>
            <md-divider></md-divider>
            <div v-for="(player, index) in game.players">
                <md-list-item
                    style="width: 100%"
                    @click="$emit('watchPlayer', index)"
                >
                    <md-ripple></md-ripple>
                    {{ player.name }}
                    <md-icon slot="start" :key="index">{{
                        game.game_state === "DRAFT"
                            ? player.is_ready
                                ? "check"
                                : ""
                            : player.has_bingo
                              ? "trophy"
                              : ""
                    }}</md-icon>
                    <md-icon slot="end" :key="index">chevron_right</md-icon>
                </md-list-item>
                <md-divider></md-divider>
            </div>
        </md-list>
    </div>
</template>

<style scoped>
md-list {
    --md-list-container-color: var(--md-sys-color-surface-container);
    position: relative;
    width: 100%;
    margin-bottom: 28px;
}

md-list-item {
    position: relative;
}

md-list-item:hover {
    cursor: pointer;
}

h2 {
    margin: 0;
    padding: 30px;
}
</style>
