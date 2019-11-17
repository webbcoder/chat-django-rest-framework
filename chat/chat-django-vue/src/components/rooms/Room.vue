<template>
    <mu-paper :z-depth="5">
    <mu-col span="4" xl="3" lg="4">
        <div v-for="room in rooms">
            <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
            <span>{{room.date}}</span>
        </div>

    </mu-col>
    </mu-paper>
</template>

<script>
    import axiosInit from '@/assets/axiaos.config';
    export default {
        name: "Room",
        data() {
            return {
                rooms: ''
            }
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
                this.$emit('openDialog', id)
            }
        }
    }
</script>

<style scoped>
    h3{
        cursor: pointer;
    }
</style>
