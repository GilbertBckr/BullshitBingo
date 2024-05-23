<script>
export default {
    props: ['title']
}
</script>
<template>
    <div class="wrapper">
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
    border-radius: 8px;
    background-color: var( --md-sys-color-surface-container);
    position: absolute;
    top: 130px;
    left: 30px;
    right: 30px;
    bottom: 30px;
}

.container {}
</style>