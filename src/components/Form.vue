<template>
  <form
    id="createSecret"
    method="post"
    autocomplete="off"
    action="/"
    @submit.prevent="sendForm"
  >
    <fieldset>
      <div class="form-group">
        <textarea
          rows="5"
          class="form-control"
          name="secret"
          autocomplete="off"
          placeholder="Тайное содержимое вводится сюда..."
          v-model.trim="form.secret"
          :class="{
            'is-invalid': $v.form.secret.$dirty && !$v.form.secret.required,
          }"
        ></textarea>
        <small class="invalid-feedback">Введите сообщение.</small>
      </div>
      <div class="title">Настройки приватности</div>
      <div class="form-group">
        <label class="control-label lighter" for="passphraseField"
          >Фраза-пропуск:</label
        >
        <input
          class="form-control"
          type="text"
          name="passphrase"
          id="passphraseField"
          value=""
          placeholder="Слово или фраза, которую сложно угадать"
          autocomplete="off"
          v-model.trim="form.passphrase"
          :class="{
            'is-invalid':
              $v.form.passphrase.$dirty && !$v.form.passphrase.required,
          }"
        />
        <small class="invalid-feedback">Введите фразу-пропуск.</small>
      </div>
      <div class="form-group">
        <label class="control-label lighter" for="recipientField"
          >Lifetime:</label
        >
        <div class="form-group">
          <select
            name="ttl"
            class="form-control"
            v-model.trim="form.ttl"
            :class="{
              'is-invalid': $v.form.ttl.$dirty && !$v.form.ttl.required,
            }"
          >
            <option value="604800.0" selected="">7 days</option>
            <option value="259200.0">3 days</option>
            <option value="86400.0">1 day</option>
            <option value="43200.0">12 hours</option>
            <option value="14400.0">4 hours</option>
            <option value="3600.0">1 hour</option>
            <option value="1800.0">30 minutes</option>
            <option value="300.0">5 minutes</option>
          </select>
          <small class="invalid-feedback">Выберите lifetime.</small>
        </div>
      </div>
      <button
        class="btn btn-outline-secondary"
        type="submit"
        name="kind"
        value="share"
        :class="{
          disabled: !($v.form.secret.required && $v.form.passphrase.required),
        }"
      >
        Создать ссылку на тайну*
      </button>
    </fieldset>
    <hr />
    <p class="lead">
      * Ссылка на тайну работает только один раз, а затем навсегда исчезает.
    </p>
  </form>
</template>

<script>
import { required } from "vuelidate/lib/validators";
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
  validations: {
    form: {
      secret: { required },
      passphrase: { required },
      ttl: { required },
    },
  },
  methods: {
    sendForm() {
      if (!this.$v.$invalid) {
        console.log({ ...this.form, date: Date.now()}); // Это буду отправлять
        this.$v.$reset();
        this.form.secret = this.form.passphrase = ""; // Очищаю форму
      } else {
        this.$v.$touch();
        console.log("error");
        return;
      }
    },
  },
};
</script>