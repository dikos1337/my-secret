<template>
  <div class="home">
    <main role="home" class="container">
      <div class="app-template">
        <h3>Вставьте пароль, тайное сообщение или частную ссылку ниже.</h3>
        <Form />
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
};
</script>
