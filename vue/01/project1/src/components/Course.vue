<template>

    <div>

        <div v-for="row in courseList" >
            <div style="width: 350px;float: left;margin-top:100px">
                <img :src="row.course_img" alt="图片暂时无法加载">
                <h3>
                    <router-link :to="{name:'detail',params:{id:row.id}}">{{row.name}}</router-link>
                </h3>
                <span>{{row.level}}</span>
                <div>
                    <span>{{row.beief}}</span>
                </div>

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
                url:'http://127.0.0.1:8000/courseAPI/v1/course/',
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
