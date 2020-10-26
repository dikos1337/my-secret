<template>
  <div class="home">
    <!-- <h1>{{ msg }}</h1> -->
    <main role="home" class="container">
      <div class="starter-template">
        <h3>Вставьте пароль, тайное сообщение или частную ссылку ниже.</h3>
        <Form @secret-id="getSecretId" />
      </div>
      <Modal v-bind:secretId="secretId" />
    </main>
  </div>
</template>

<script>
import Form from "@/components/Form";
import Modal from "@/components/Modal";

export default {
  name: "Home",
  data() {
    return {
      secretId: "",
    };
  },
  components: {
    Form,
    Modal,
  },
  methods: {
    getSecretId(secretId) {
      this.secretId = secretId;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
/* body {
  padding-top: 5rem;
} */
.starter-template {
  padding: 1rem 1.5rem;
  text-align: center;
}

h3 {
  /* font-family: "Roboto"; */
  font-weight: 700;
}
</style>