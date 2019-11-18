<template>
  <div id="app">
      <mu-container>
          <Header></Header>
<!--        <mu-row justify-content="between">-->
<!--            <Room v-if="auth" @click=""></Room>-->
<!--            <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>-->
<!--        </mu-row>-->
        <mu-row justify-content="between">
            <router-view/>
        </mu-row>
    </mu-container>
  </div>
</template>

<script>
import HomeSlot from './components/Home';
import Header from './components/Header';

export default {
  name: 'App',
  components: {HomeSlot, Header}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
