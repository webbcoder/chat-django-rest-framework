<template>
    <div>
        <ul>
            <li v-for="room in rooms">
                <h3>{{room.creator.username}}</h3>
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
                rooms: '',
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
        }
    }
</script>

<style scoped>

</style>
