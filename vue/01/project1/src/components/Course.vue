<template>

    <div>
        <!-- course
        <!-- <img src="../pic/2.jpg" alt=""> -->
        <!-- <ul v-for="row in courseList">
        <!-- <li><router-link :to="/detail">{{row.title}}</router-link></li> -->
        <!-- <li> -->
           <!-- {{row.id}} -->
            <!-- <img :src="row.pic_src" alt=""> -->
            <!-- <router-link :to="{path:'/detail',params:{id:row.id}}">{{row.title}}</router-link> -->
            <!-- <router-link :to="{name:'detail',params:{id:row.id}}">{{row.title}}</router-link> -->
        <!-- </li> -->
        <!-- </ul> -->

        <div v-for="row in courseList">
            <div style="width: 350px;float: left">

        <h3><router-link :to="{name:'detail',params:{id:row.id}}">{{row.title}}</router-link></h3>
        <p>{{row.level}}</p>
      </div>
    </div>
        <router-view></router-view>
    </div>
</template>



<script>

export default{
    name:'course',
    data(){
        return{
            courseList:[],
        }
    },
    mounted:function(){
        this.get_courselist()
    },
    methods:{
        get_courselist(){
            var that = this
            this.$axios.request({
                url:'http://127.0.0.1:8000/collegeAPI/v1/course/',
                method:'GET'
            }).then(function(ret){
                if(ret.data.code===1000){
                    that.courseList = ret.data.data
                }
            }).catch(function(ret){

            })
        }
    }
}

</script>


 
<style>

</style>
