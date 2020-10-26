<template>
  <form
    id="createSecret"
    method="post"
    autocomplete="off"
    action="/"
    @submit.prevent="onSubmit"
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
            name="lifetime"
            class="form-control"
            v-model.trim="form.lifetime"
            :class="{
              'is-invalid':
                $v.form.lifetime.$dirty && !$v.form.lifetime.required,
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
import axios from "axios";

export default {
  name: "Form",
  data() {
    return {
      form: {
        secret: "",
        passphrase: "",
        lifetime: "300.0",
      },
    };
  },
  validations: {
    form: {
      secret: { required },
      passphrase: { required },
      lifetime: { required },
    },
  },
  methods: {
    onSubmit() {
      if (!this.$v.$invalid) {
        axios
          .post(
            "/api/v1/secrets",
            { ...this.form },
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          )
          .then((response) => {
            this.$emit("secret-id", response.data.id); // Прокидываю id выше
            this.$emit("set-modal-state", true); // Открываю модалку
          })
          .catch((error) => console.log(error)); // сюда можно флаг для текста модалки прокинуть ок или нет
                                                 // и установить флаг чистить ли текст в формах, при ошибке не чистить
        // Очищаю форму
        this.$v.$reset();
        this.form.secret = this.form.passphrase = "";
      } else {
        this.$v.$touch();
        return;
      }
    },
  },
};
</script>