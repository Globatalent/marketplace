<template>
  <div class="footer">

    <el-row class="el-row--flex" type="flex" justify="center" :gutter="15">
      <el-col class="text-center">
        <h4>{{ $t("message.Social") }}</h4>
        <p>{{ $t("message.JoinOurConv") }}</p>
        <ul class="socialList">
          <li class="socialList-item">
            <a href="https://www.facebook.com/globatalent.official" target="_blank" class="socialList-item-link"><img src="~@/assets/img/facebook-icon.png" alt="" class="socialList-item-link-icon"></a>
          </li>
          <li class="socialList-item">
            <a href="https://twitter.com/globatalent" target="_blank" class="socialList-item-link"><img src="~@/assets/img/twitter-icon.png" alt="" class="socialList-item-link-icon"></a>
          </li>
          <li class="socialList-item">
            <a href="https://instagram.com/globatalent" class="socialList-item-link" target="_blank" style="width:14px"><img src="~@/assets/img/icon-instagram.png" style="width:14px" alt="" class="socialList-item-link-icon"></a>
          </li>
          <li class="socialList-item">
            <a href="https://t.me/globatalent" class="socialList-item-link" target="_blank" style="width:14px"><img src="~@/assets/img/icon-telegram.png" style="width:14px" alt="" class="socialList-item-link-icon"></a>
          </li>
        </ul>
      </el-col>
      <el-col>
        <h4>{{ $t("message.About") }}</h4>
        <p>{{ $t("message.AboutTxt") }}</p>
      </el-col>
      <el-col>
      <h4>Contact us</h4>
      <p>
        You can contact us <a href="https://web.globatalent.com/contact/">here</a>.You can also reach us at <a href="tel:+44 (0)20 7504 1304">+44 (0)20 7504 1304</a> and <a href="mailto:contact@globatalent.com">contact@globatalent.com</a>
      </p>
      </el-col>
      <el-col>
        <h4>{{ $t("message.Location") }}</h4>
        <address>
        <p>
          {{ $t("message.London") }}
          <br>
          <small>{{ $t("message.LondonAdd") }}</small>
        </p>
        </address>
        <p>{{ $t("message.BuenosAires") }}</p>
        <address>
        <p>
          {{ $t("message.HongKong") }}
          <br>
          <small>{{ $t("message.HongKongAdd") }}</small>
        </p>
        </address>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center subscribeCol">
        <div class="subscribe-text">{{ $t("message.SubscribeToUs") }}</div>
        <div class="subscribeBox">
          <input class="subscribeBox-input" type="text" :placeholder="$t('message.InputEmail')">
          <button class="subscribeBox-button">{{ $t("message.SignUp") }}</button>
        </div>
      </el-col>
      <el-col class="text-center">
      <img class="subscribe-image" src="~@/assets/img/etherum-foundation.png" />
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center footerBottom">
        <el-row>
        <a class="copy" href="/privacy"> {{ $t("message.privacy") }}</a>
        <a class="copy" href="/terms"> {{ $t("message.terms") }}</a>
        <a class="copy" href="/risks"> {{ $t("message.risk") }}</a>
        <div class="copy">Ⓒ {{ $t("message.AllRightsReserved") }}</div>

        </el-row>
        <el-row>
        <div class="copy">{{$t("message.incorporation")}}</div>
        </el-row>
      </el-col>
    </el-row>
    <cookie-law>
      <div slot="message">
        {{ $t("message.cookiesAd") }} <router-link to="legal-notes">{{ $t("message.cookiesLink") }}</router-link>
      </div>
    </cookie-law>
  </div>
</template>

<script>
import VueI18n from 'vue-i18n'
import CookieLaw from 'vue-cookie-law'
export default {
  name: 'gb-footer',
  components: { CookieLaw }
}
</script>

<style lang="scss" scoped>
@import '../scss/variables.scss';
.footer {
  padding: 20px;
  margin-top: 20px;
  background: $--black;
  color: $--grey;
  font-family: 'Aller Regular';
}
.logoFooter {
  width: 100%;
  height: auto;
  max-width: 226px;
  margin: 20px auto;
}
.footerMenu{
  margin-bottom: 20px;
}
.el-menu-demo {
  background: transparent;
  width: auto;
  display: inline-block;
  &.el-menu--horizontal {
    border: none;
  }
  .el-menu-demo-item {
    color: white;
    text-transform: uppercase;
    font-family: 'Aller Bold';
  }
}
.subscribeCol {
  margin-bottom: 20px;
}
.subscribe-text {
  display: inline-block;
  text-transform: uppercase;
  font-size: 18px;
  font-family: 'Aller Bold';
}
.subscribeBox {
  display: inline-block;
  margin: 0 20px;
  font-size: 0;
}
.subscribeBox-input {
  border: none;
  display: inline-block;
  font-size: 11px;
  color: $--grey;
  width: 225px;
  height: 40px;
  padding-left: 10px;
  position: relative;
  top: 1px;
  &::placeholder {
    text-transform: uppercase;
  }
}
.subscribeBox-button {
  background: $--blue;
  color: white;
  text-transform: uppercase;
  font-size: 12px;
  font-family: 'Aller Bold';
  border: none;
  height: 40px;
  width: 100px;
}
.subscribe-image {
  display: inline-block;
  width: 100%;
  max-width: 115px;
  margin-left: 20px;
}
.el-menu-footer-bottom {
  background: transparent;
  width: auto;
  display: inline-block;
  &.el-menu--horizontal {
    border: none;
    .el-menu-footer-bottom-item{
      font-size: 11px;
      font-family: 'Aller Bold';
      height: auto;
      line-height: inherit;
      border: none;
      text-transform: uppercase;
    }
  }
}
.socialList{
  margin: 0;
  padding: 0;
  list-style: none;
  width: auto;
  display: inline-block;
}
.socialList-item{
  display: inline-block;
  margin: 0 10px;
}
.contact-form {
  width: 100%;
}
.contact-form label {
  width: 100px;
  text-align: left;
}
.contact-form label span {
  color: #f00;
}
.contact-form input[type="text"] {
  width: 100%;
  max-width: 200px;
}
.copy{
  display: inline-block;
  margin-left: 20px;
  font-size: 14px;
}
.footerBottom{
  margin: 15px 0;
}
@media only screen and (max-width: 768px) {
  .el-row--flex {
    display: block;
  }
  .el-col {
    float: none;
    text-align: center;
    margin-bottom: 20px;
  }
}
</style>
