<template>
  <div class="starter-template">
    <div class="container">
      <div v-if="!secretIsUnavailable">
        <h3>Поделиться этой ссылкой:</h3>
        <input
          class="form-control"
          id="readOnlyInput"
          v-bind:value="getUrl()"
          readonly="readonly"
        />

        <div class="secret">
          <em>Тайна:</em>
          <span class="form-text text-muted"
            >(вы увидете его только один раз)</span
          ><br />
          <textarea
            class="form-control"
            readonly="readonly"
            rows="3"
            v-model="secretData.secret"
          ></textarea>
        </div>

        <p>
          <strong>Истекает через {{ secretData.lifetime }} секунд</strong>.
          <span class="form-text text-muted">{{ calculateExpiryDate() }}</span>
        </p>

        <hr />
        <router-link class="btn btn-danger btn-block" :to="getBurnUrl()"
          >Сжечь эту тайну*</router-link
        >

        <hr />
        <p class="hint">
          * Сожжение тайны удалит её до прочтения (щёлкните здесь, чтоыб
          подтвердить).
        </p>
        <hr />

        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Создать новый секрет</router-link
        >
      </div>
      <div v-else>
        <h2>Секрет либо никогда не существовал, либо он уже был просмотрен.</h2>
        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Создать новый секрет</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      secretId: this.$route.params.id,
      secretData: {},
      secretIsUnavailable: false,
    };
  },
  mounted() {
    axios
      .get(`/api/v1/private/${this.secretId}`)
      .then((privatekResponse) => {
        this.secretData = privatekResponse.data;
      })
      .catch(() => {
        this.secretIsUnavailable = true;
      });
  },
  methods: {
    getUrl() {
      return location.origin + /secret/ + this.secretData.id;
    },
    getBurnUrl() {
      return "/burn/" + this.secretData.id;
    },
    getSecret() {
      axios
        .get(`/api/v1/secrets/${this.secretId}`)
        .then((response) => {
          this.secretData = { ...response.data };
          this.deleteSecret(response.data.id);
        })
        .catch((error) => console.log(error));
    },
    calculateExpiryDate() {
      let created_date = new Date(this.secretData.created_date);
      let lifetime = this.secretData.lifetime;
      created_date.setSeconds(created_date.getSeconds() + lifetime);
      return created_date.toLocaleString();
    },
    // deleteSecret(secretId) {
    //   console.log(`Удаляю секрет с id: ${secretId}`);
    // },
  },
};
</script>

<style scoped>
.form-text {
  display: inline;

  margin: 0.2rem;
}

.starter-template {
  text-align: left;
}
</style>