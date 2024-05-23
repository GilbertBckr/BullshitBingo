<script>
export default {

}
</script>
<template>
    <div class="wrapper">
        <slot />
    </div>

</template>
<style scoped>
.wrapper {
    display: flex;
    flex-direction: row;
    gap: 13px;
    flex-wrap: wrap;
}
</style>