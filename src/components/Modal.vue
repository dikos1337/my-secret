<template>
  <div>
    <div v-if="modalState">
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Секрет успешно создан!</h5>
                  <button
                    type="button"
                    class="close"
                    data-dismiss="modal"
                    aria-label="Close"
                  >
                    <span aria-hidden="true" @click="$emit('set-modal-state',false)"
                      >&times;</span
                    >
                  </button>
                </div>
                <div class="modal-body">
                  <p>Поделиться этой ссылкой:</p>
                  <input class="form-control" type="text" :value="makeUrl()" />
                  <p>
                    <a :href="makeUrl()">{{ makeUrl() }}</a>
                  </p>
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-secondary"
                    @click="$emit('set-modal-state',false)"
                  >
                    Закрыть
                  </button>
                  <button type="button" class="btn btn-primary">
                    Скопировать ссылку
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
    <!-- <button @click="$emit('set-modal-state',true)">Click</button> -->
  </div>
</template>

<script>
export default {
  name: "Modal",
  props: {
    secretId: String,
    modalState: Boolean,
  },
  methods: {
    makeUrl() {
      return location.href + "private/" + this.secretId;
    },
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
</style>