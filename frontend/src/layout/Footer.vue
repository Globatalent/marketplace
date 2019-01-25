<template>
  <div class="footer">

    <el-row class="el-row--flex" type="flex" justify="center" gutter="15">
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
        <div id='crmWebToEntityForm'>
          <META HTTP-EQUIV ='content-type' CONTENT='text/html;charset=UTF-8'/>
          <form action='https://crm.zoho.com/crm/WebToLeadForm' name=WebToLeads3718183000000307001 method='POST' onSubmit='javascript:document.charset="UTF-8";' accept-charset='UTF-8'>
            <!-- Do not remove this code. -->
            <input type='text' style='display:none;' name='xnQsjsdp' value='26ded01eee3cbb74693abaeee34e2f8acbb50ca314ea68813ba8b57665b4dc48'/>
            <input type='hidden' name='zc_gad' id='zc_gad' value=''/>
            <input type='text' style='display:none;' name='xmIwtLD' value='902ae1508809b664f4a8880feb722643fe2db5ba1a2f62a32a61306421cf8410'/>
            <input type='text' style='display:none;'  name='actionType' value='TGVhZHM='/>
            <input type='text' style='display:none;' name='returnURL' value='https://market.globatalent.com' /> 
            <!-- Do not remove this code. -->

            <div class="contact-form">
              <div>
                <label>Fist Name<span>*</span></label>
                <input type='text' maxlength='40' name='First Name' />
              </div>
              <div>
                <label>Last Name<span>*</span></label>
                <input type='text' maxlength='80' name='Last Name' />
              </div>
              <div>
                <label>Email<span>*</span></label>
                <input type='text' maxlength='100' name='Email' />
              </div>
              <div>
                <label>Comments<span>*</span></label>
                <textarea name='Description' maxlength='32000'>&nbsp;</textarea>
              </div>
              <div>
                <input style='font-size:12px;color:black'  type='submit' value='Submit' />
                <input  type='reset' style='font-size:12px;color:black' value='Reset' />
              </div>
            </div>

          </form>
        </div>
      </el-col>
      <el-col>
        <h4>{{ $t("message.Location") }}</h4>
        <p>{{ $t("message.London") }}</p>
        <p>{{ $t("message.BuenosAires") }}</p>
        <address>
          <p>{{ $t("message.HongKong") }}</p>
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
        <div class="copy">Ⓒ {{ $t("message.AllRightsReserved") }}</div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import VueI18n from 'vue-i18n'
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
