<template>
    <div>
        <h1>课程详细</h1>
        <p><b>{{detial.course_name}}</b>
            <span>{{detial.course_level}}</span>
        </p>
        <p>{{detial.slogen}}</p>
        <p>{{detial.reason}}</p>
        <p>{{detial.describe}}</p>
        
        <div>
            <p>课程章节:</p>
            <ul>
                <li v-for="item in detial.chapters">
                    <p><b>{{item.num}}</b>{{item.name}}</p>

                </li>
            </ul>
        </div>

        <div>
            <p>推荐:</p>
            <ul>
                <li v-for="item in detial.recommendation">
                    <a @click="to_newdcourse(item.id)"><p>{{item.title}}</p></a>
                </li>
            </ul>
        </div>
    </div>

</template>



<script>

export default{
    name:'coursedetial',
    data(){
        return{
            detial:''
        }
    },
    mounted:function(){
        var nid = this.$route.params.id
        this.show_datas(nid)
    },
    methods:{
        show_datas(nid){           
            var that = this
            this.$axios.request({
                url:'http://localhost:8000/collegeAPI/v1/course/'+nid+'/',
                methods:'GET'
            }).then(function(args){
                if(args.data.code === 1000){
                    that.detial = args.data.data
                }else{
                    alert(args.data.errorMessage)
                }
            }).catch(function (ret) {
                
            })
        },
        to_newdcourse(args){
            this.show_datas(args)
            //改变
            this.$router.push({name:'detail',params:{id:args}})
        }
    }
}

</script>



<style>

</style>
