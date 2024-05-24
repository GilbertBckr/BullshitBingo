<script>
export default {
    data() {
        return {
            counter: 0
        }
    }
}
</script>

<template>
    <button @click="counter++">Add 1</button>
    <p>The button above has been clicked {{ counter }} times.</p>
</template>