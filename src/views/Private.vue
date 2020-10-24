<template>
  <div class="starter-template">
    <h1 @click="getSecret">Узнать секрет</h1>
    <span>
      {{ secretData.secret }}
      <hr />
    </span>
    <router-link to="/">Создать новый секрет</router-link>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      secretId: this.$route.params.id,
      secretData: {},
    };
  },
  methods: {
    getSecret() {
      axios
        .get(`/api/v1/secrets/${this.secretId}`)
        .then((response) => {
          this.secretData = { ...response.data };
          console.log(this.secretData);
          console.log(response);
          this.deleteSecret(console.log("Удаляю секрет"));
        })
        .catch((error) => console.log(error));
    },
    deleteSecret() {},
    test() {
      console.log(this.$route);
      console.log(this.secretId);
    },
  },
};
</script>

<style>
</style>