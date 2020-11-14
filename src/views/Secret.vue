<template>
  <div class="starter-template">
    <div class="container">
      <div v-if="passphraseRequired" class="form-group">
        <label class="control-label lighter" for="passphraseField"
          >Фраза-пропуск:</label
        >
        <input
          class="form-control"
          type="text"
          name="passphrase"
          id="passphraseField"
          value=""
          placeholder="Введите фразу-пропуск"
          autocomplete="off"
          v-model.trim="form.passphrase"
        />
      </div>

      <div v-if="secretData.secret" class="secret">
        <h3>Это сообщение для вас:</h3>
        <textarea
          class="form-control"
          readonly="readonly"
          rows="4"
          v-model="secretData.secret"
        ></textarea>
        <p class="TODO">Осторожно: мы покажем это только один раз.</p>
        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Ответить другим секретом</router-link
        >
      </div>
      <div v-if="secretIsUnavailable">
        <h2>Секрет либо никогда не существовал, либо он уже был просмотрен.</h2>
        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Создать новый секрет</router-link
        >
      </div>
      <button
        v-if="renderButtonRequired"
        class="btn btn-outline-secondary btn-block"
        @click="showSecretOneTime"
      >
        Узнать секрет
      </button>
    </div>
  </div>
</template>

<script>
// TODO короче мне надо на бекенде сделать метод который возвращает есть ли пароль у секрте и если такой секрет вообще, если есть пароль то вывожу форму если нет то просто кнопка узнать секрет
import axios from "axios";
export default {
  data() {
    return {
      secretId: this.$route.params.id,
      secretData: {},
      secretIsUnavailable: false,
      renderButtonRequired: true,
      passphraseRequired: undefined,
      form: {
        passphrase: "",
      },
    };
  },
  mounted() {
    axios
      .get(`/api/v1/check/${this.secretId}`)
      .then((checkResponse) => {
        if (checkResponse.data.passphrase) {
          this.passphraseRequired = true;
        }
      })
      .catch(() => {
        this.secretIsUnavailable = true;
        this.renderButtonRequired = false;
      });
  },
  methods: {
    showSecretOneTime() {
      axios
        .post(
          `/api/v1/secret/${this.secretId}`,
          { ...this.form, id: this.secretId },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((postResponse) => {
          axios({
            method: "DELETE",
            url: `/api/v1/secret/${this.secretId}`,
            data: { ...this.form, id: this.secretId },
          })
            .then((deleteResponse) => {
              // И только уже после того как успешно удалился я показываю секрет
              if (deleteResponse.status === 204) {
                this.secretData = { ...postResponse.data };
                this.renderButtonRequired = false;
                this.passphraseRequired = false;
              }
            })
            .catch((error) => console.log(error));
        })
        .catch((error) => {
          console.log(error);
          // Ставлю флаг в true чтоб отрендерить ошибку на фронте
          // this.secretIsUnavailable = true;
        });
      // }
    },
  },
};
</script>

<style>
</style>