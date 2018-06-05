<template>
    <div>
        <p><input type="text" placeholder="用户名" v-model="username"></p>
        <p><input type="password" placeholder="密码" v-model="password"></p>
        <input type="submit" value="提交" @click="doregister">
    </div>
</template>



<script>
export default{
    data(){
        return{
            username:'',
            password:'',
        }
    },
    methods:{
        
        doregister(){
            var that= this
            // console.log(123)
            this.$axios.request({
                url:'http://localhost:8000/courseAPI/v1/resiger/',
                method:'POST',
                data:{
                    user:this.username,
                    pwd:this.password
                },
                headers:{
                    "Content-Type":'application/json'
                }
            }).then(function(args){
                if(args.data.code ===1000){
                    that.$store.state.token = args.data.token
                    that.$store.state.username = that.username
                    that.$store.commit('savetoken',{tonk})
                }else{
                    alert(args.data.error)
                }
            }).catch(function(args){
                
            })
        }
    }
}

</script>



<style>

</style>
