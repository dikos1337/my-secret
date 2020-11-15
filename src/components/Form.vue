<template>
  <form id="createSecret" autocomplete="off" @submit.prevent="onSubmit">
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
        />
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
          disabled: !$v.form.secret.required,
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
      passphrase: {},
      lifetime: { required },
    },
  },
  methods: {
    onSubmit() {
      if (!this.$v.$invalid) {
        axios
          .post(
            "/api/v1/secret",
            { ...this.form },
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          )
          .then((response) => {
            window.location.href = `/private/${response.data.id}`; // Редирект на private view
          })
          .catch((error) => console.error(error));
      } else {
        this.$v.$touch();
        return;
      }
    },
  },
};
</script>