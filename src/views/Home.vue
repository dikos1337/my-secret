<template>
  <div class="home">
    <main role="home" class="container">
      <div class="starter-template">
        <h3>Вставьте пароль, тайное сообщение или частную ссылку ниже.</h3>
        <Form @secret-id="getSecretId" @set-modal-state="setModalState" />
      </div>
      <Modal v-bind:secretId="secretId" v-bind:modalState="modalState" @set-modal-state="setModalState"/>
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
      modalState: false,
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
    setModalState(state){
      this.modalState = state
    }
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