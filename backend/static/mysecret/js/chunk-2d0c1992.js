(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0c1992"],{4770:function(t,e,c){"use strict";c.r(e);var a=function(){var t=this,e=t.$createElement,c=t._self._c||e;return c("div",{staticClass:"starter-template"},[c("h1",{on:{click:t.getSecret}},[t._v("Узнать секрет")]),c("span",[t._v(" "+t._s(t.secretData.secret)+" "),c("hr")]),c("router-link",{attrs:{to:"/"}},[t._v("Создать новый секрет")])],1)},n=[],r=c("5530"),s=c("bc3a"),o=c.n(s),i={data:function(){return{secretId:this.$route.params.id,secretData:{}}},methods:{getSecret:function(){var t=this;o.a.get("/api/v1/secrets/".concat(this.secretId)).then((function(e){t.secretData=Object(r["a"])({},e.data),t.deleteSecret(e.data.id)})).catch((function(t){return console.log(t)}))},deleteSecret:function(t){console.log("Удаляю секрет с id: ".concat(t))}}},l=i,u=c("2877"),d=Object(u["a"])(l,a,n,!1,null,null,null);e["default"]=d.exports}}]);
//# sourceMappingURL=chunk-2d0c1992.js.map