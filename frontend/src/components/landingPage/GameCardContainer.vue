<script>
export default {
    data() {
        return {
            centeringOffset: 0,
        };
    },

    mounted() {
        this.centerContainer();
    },

    created() {
        window.addEventListener("resize", this.centerContainer);
    },
    destroyed() {
        window.removeEventListener("resize", this.centerContainer);
    },
    methods: {
        centerContainer() {
            if (this.$refs.cardContainer === null) {
                return;
            }

            const cardCount = this.$refs.cardContainer.childElementCount;
            const cardWidth = 200;
            const gapWidth = 13;
            const paddingContainer = 30;
            const containerWidth = this.$refs.cardContainer.offsetWidth;
            const gap =
                (containerWidth - 2 * paddingContainer) %
                (cardWidth + gapWidth);
            if (
                containerWidth - 2 * paddingContainer >=
                cardCount * (cardWidth + gapWidth) - gapWidth
            ) {
                this.centeringOffset = 0;
            } else if (gap < cardWidth) {
                this.centeringOffset = gap / 2;
            } else {
                this.centeringOffset = (gap - cardWidth) / 2;
            }
        },
    },
};
</script>
<template>
    <div ref="cardContainer" class="cardContainer">
        <slot />
    </div>
</template>
<style scoped>
.cardContainer {
    display: flex;
    flex-direction: row;
    padding-right: 30px;
    padding-bottom: 30px;
    padding-left: calc(30px + calc(v-bind(centeringOffset) * 1px));
    gap: 13px;
    flex-wrap: wrap;
    overflow: scroll;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
}
</style>
