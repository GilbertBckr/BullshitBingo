<script>
export default {
    props: ['title']
}
</script>
<template>
    <div class="wrapper">
        <md-elevation></md-elevation>
        <h2 class="md-typescale-headline-large">{{ title }}</h2>
        <div class="container">
            <slot />
        </div>
    </div>

</template>
<style scoped>
h2 {
    margin: 0;
    padding: 30px;
}

.wrapper {
    border-radius: 12px;
    background-color: var(--md-sys-color-surface-container);
    position: relative;
    height: 100%;
    width: 100%;
    --md-elevation-level: 1;
}
</style>