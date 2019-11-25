<template>
    <mu-container>
        <mu-row justify-content="end">
<!--            <div class="add-user">-->
<!--                <AddUsers :room="id"></AddUsers>-->
<!--            </div>-->
        </mu-row>
        <mu-row>
            <mu-col span="3" class="rooms-list">
                <mu-button @click="addRoom">Create room</mu-button>
                <div v-for="room in rooms">
                    <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
                    <span>{{room.date}}</span>
                </div>
            </mu-col>
            <slot></slot>
        </mu-row>
    </mu-container>
</template>

<script>
    import axiosInit from '@/assets/axiaos.config';
    import HomeSlot from '../Home'
    import AddUsers from "./AddUsers";
    export default {
        name: "Room",
        data() {
            return {
                rooms: ''
            }
        },
        components:{
            HomeSlot,
            AddUsers
        },
        created() {
            this.loadRoom();
        },
        methods: {
            loadRoom() {
                const instance = axiosInit();
                instance({
                    method: 'get',
                    url: "room/"
                })
                .then(response => {
                    this.rooms = response.data.data.data
                })
            },
            openDialog(id){
                //this.$emit('openDialog', id)
                this.$router.push({name: 'dialog', params: {id: id}})
            },
            addRoom() {
                const instance = axiosInit();
                instance({
                    method: 'post',
                    url: 'room/',
                })
                .then(response => {
                    //console.log(response);
                    this.loadRoom();
                })
                .catch(error => alert(error.statusText))
            }
        }
    }
</script>

<style scoped>
    h3{
        cursor: pointer;
    }
    .rooms-list {
        /*margin: 0 10px 0 0;*/
        box-shadow: 1px 4px 5px #848181;
        height: 50vh;
        overflow-y: auto;
    }
    .add-user{
        margin: 20px 0;
    }
</style>
