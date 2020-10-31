<template>
  <div class="starter-template">
    <div class="container">
      <h3>Поделиться этой ссылкой:</h3>
      <br />
      <input
        class="form-control"
        id="readOnlyInput"
        v-bind:value="getUrl()"
        readonly="readonly"
      />

      <div class="secret">
        <em>Тайна (iqsrhg):</em>
        <span class="form-text text-muted"
          >(вы увидете его только один раз)</span
        ><br />
        <textarea class="form-control" readonly="readonly" rows="3">
Вставьте пароль, тайное сообщение или частную ссылку ниже.
Не пропускайте чувствительную информацию в беседы и э-почту.</textarea
        >
      </div>

      <p>
        <strong>Истекает через 7 days</strong>.
        <span class="form-text text-muted">(2020-10-29@12:06:30 UTC)</span>
      </p>

      <hr />
      <a class="btn btn-danger btn-block" :href="getBurnUrl()"
        ><i class="icon-fire"></i> Сжечь эту тайну*</a
      >

      <hr />
      <p class="hint">
        * Сожжение тайны удалит её до прочтения (щёлкните здесь, чтоыб
        подтвердить).
      </p>

      <hr />
      <p class="">
        <a class="btn btn-outline-secondary btn-block" href="/"
          >Создать другой секрет</a
        >
      </p>
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
    };
  },
  methods: {
    getUrl() {
      return location.href.replace("/private/", "/secret/");
    },
    getBurnUrl() {
      return location.href + "/burn";
    },
    getSecret() {
      axios
        .get(`/api/v1/secret/${this.secretId}`)
        .then((response) => {
          this.secretData = { ...response.data };
          this.deleteSecret(response.data.id);
        })
        .catch((error) => console.log(error));
    },
    deleteSecret(secretId) {
      console.log(`Удаляю секрет с id: ${secretId}`);
    },
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