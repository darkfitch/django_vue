import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Homesite from '@/components/Homesite'
import Luffy_degree from '@/components/Luffy_degree'
import Course from '@/components/Course'
import CourseDetial from '@/components/CourseDetial'
import login from '@/components/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Homesite',
      component: Homesite
    },
    {
      path:'/course',
      name:'Course',
      component:Course
    },
    {
      path:'/detail/:id',
      name:'detail',
      component:CourseDetial
    },
    {
      path:'/degree',
      name:'Luffy_degree',
      component:Luffy_degree
    },
    {
      path:'/login',
      name:'login',
      component:login
    }
  ],
  mode:'history'
})
