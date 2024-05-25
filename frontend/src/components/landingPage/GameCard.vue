<script>
import { joinGame } from '@/logic/token';
export default {
  props: ['name', 'playerCount', 'dimensions', "gameId"],
  data() {
    return {
      isPopupVisible: false,
      formData: {
        username: ''
      }
    }
  },
  methods: {
    showPopup() {
      this.isPopupVisible = true;
    },
    closePopup() {
      this.formData.username = '';
      this.isPopupVisible = false;
    },
    joinGame() {
      console.log(this.formData);
      console.log(this.gameId);
      // TODO: check if username is already used 
      joinGame(this.gameId, this.formData.username, () => {
        this.$router.push('/lobby/' + this.gameId);
      });
      this.closePopup();

    }
  }
}
</script>
<template>
  <div class="card">
    <md-elevation></md-elevation>
    <h4 class="name md-typescale-title-large">{{ name }}</h4>
    <p class="info md-typescale-label-medium">{{ playerCount }} Player · {{ dimensions }}x{{ dimensions }}</p>
    <md-filled-button class="button" @click="showPopup">Join</md-filled-button>
  </div>

  <div v-if="isPopupVisible" class="popup">
    <form @game.prevent="joinGame" class="dialog">
      <h2 class="dialog-title">Join Game</h2>

      <div class="dialog-content">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="formData.username" required />
      </div>

      <div class="dialog-actions">
        <button type="submit" class="mdc-button mdc-button--raised" @click.prevent="joinGame">Join Game</button>
        <button type="button" class="mdc-button mdc-button--outlined" @click="closePopup">Close</button>
      </div>
    </form>
  </div>

</template>
<style scoped>
.card {
  position: relative;
  width: calc(200px - 24px);
  height: calc(200px - 24px);
  padding: 12px;
  border-radius: 12px;
  background-color: var(--md-sys-color-surface-container-highest);
  --md-elevation-level: 1;
}

.name,
.info {
  margin: 0;
}

.button {
  position: absolute;
  bottom: 12px;
  right: 12px;
}

.popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.3);
  z-index: 1000;
}

.dialog {
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}

.dialog-title {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 24px;
  text-align: center;
}

.dialog-content label {
  display: block;
  margin-top: 8px;
}

.dialog-content input,
.dialog-content select {
  width: calc(100% - 24px);
  margin: 8px 0;
  padding: 8px 12px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.dialog-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 24px;
}

.mdc-button {
  font-size: 14px;
  padding: 0 16px;
  line-height: 36px;
  border-radius: 4px;
  text-transform: uppercase;
}

.mdc-button--raised {
  background-color: #6200ea;
  color: white;
  margin-right: 8px;
}

.mdc-button--outlined {
  border: 1px solid #6200ea;
  color: #6200ea;
}
</style>
