<script>
export default {
    props: ['name', 'playerCount', 'dimensions']
}
</script>
<template>
    <div>
        <h4 class="name">{{ name }}</h4>
        <p class="info">{{ playerCount }} Player  · {{ dimensions }}x{{ dimensions }}</p>
        <md-filled-button>Enter</md-filled-button>
    </div>
</template>
<script>
</script>