<template>
  <div class="home">
    <!-- <h1>{{ msg }}</h1> -->
    <main role="home" class="container">
      <div class="starter-template">
        <h3>Вставьте пароль, тайное сообщение или частную ссылку ниже.</h3>
        <Form @secret-id="testFunc" />
      </div>
    </main>
  </div>
</template>

<script>
import Form from "@/components/Form";
export default {
  name: "Home",
  components: {
    Form,
  },
  methods: {
    testFunc(id) {
      console.log(id);
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