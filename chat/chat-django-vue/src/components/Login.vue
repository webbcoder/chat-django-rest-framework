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


                // axios.post(`http://127.0.0.1:8000/auth/token/login/`, JSON.stringify({
                //     username: this.login,
                //     password: this.password
                // }))
                // .then(response => console.log(response))
                // .catch(error => console.log(error));

                axios({
                    method: 'post',
                    // mode: 'no-cors',
                    url: 'http://127.0.0.1:8000/auth/token/login/',
                    data: JSON.stringify({
                        username: this.login,
                        password: this.password,
                        // Authorization: 'Token ca01c725e2352077e3829ab99aef2920b482eb60'

                    }),
                    // xsrfHeaderName: "X-CSRFToken",
                    // xsrfCookieName: 'XCSRF-TOKEN',
                    // headers:{'Content-Type': 'application/json; charset=utf-8'}
                    config: {
                        headers: {'Content-Type': 'application/json; charset=utf-8' },
                    },
                    headers: {
                        // 'Access-Control-Allow-Origin': '*',
                        // 'Access-Control-Allow-Headers': '*',
                        'Accept': 'application/json',
                        // 'Content-Type': 'application/json',
                        'Content-Type' : 'application/x-www-form-urlencoded',
                        'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
                        'Access-Control-Expose-Headers': 'Access-Token, Uid',
                        'Access-Control-Allow-Methods': 'GET, PUT, POST, DELETE, OPTIONS',
                        // 'Access-Control-Allow-Credentials': 'true',
                        // 'X-Requested-With': 'XMLHttpRequest',
                    },
                    // withCredentials: false,
                    // credentials: 'same-origin',
                })
                .then(response => {
                    console.log(response);
                    // console.log(csrftoken);
                })
                .catch(error => {
                    console.log(error);
                    // console.log(csrftoken);
                });
            }
        }
    }
</script>

<style scoped>

</style>
