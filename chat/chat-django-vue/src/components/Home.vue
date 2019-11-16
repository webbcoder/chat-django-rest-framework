<template>
    <div>
        <h1>Chat room</h1>
        <button v-if="!auth" @click="goLogin">Login</button>
        <button v-else @click="logout">Logout</button>
        <Room v-if="auth"></Room>
    </div>
</template>

<script>
    import Room from './rooms/Room';
    export default {
        name: "home",
        components: {Room},
        computed:{
            auth(){
                if(sessionStorage.getItem('auth_token')){
                    return true
                }
            }
        },
        methods: {
            goLogin(){
                this.$router.push({name: 'login'})
            },
            logout(){
                sessionStorage.removeItem('auth_token');
                window.location = '/';
            }
        }
    }
</script>

<style scoped>

</style>
