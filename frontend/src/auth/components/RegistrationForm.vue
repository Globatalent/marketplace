<template>
  <el-col class="text-center">
    <h2 class="form-lined-title">{{ $tc('message.RegisterNewUser') }}</h2>
    <div class="form-lined">
      <el-form ref="form" label-position="top" class="text-left" :model="form" :rules="rules">
        <el-row :gutter="20">
          <el-col :xs="24" :lg="12">
            <el-form-item required prop="firstName">
              <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
            </el-form-item>
            <el-form-item required prop="lastName">
              <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
            </el-form-item>
            <el-form-item required prop="country">
              <el-select v-model="form.country" filterable v-bind:placeholder="$tc('message.CountryResidence')">
                <el-option v-for="(code, index) in Object.keys(countries).filter(country => false === ['UM', 'AS', 'VI', 'US'].includes(country))" :key="index" :label="countries[code]" :value="code">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item required prop="citizenship">
              <!-- <el-input v-bind:placeholder="$tc('message.Citizenship')" type="text" v-model="form.citizenship"></el-input> -->
              <el-select v-model="form.citizenship" filterable v-bind:placeholder="$tc('message.Citizenship')">
                <el-option v-for="(code, index) in Object.keys(countries).filter(country => false === ['UM', 'AS', 'VI', 'US'].includes(country))" :key="index" :label="countries[code]" :value="code">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :lg="12">
            <el-form-item required prop="email">
              <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item required prop="birthDate">
              <el-date-picker v-bind:placeholder="$tc('message.DateFormat')" type="date" class="datepicker" v-model="form.birthDate"></el-date-picker>
            </el-form-item>
            <el-form-item required prop="password">
              <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item required prop="repeatPassword">
              <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="24">
            <el-form-item class="text-left" required prop="conditions" style="padding-bottom:20px;">
              <el-checkbox class="registrationForm-accept" v-model="form.conditions"><a href="/privacy" target="_blank">{{$tc('message.AcceptDataProtectionConditions')}}</a></el-checkbox>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item class="text-center">
          <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc('message.Register')}}
          </el-button>
        </el-form-item>
      </el-form>
      <el-row>
        <div class="form-reminderBlock text-center">{{ $tc('message.AlreadyAccount') }}
          <router-link :to="{ name: 'login'}" class="is-main-color">{{ $tc('message.LogIn') }}</router-link>
        </div>
      </el-row>
    </div>
    <p class="registrationForm-infoRegulations">{{$tc('message.DueToRegulations')}}</p>
  </el-col>
</template>

<script>
import router from '@/router.js'
import { Message } from 'element-ui'
import countries from '@/base/helpers/countries'

export default {
  name: 'RegistrationForm',
  components: {},
  data() {
    return {
      countries: countries,
      form: {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        repeatPassword: '',
        birthDate: '',
        country: '',
        citizenship: '',
        conditions: ''
      },
      rules: {
        email: [
          {
            required: true,
            message: 'Please enter a valid email',
            trigger: 'blur'
          },
          {
            type: 'email',
            message: 'Please enter a valid email',
            trigger: ['blur', 'change']
          }
        ],
        password: [{ validator: this.validatePass, trigger: 'change' }],
        repeatPassword: [{ validator: this.validatePass2, trigger: 'change' }],
        firstName: [
          {
            required: true,
            message: 'Please input first name',
            trigger: 'blur'
          }
        ],
        lastName: [
          { required: true, message: 'Please input last name', trigger: 'blur' }
        ],
        birthDate: [
          {
            required: true,
            message: 'Please select your birth date',
            trigger: 'blur'
          }
        ],
        country: [
          { required: true, message: 'Please input country', trigger: 'blur' }
        ],
        citizenship: [
          {
            required: true,
            message: 'Please input citizenship',
            trigger: 'blur'
          }
        ],
        conditions: [
          {
            required: true,
            message: 'Please accept the conditions',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  created() {
    // console.log(countries)
  },
  methods: {
    validatePass(rule, value, callback) {
      if (value === '') {
        callback(new Error('Please input the password'))
      } else {
        callback()
      }
    },
    validatePass2(rule, value, callback) {
      if (value === '') {
        callback(new Error('Please input the password again'))
      } else if (value !== this.form.password) {
        callback(new Error("Two inputs don't match!"))
      } else {
        callback()
      }
    },
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = Object.assign({}, this.form);
          const formToSend = new FormData();

          formToSend.append('xnQsjsdp','26ded01eee3cbb74693abaeee34e2f8acbb50ca314ea68813ba8b57665b4dc48');  
          formToSend.append('zc_gad','');
          formToSend.append('xmIwtLD','902ae1508809b664f4a8880feb72264315a8f92dcadde00bd65c96b2b9cbbafb');
          formToSend.append('actionType', 'Q29udGFjdHM=');
          formToSend.append('returnURL','https&#x3a;&#x2f;&#x2f;market.globatalent.com');
          formToSend.append('CONTACTCF1', this.$route.query.utm_campaign ); //CAMPAIGN
          formToSend.append('CONTACTCF2', this.$route.query.utm_source ); //AFFILIATE NETWORK
          formToSend.append('First Name', dataForm.firstName);
          formToSend.append('Last Name', dataForm.lastName);
          formToSend.append('Date of Birth', (dataForm.birthDate.getMonth() + 1).toString().padStart(2, 0) + '/' + dataForm.birthDate.getDate().toString().padStart(2, 0) + '/' + dataForm.birthDate.getFullYear().toString());
          formToSend.append('Email', dataForm.email);
          formToSend.append('Mailing Country', dataForm.country); 
          formToSend.append('Other Country', dataForm.citizenship);

          const request = new XMLHttpRequest();
          request.open("POST", "https://crm.zoho.com/crm/WebToContactForm");
          request.send(formToSend);

          console.log(this.$route.query.utm_source)
          console.log(this.$route.query.utm_campaign)

          if (this.$route.query.utm_source.toLowerCase() === "biggico") {
            this.axios.get('https://biggi.co/api/v4/trackconversion/SVQVDZPxbg/?clickId=' + this.$route.query.click_id )
          }
          else if (this.$route.query.utm_source.toLowerCase() === "futmondo") {
            this.axios.get('https://beta.futmondo.com/mondos/globatalent/grant?clickd_id=' + this.$route.query.click_id + '&utm_campaign=' + this.$route.query.utm_campaign)
          }

          this.$store
            .dispatch('auth/register', dataForm)
            .then(data => {
              router.push({ name: 'campaign.list' })
            })
            .catch(error => {
              if (!!error.response) {
                if (error.response.data.email) {
                  Message.error({
                    message: error.response.data.email[0],
                    center: true
                  })
                } else {
                  Message.error({
                    message: error.response.data.error,
                    center: true
                  })
                }
              } else {
                console.error(error)
              }
            })
        } else {
          console.error('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../scss/variables.scss';

.el-date-editor.el-input.datepicker {
  width: 100%;
}

.el-select {
  width: 100%;
}
.registrationForm-infoRegulations {
  margin-top: 5px;
  font-size: 9px;
  font-family: 'Aller Regular';
  color: $--grey-text;
}
.el-checkbox .el-checkbox__label {
  font-size: 12px;
}
</style>
