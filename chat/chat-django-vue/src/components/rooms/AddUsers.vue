<template>
    <div>
        <select v-model="option">
            <option v-for="user in list"
                    :value="user.id">
                {{user.attributes.username}}
            </option>
        </select>
        <mu-button class="btn-send" round color="primary" @click="addUser">Add user</mu-button>
    </div>
</template>

<script>
    import axiosInit from '@/assets/axiaos.config';
    export default {
        name: "AddUsers",
        props: {
            room: '',
        },
        data() {
            return {
                option: '',
                list: '',
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            loadUsers(){
                const instance = axiosInit();
                instance({
                    method: 'get',
                    url: 'users/',

                })
                .then(response => {
                    this.list = response.data.data;
                })
                .catch(error => {
                    console.log(error)
                })
            },
            addUser(){
                console.log(this.room);
                const instance = axiosInit();
                let bodyFormData = new FormData();
                bodyFormData.set('room', this.$route.params.id);
                bodyFormData.set('user', parseInt(this.option));
                instance({
                    method: 'post',
                    url: 'users/',
                    data: bodyFormData,
                    headers: {'Content-Type': 'multipart/form-data' }
                })
                .then(response => {
                    alert('Add user')
                })
                .catch(error => {
                    console.log(error);
                    alert(error.statusText)
                });
            }
        }
    }
</script>

<style scoped>

</style>
