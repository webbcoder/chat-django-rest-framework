<template>
    <div>
        <div v-for="dialog in dialogs">
            <h2>{{dialog.user.username}}</h2>
            <p>{{dialog.text}}</p>
            <span>{{dialog.date}}</span>
        </div>
    </div>
</template>

<script>
    import axiosInit from '@/assets/axiaos.config';
    export default {
        name: "dialog",
        props: {
            id: '',
        },
        data(){
            return{
                dialogs: '',
            }
        },
        created(){
            this.loadDialog()
        },
        methods: {
            loadDialog(){
                // let bodyFormData = new FormData();
                // bodyFormData.set('username', this.login);
                // bodyFormData.set('password', this.password);
                const instance = axiosInit();
                instance({
                    method: 'get',
                    url: 'dialog/',
                    params: {
                        room: this.id
                    },

                })
                .then(response => {
                    // console.log(response);
                    this.dialogs = response.data.data.data
                })
                .catch(error => {
                    console.log(error);
                });
            }
        }
    }
</script>

<style scoped>

</style>
