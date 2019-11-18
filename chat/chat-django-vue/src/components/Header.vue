<template>
    <div class="header">
        <mu-appbar style="width: 100%;" color="primary">
            Chat room
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">Login</mu-button>
            <mu-button flat slot="right" v-else @click="logout">Logout</mu-button>
        </mu-appbar>
    </div>
</template>

<script>
    import Room from './rooms/Room';
    export default {
        name: "header",
        // components: {
        //     Room,
        //     Dialog
        // },
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
    .header{
        margin-bottom: 20px;
    }
</style>
