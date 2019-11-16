<template>
    <div>
        <h1>Chat room</h1>
        <button v-if="!auth" @click="goLogin">Login</button>
        <button v-else @click="logout">Logout</button>
        <Room v-if="auth" @openDialog="openDialog"></Room>
        <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </div>
</template>

<script>
    import Room from './rooms/Room';
    import Dialog from "./rooms/Dialog";
    export default {
        name: "home",
        components: {
            Room,
            Dialog
        },
        data(){
            return{
                dialog: {
                    id: '',
                    show: false,
                }
            }
        },
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
            },
            openDialog(id){
                this.dialog.id = id;
                this.dialog.show = true;
            }

        }
    }
</script>

<style scoped>

</style>
