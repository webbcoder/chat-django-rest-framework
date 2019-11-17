<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            Chat room
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">Login</mu-button>
            <mu-button flat slot="right" v-else @click="logout">Logout</mu-button>
        </mu-appbar>
        <mu-row>
            <h1></h1>
        </mu-row>
        <mu-row justify-content="between">
            <Room v-if="auth" @click=""></Room>
            <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
        </mu-row>
    </mu-container>
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
            // openDialog(id){
            //     this.dialog.id = id;
            //     this.dialog.show = true;
            // }

        }
    }
</script>

<style scoped>

</style>
