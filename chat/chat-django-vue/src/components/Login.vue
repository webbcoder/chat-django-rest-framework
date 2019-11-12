<template>
    <div>
        <input v-model="login" placeholder="Login"/>
        <input v-model="password" placeholder="Password"/>
        <button>Login</button>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return{
                login: '',
                password: ''
            }
        }
    }
</script>

<style scoped>

</style>
