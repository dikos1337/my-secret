<template>
  <div class="starter-template">
    <div class="container">
      <div v-if="!secretIsUnavailable">
        <div class="secret">
          <h2 class="pretext">Секрет: {{ secretId }}</h2>
        </div>
        <div v-if="passphraseRequired" class="form-group">
          <input
            class="form-control"
            type="text"
            name="passphrase"
            id="passphraseField"
            value=""
            placeholder="Введите фразу-пропуск"
            autocomplete="off"
            v-model.trim="form.passphrase"
            :class="{
              'is-invalid': passphraseIsWrong,
            }"
          />
          <small class="invalid-feedback">Неверный пароль.</small>
        </div>
        <button class="btn btn-danger btn-block" @click="burnSecret">
          Подтвердить: сжечь этот секрет
        </button>
        <router-link
          class="btn btn-outline-secondary btn-block"
          :to="getPrivateUrl()"
          >Отмена</router-link
        >
        <hr />
        <p class="text-secondary">
          Секрет сжигается навсегда, и не может быть востановлен
        </p>
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
      passphraseRequired: false,
      form: {
        passphrase: "",
      },
    };
  },
  mounted() {
    axios
      .get(`/api/v1/check/${this.secretId}`)
      .then((response) => {
        this.secretData = response.data;
        if (this.secretData.passphrase) {
          this.passphraseRequired = true;
        }
      })
      .catch(() => {
        this.secretIsUnavailable = true;
      });
  },
  methods: {
    getPrivateUrl() {
      return "/private/" + this.secretId;
    },
    burnSecret() {
      axios({
        method: "DELETE",
        url: `/api/v1/secret/${this.secretId}`,
        data: { ...this.form, id: this.secretId },
      })
        .then(() => {
          window.location.href = "/"; // Редирект на главную
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
</style>