<template>
    <div >
        <div v-if="status">
            <h1>课程详细</h1>
            <p><b>{{detial.name}}</b>
                <span>{{detial.level}}</span>
            </p>
            <img :src="course_img" alt="图片暂时无法加载">
            <p>{{detial.course_slogan}}</p>
            <p>{{detial.video_brief_link}}</p>
            <p>{{detial.why_study}}</p>
            <p>{{detial.what_to_study_brief}}</p>
            <p>{{detial.career_improvement}}</p>
            
            <div>
                <p>课程章节:</p>
                <ul>
                    <li v-for="item in detial.coursechapter">
                        <p><b>{{item.chapter}}</b>{{item.name}}</p>

                    </li>
                </ul>
            </div>

            <div>
                <p>推荐:</p>
                <ul>
                    <!-- <li v-for="item in detial.recommendation">
                        <a @click="to_newdcourse(item.id)"><p>{{item.title}}</p></a>
                    </li> -->
                </ul>
            </div>
        </div>

        <div v-else>
            <h1>-{{detial}}-</h1>
        </div>

    </div>

    

</template>



<script>

export default{
    name:'coursedetial',
    data(){
        return{
            status:true,
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
                url:'http://localhost:8000/courseAPI/v1/coursedetial/'+nid+'/',
                methods:'GET'
            }).then(function(args){
                if(args.data.code === 1000){
                    that.detial = args.data.data
                }else{
                    that.status=false,
                    that.detial = args.data.error;
                    
                }
            }).catch(function (ret) {
                
            })
        },
        course_img(){

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
