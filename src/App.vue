<template>
  <div id="app">
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header";

export default {
  name: "App",
  components: {
    Header,
  },
};
</script>

<style>
#app {
  font-family: "Roboto", Arial, Helvetica, sans-serif;
  color: #343a40;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.app-template {
  padding: 1rem 1.5rem;
  text-align: center;
}
h3 {
  font-weight: 700;
}
.form-text {
  display: inline;
  margin: 0.2rem;
}
</style>
