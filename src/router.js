import Vue from "vue"
import Router from "vue-router"
import Home from "@/views/Home"

Vue.use(Router)

export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            component: Home
        },
        {
            path: "/secret/:id",
            component: () => import("./views/Secret.vue")
        },
        {
            path: "/private/:id",
            component: () => import("./views/Private.vue")
        },
        {
            path: "/burn/:id",
            component: () => import("./views/Burn.vue")
        }
    ]
})