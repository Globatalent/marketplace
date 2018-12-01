<template>
  <div class="footer">
    <el-row type="flex" justify="center">
      <el-col class="text-center">
      <h4>Social</h4>
      <p>Join our conversations.</p>
              <ul class="socialList">
          <li class="socialList-item">
            <a href="https://www.facebook.com/globatalent.official" target="_blank" class="socialList-item-link"><img src="~@/assets/img/facebook-icon.png" alt="" class="socialList-item-link-icon"></a>
          </li>
          <li class="socialList-item">
            <a href="https://twitter.com/globatalent" target="_blank" class="socialList-item-link"><img src="~@/assets/img/twitter-icon.png" alt="" class="socialList-item-link-icon"></a>
          </li>
          <li class="socialList-item">
            <a href="" class="socialList-item-link"><img src="~@/assets/img/pinterest-icon.png" alt="" class="socialList-item-link-icon"></a>
          </li>
        </ul>
      </el-col>
      <el-col>
      <h4>About</h4>
      <p>Globatalent is the the first sports crypto exchange where you can tokenize, trade and support your favorite clubs and sports idols.</p>
      </el-col>
      <el-col>
      <h4>Location</h4>
      <p>London</p>
      <p>Buenos aires</p>
      <address>
      <p>Hong Kong</p>
      <p>1/F Knowles Building, HKU, Pokfulam Road, Hong Kong</p>
      </address>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center subscribeCol">
        <div class="subscribe-text">{{ $tc("message.SubscribeToUs") }}</div>
        <div class="subscribeBox">
          <input class="subscribeBox-input" type="text" :placeholder="$tc('message.InputEmail')">
          <button class="subscribeBox-button">{{ $tc("message.SignUp") }}</button>
        </div>
      </el-col>
      <el-col class="text-center">
      <img class="subscribe-image" src="~@/assets/img/etherum-foundation.png" />
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center footerBottom">
        <div class="copy">Ⓒ All rights reserved 2018.</div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'gb-footer'
}
</script>

<style lang="scss" scoped>
@import '../scss/variables.scss';
.footer {
  padding: 20px;
  margin-top: 20px;
  background: $--black;
  color: $--grey;
  font-family: 'OpenSans Regular';
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
    font-family: 'OpenSans Bold';
  }
}
.subscribeCol {
  margin-bottom: 20px;
}
.subscribe-text {
  display: inline-block;
  text-transform: uppercase;
  font-size: 18px;
  font-family: 'OpenSans Bold';
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
  font-family: 'OpenSans SemiBold';
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
      font-family: 'OpenSans SemiBold';
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
.copy{
  display: inline-block;
  margin-left: 20px;
  font-size: 14px;
}
.footerBottom{
  margin: 15px 0;
}
</style>
