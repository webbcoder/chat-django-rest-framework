<template>
    <div>
        <ul>
            <li v-for="room in rooms">
                <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
                <span>{{room.date}}</span>
            </li>
        </ul>
    </div>
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
                .catch(error => {
                    console.log(error);
                });
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
