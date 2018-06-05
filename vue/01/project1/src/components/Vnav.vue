<template>

    <div >
        <router-link to="/">首页</router-link>
        <router-link to="/course">课程</router-link>
        <router-link to="/degree">路飞学位</router-link>
        <router-link to="/technoloy">深科技</router-link>
        <span v-if="this.$store.state.token">
            <a >{{this.$store.state.username}}</a>
            <a @click="logout">注销</a>
        </span>
        <span v-else>
            <router-link to="/login">登录|注册</router-link>
        </span>
    

    </div>

</template>



<script>
export default{
    name:'Vnav',
    data(){
        return{

        }
    },
    methods:{
        logout(){
            this.$store.commit('clearToken')
        }
    }
}

</script>



<style>

</style>
