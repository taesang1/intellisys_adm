import { createWebHistory, createRouter } from 'vue-router'
import blog_write from './page/blog_write.vue'
import blog_list from './page/blog_list.vue'

const routes = [
    {
        path: '/',
        name: 'root',
        component: blog_list
    },
    {
        path: '/blog_list',
        name: 'blog_list',
        component: blog_list
    },
    {
        path: '/blog_write',
        name: 'blog_write',
        component: blog_write
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router