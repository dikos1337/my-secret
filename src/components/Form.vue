<template>
  <form
    id="createSecret"
    method="post"
    autocomplete="off"
    action="/"
    class="form-horizontal"
    @submit.prevent="sendForm"
  >
    <!-- <input
      type="hidden"
      name="shrimp"
      value="qw0vz81t43ziv07egotzrcjafsfzzf7285u75yqoddwpgyabm560v3ax1zdbdqryxaihdd72rnfjhrmdocz2ubysob1zmi6bm03"
    /> -->
    <fieldset>
      <div class="form-group">
        <textarea
          rows="7"
          class="form-control"
          name="secret"
          autocomplete="off"
          placeholder="Тайное содержимое вводится сюда..."
          v-model="form.secret"
        ></textarea>
        <!-- <div class="chars-display lightest"></div> -->
      </div>
      <!-- <div class="well options-box"> -->
      <div class="title">Настройки приватности</div>
      <div class="form-group">
        <label class="control-label lighter" for="passphraseField"
          >Фраза-пропуск:</label
        >
        <div class="controls">
          <input
            class="form-control"
            type="text"
            name="passphrase"
            id="passphraseField"
            value=""
            placeholder="Слово или фраза, которую сложно угадать"
            autocomplete="off"
            v-model="form.passphrase"
          />
        </div>
      </div>
      <div class="form-group">
        <label class="control-label lighter" for="recipientField"
          >Lifetime:</label
        >
        <div class="form-group">
          <select name="ttl" class="form-control" v-model="form.ttl">
            <option value="604800.0" selected="">7 days</option>
            <option value="259200.0">3 days</option>
            <option value="86400.0">1 day</option>
            <option value="43200.0">12 hours</option>
            <option value="14400.0">4 hours</option>
            <option value="3600.0">1 hour</option>
            <option value="1800.0">30 minutes</option>
            <option value="300.0">5 minutes</option>
          </select>
        </div>
      </div>
      <!-- </div> -->
      <button
        class="btn btn-outline-secondary"
        type="submit"
        name="kind"
        value="share"
      >
        Создать ссылку на тайну*
      </button>
      <!-- <button
              class="generate btn btn-large btn-block cufon"
              type="submit"
              name="kind"
              value="generate"
            >
              Или сгенинировать одноразовый пароль
            </button> -->
    </fieldset>
    <hr />
    <p class="lead">
      * Ссылка на тайну работает только один раз, а затем навсегда исчезает.
    </p>
  </form>
</template>

<script>
export default {
  name: "Form",
  data() {
    return {
      form: {
        secret: "",
        passphrase: "",
        ttl: "300.0",
      },
    };
  },
  methods: {
    validateData(form) {
      if (form.secret == "") {
        return false;
      } else if (form.passphrase == "") {
        return false;
      } else if (!Number(form.ttl)) {
        return false;
      } else {
        console.log("validating data");
        return true;
      }
    },
    sendForm() {
      if (this.validateData(this.form)) {
        console.log({ ...this.form, date: Date.now(), viewed: false }); // Это буду отправлять
        this.form.secret = this.form.passphrase = "";
      } else {
        console.log("error");
      }
    },
  },
};
</script>