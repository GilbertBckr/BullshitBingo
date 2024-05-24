<script setup>

</script>

<script>
export default {
    props: ['game'],
}
</script>

<template>
    <div>
        
        <div style="max-width: fit-content; margin-left: auto; margin-right: auto;">
            <h1>Players</h1>
            <md-list style="width: 100%; background-color: var(--md-sys-color-surface-container);">
                <div v-for="(player, index) in game.players" style="width: 250px;"> <!-- TODO: dynamically size the div-->
                    <md-list-item style="width: 100%">
                        <md-outlined-icon-button><md-icon>check</md-icon></md-outlined-icon-button>
                        {{ player.name }}
                        <md-icon slot="end" @click="$emit('watchPlayer', index)" :key="index">check</md-icon>
                    </md-list-item>
                    <md-divider></md-divider>
                </div>
            </md-list>
        </div>
    </div>
</template>

<style scoped>

</style>