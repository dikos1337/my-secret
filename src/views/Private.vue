<template>
  <div class="app-template">
    <div class="container">
      <div v-if="!secretIsUnavailable">
        <h3>Поделиться этой ссылкой:</h3>
        <div class="input-group">
          <input
            class="form-control"
            id="readOnlyInput"
            v-bind:value="getUrl()"
            readonly="readonly"
          />
          <div class="input-group-append">
            <button class="btn btn-success" @click="copyToClipboard">
              Copy
            </button>
          </div>
        </div>
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
          <span class="form-text text-muted">{{
            new Date(secretData.expiration_date).toLocaleString()
          }}</span>
        </p>

        <hr />
        <router-link class="btn btn-danger btn-block" :to="getBurnUrl()"
          >Сжечь эту тайну*</router-link
        >

        <hr />
        <p class="hint">* Сожжение тайны удалит её до прочтения.</p>
        <hr />

        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Создать новый секрет</router-link
        >
      </div>
      <div v-else>
        <NotFoundMessage />
        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Создать новый секрет</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NotFoundMessage from "@/components/NotFoundMessage";

export default {
  components: {
    NotFoundMessage,
  },
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
        })
        .catch((error) => console.log(error));
    },
    copyToClipboard() {
      navigator.clipboard.writeText(this.getUrl());
    },
  },
};
</script>

<style scoped>
.app-template {
  text-align: left;
}
p {
  margin-top: 0.2rem;
  margin-bottom: 0rem;
}
hr {
  margin-top: 0.2rem;
  margin-bottom: 0.5rem;
}
.btn {
  margin-bottom: 0.5rem;
}
</style>
