<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png" width="25%"> -->
    <Header />
    <Main />
    <!-- <Footer /> -->
  </div>
</template>

<script>
import Header from "./components/Header";
import Main from "./components/Main";
// import Footer from "./components/Footer";

export default {
  name: "App",
  components: {
    Header,
    Main,
    // Footer,
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
</style>
