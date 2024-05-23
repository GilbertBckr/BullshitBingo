<script>
export default {
    data() {
        return {
            centeringOffset: 0,
        };
    },

    mounted() {
        this.centerWrapper()
    },

    created() {
        window.addEventListener("resize", this.centerWrapper);
    },
    destroyed() {
        window.removeEventListener("resize", this.centerWrapper);
    },
    methods: {
        centerWrapper() {
            let cardWidth = 200;
            let gapWidth = 13;
            let paddingContainer = 30;
            let gap = (this.$refs.wrapper.offsetWidth - 2 * paddingContainer) % (cardWidth + gapWidth);
            if (gap < cardWidth) {
                this.$data.centeringOffset = gap / 2;
            } else {
                this.$data.centeringOffset = (gap - cardWidth) / 2;
            }
        }
    }
}
</script>
<template>
    <div ref="wrapper" class="wrapper">
        <slot />
    </div>

</template>
<style scoped>
.wrapper {
    display: flex;
    flex-direction: row;
    padding-right: 30px;
    padding-left: calc(30px + calc(v-bind(centeringOffset) * 1px));
    gap: 13px;
    flex-wrap: wrap;
    overflow: scroll;
    position: absolute;
    top: 0;
    bottom: 0;
}
</style>