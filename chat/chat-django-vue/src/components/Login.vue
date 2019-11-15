<template>
    <div>
        <input v-model="login" placeholder="Login"/>
        <input v-model="password" placeholder="Password"/>
        <button @click="setLogin">Login</button>
    </div>
</template>

<script>

    import axios from 'axios';
    import $ from 'jquery'
    export default {
        name: "Login",
        data(){
            return{
                login: '',
                password: ''
            }
        },
        methods:{
            setLogin(){

                // $.ajax({
                //     url: "http://127.0.0.1:8000/auth/token/login/",
                //     type: "POST",
                //     data: {
                //         username: this.login,
                //         password: this.password
                //     },
                //     success: (response) => {
                //         console.log(response)
                //     },
                //     error: (response) => {
                //         if (response.status === 400) {
                //             alert("Логин или пароль не верен")
                //         }
                //     }
                // })

                let bodyFormData = new FormData();
                bodyFormData.set('username', this.login);
                bodyFormData.set('password', this.password);
                axios({
                    method: 'post',
                    url: 'http://127.0.0.1:8000/auth/token/login/',
                    data: bodyFormData,
                    headers: {'Content-Type': 'multipart/form-data' }
                })
                .then(response => {
                    console.log(response);
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
