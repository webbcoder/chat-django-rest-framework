<template>
    <Room v-if="auth"></Room>
</template>

<script>
    import Room from './rooms/Room';
    export default {
        name: "home",
        components: {Room},
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

</style>
