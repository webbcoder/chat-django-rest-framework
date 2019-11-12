<template>
    <div>
        <h1>Chat room</h1>
        <button @click="goLogin">Login</button>
    </div>
</template>

<script>
    export default {
        name: "home",
        methods: {
            goLogin(){
                this.$router.push({name: 'login'})
            }
        }
    }
</script>

<style scoped>

</style>
