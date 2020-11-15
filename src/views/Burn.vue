<template>
  <div class="starter-template">
    <div class="container">
      <div class="secret">
        <h2 class="pretext">Секрет: {{ secretId }}</h2>
      </div>
      <router-link class="btn btn-danger btn-block" to=""
        >Подтвердить: сжечь этот секрет</router-link
      >
      <router-link
        class="btn btn-outline-secondary btn-block"
        :to="getPrivateUrl()"
        >Отмена</router-link
      >
    </div>
    <hr>
    <p class="text-secondary">Секрет сжигается навсегда, и не может быть востановлен</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      secretId: location.pathname.replace("/burn/", ""),
    };
  },
  methods: {
    getPrivateUrl() {
      return "/private/" + this.secretId;
    },
  },
};
</script>

<style>
</style>