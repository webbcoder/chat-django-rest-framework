<template>
    <RoomSlot>
        <mu-col span="9" class="">
            <mu-row justify-content="end">
                <div class="add-user">
                    <AddUsers :room="id"></AddUsers>
                </div>
            </mu-row>
<!--            <mu-paper :z-depth="5">-->
            <mu-container class="chat-window">
                <mu-row direction="column" justify-content="start" align-items="end">

                    <div v-for="dialog in dialogs" style="text-align: right">
                        <mu-chip class="dialog-text">
                            <p><strong>{{dialog.user.username}}</strong></p>
                            <p>{{dialog.text}}</p>
                            <span>{{dialog.date}}</span>
                        </mu-chip>
                    </div>
                </mu-row>
            </mu-container>
<!--            </mu-paper>-->
            <mu-container>
                <mu-row direction="row" align-items="center">
                    <mu-col span="10">
                        <mu-text-field v-model="form.textarea" multi-line :rows="4" full-width></mu-text-field>
                    </mu-col>
                    <mu-col span="2">
                        <mu-button round color="primary" @click="sendMessage">Send</mu-button>
                    </mu-col>
                </mu-row>
            </mu-container>
        </mu-col>
    </RoomSlot>
</template>

<script>
    import axiosInit from '@/assets/axiaos.config';
    import RoomSlot from './Room'
    import AddUsers from "./AddUsers";
    export default {
        name: "dialog",
        props: {
            id: '',
        },
        components: {
            AddUsers,
            RoomSlot
        },
        data(){
            return{
                dialogs: '',
                form: {
                    textarea: ''
                }
            }
        },
        created(){
            this.loadDialog();
            setInterval(() => this.loadDialog(), 5000) ;
        },
        methods: {
            loadDialog(){
                const instance = axiosInit();
                instance({
                    method: 'get',
                    url: 'dialog/',
                    params: {
                        room: this.$route.params.id
                    },

                })
                .then(response => {
                    // console.log(response);
                    this.dialogs = response.data.data.data
                })
            },
            sendMessage(){
                const instance = axiosInit();
                let bodyFormData = new FormData();
                bodyFormData.set('text', this.form.textarea);
                bodyFormData.set('room', this.$route.params.id);
                instance({
                    method: 'post',
                    url: 'dialog/',
                    data: bodyFormData,

                })
                .then(response => {
                    console.log(response);
                    this.loadDialog()
                })
                .cathe(error => {
                    alert(error.statusText)
                })
            }
        }
    }
</script>

<style scoped>
    .dialog{
        border: 1px solid #000;
    }
    .dialog-text{
        display: block;
    }
    .chat-window{
        height: 50vh;
        overflow-y: auto;
    }
</style>
