<template>
    <div>
        <p><input type="text" placeholder="用户名"></p>
        <p><input type="password" placeholder="密码"></p>
        <input type="submit" value="提交">
    </div>
</template>



<script>

export default{
    name:'login',
    data(){
        return{
            username:'',
            password:''
        }
    },
    methods:{
        toLogin(){
            this.$axios.request({
                url:'',
                methods:'POST',
                data:{
                    user:this.username,
                    pwd:this.password
                },
                headers:{
                    "Content-Type":'application/json'
                }
            }).then(function(args){

            }).catch(function(args){
                
            })
        }
    }
}

</script>


<style>

</style>
