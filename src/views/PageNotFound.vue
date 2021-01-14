<template>
  <div class="container">
    <router-link class="error404" to="/">404</router-link>
  </div>
</template>

<style scoped>
.error404 {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 50vmin;
  letter-spacing: 0px;
  line-height: 0;
  opacity: 0.9;
  font-weight: 900;
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  color: rgba(0, 0, 0, 1);
  transition: 750ms ease-in-out;
  -webkit-transform: translate(-50%, -50%) rotate(-10deg);
  transform: translate(-50%, -50%) rotate(-10deg);
  text-shadow: 2vmin 2vmin #ff4655, 3vmin 3vmin #000000;
  animation: colorrr 10s infinite;
}
.error404:hover {
  text-decoration: none;
}

@keyframes colorrr {
  0% {
    filter: hue-rotate(0deg);
  }
  50% {
    filter: hue-rotate(360deg);
  }
}
</style>