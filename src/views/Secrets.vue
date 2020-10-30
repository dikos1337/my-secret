<template>
  <div class="starter-template">
    <div class="container">
      <div v-if="!secretData.secret">
        <button class="btn btn-outline-secondary btn-block" @click="getSecret">
          Узнать секрет
        </button>
      </div>
      <div class="shared" v-else>
        <div class="secret">
          <h3>Это сообщение для вас:</h3>
          <textarea
            class="form-control"
            readonly="readonly"
            rows="4"
            v-model="secretData.secret"
          ></textarea>
          <p class="TODO">Осторожно: мы покажем это только один раз.</p>
        </div>
        <router-link class="btn btn-outline-secondary btn-block" to="/"
          >Ответить другим секретом</router-link
        >
      </div>
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
    };
  },
  methods: {
    getSecret() {
      axios
        .get(`/api/v1/secrets/${this.secretId}`)
        .then((getResponse) => {
          // // После получения ответа я отправляю запрос на удаление
          axios
            .delete(`/api/v1/secrets/${this.secretId}`)
            .then((deleteResponse) => {
              // И только уже после того как успешно удалиться я показываю секрет
              if (deleteResponse.status === 204) {
                this.secretData = { ...getResponse.data };
              }
              console.log(deleteResponse);
            });
        })
        .catch((error) => console.log(error));
    },
    deleteSecret(secretId) {
      console.log(`Удаляю секрет с id: ${secretId}`);
    },
  },
};
</script>

<style>
</style>