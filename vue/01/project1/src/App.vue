<template>
  <div id="app">

      <Vnav></Vnav>
      <router-view></router-view>
  </div>
</template>

<script>
import Vnav from '@/components/Vnav'
// import Homesite from '@/components/Homesite'
export default {
  name: 'App',
  components:{
    Vnav,
    // Homesite,
  }
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
