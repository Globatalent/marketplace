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
                <el-option v-for="(code, index) in Object.keys(citi).filter(country => false === ['UM', 'AS', 'VI', 'US'].includes(country))" :key="index" :label="citi[code]" :value="code">
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
      citi: {
  "AX": "Alandic",
  "AL": "Albanian",
  "DZ": "Algerian",
  "AD": "Andorran",
  "AO": "Angolan",
  "AI": "Anguillian",
  "AQ": "Antarctic",
  "AG": "Antiguan Barbudan",
  "AR": "Argentinian",
  "AM": "Armenian",
  "AW": "Aruban",
  "AU": "Australian",
  "AT": "Austrian",
  "AZ": "Azerbaijani",
  "BS": "Bahamian",
  "BH": "	Bahraini",
  "BD": "Bangladeshi",
  "BB": "Barbadian",
  "BY": "Belarusian",
  "BE": "Belgian",
  "BZ": "Belizean",
  "BJ": "Beninese",
  "BM": "Bermudian",
  "BT": "Bhutanese",
  "BO": "Bolivian",
  "BQ": "Bonaire, Saint Eustatius and Saba ",
  "BW": "Motswana",
  "BR": "Brazilian",
  "VG": "Virgin Islander",
  "BN": "Bruneian",
  "BG": "Bulgarian",
  "BF": "Burkinabé",
  "BI": "Burundian",
  "KH": "Cambodian",
  "CM": "Cameroonian",
  "CA": "Canadian",
  "CV": "Cape Verdean",
  "CF": "Central African",
  "TD": "Chadian",
  "CL": "Chilean",
  "CN": "Chinese",
  "CX": "Christmas Islander",
  "CC": "Australian",
  "CO": "Colombian",
  "KM": "	Comorian",
  "CK": "Cook Islander",
  "CR": "Costa Rican",
  "HR": "Croatian",
  "CY": "Cypriot",
  "CZ": "Czech",
  "CD": "Congolese",
  "DK": "Danish",
  "DJ": "Djiboutian",
  "DO": "Dominican",
  "TL": "Timorese",
  "EC": "Ecuadorian",
  "EG": "Egyptian",
  "SV": "Salvadoran",
  "GQ": "Equatorial Guinean",
  "ER": "Eritrean",
  "EE": "Estonian",
  "FK": "Falkland Islander",
  "FO": "Faroese",
  "FJ": "Fijian",
  "FI": "Finn",
  "FR": "French",
  "GF": "French Guianese",
  "PF": "French Polynesian",
  "GA": "Gabonese",
  "GM": "Gambian",
  "GE": "Georgian",
  "DE": "German",
  "GH": "Ghanaian",
  "GI": "Gibraltarian",
  "GR": "Greek",
  "GL": "Greenlander",
  "GD": "Grenadian",
  "GU": "Guamanian",
  "GT": "Guatemalan",
  "GN": "Guinean",
  "GW": "	Bissau-Guinean",
  "GY": "Guyanese",
  "HT": "Haitin",
  "HN": "Honduran",
  "HK": "Hong Kongese",
  "HU": "Hungarian",
  "IS": "Icelander",
  "IN": "Indian",
  "ID": "Indonesian",
  "IE": "Irish",
  "IM": "Manx",
  "IL": "Israeli",
  "IT": "Italian",
  "CI": "Ivorian",
  "JM": "Jamaican",
  "JP": "Japanese",
  "JE": "Jersey",
  "JO": "Jordanian",
  "KZ": "Kazakhstani",
  "KE": "Kenyan",
  "KI": "I-Kiribati",
  "XK": "Kosovan",
  "KW": "Kuwaiti",
  "KG": "Kyrgyzstani",
  "LA": "Lao",
  "LV": "Latvian",
  "LB": "Lebanese",
  "LS": "Mosotho",
  "LR": "Liberian",
  "LY": "Libyan",
  "LI": "	Liechtensteiner",
  "LT": "Lithuanian",
  "LU": "	Luxembourgish",
  "MO": "Macanese",
  "MK": "Macedonin",
  "MG": "	Malagasy",
  "MW": "Malawian",
  "MY": "Malaysian",
  "MV": "Maldivian",
  "ML": "Malian",
  "MT": "Maltese",
  "MH": "Marshallese",
  "MR": "Mauritanian",
  "MU": "Mauritian",
  "MX": "Mexican",
  "FM": "Micronesian",
  "MD": "Moldovan",
  "MC": "Monacan",
  "MN": "Mongolian",
  "ME": "Montenegrin",
  "MS": "Montserratian",
  "MA": "Moroccan",
  "MZ": "Mozambican",
  "MM": "Burmese",
  "NA": "Namibian",
  "NR": "Nauruan",
  "NP": "Nepalese",
  "NL": "Dutch",
  "NZ": "New Zealander",
  "NI": "Nicaraguan",
  "NE": "Nigerien",
  "NG": "Nigerian",
  "NU": "Niuean",
  "NF": "Norfolk Islander",
  "MP": "Northern Mariana Islander",
  "NO": "Norwegian",
  "OM": "Omani",
  "PW": "	Palauan",
  "PS": "Palestinian",
  "PA": "Panamanian",
  "PG": "Papua New Guinean",
  "PY": "Paraguayan",
  "PE": "Peruvian",
  "PH": "Filipino",
  "PN": "Pitcairn Islander",
  "PL": "Polish",
  "PT": "Portuguese",
  "PR": "Puerto Rican",
  "QA": "Qatari",
  "CG": "Congolese",
  "RO": "Romanian",
  "RU": "Russian",
  "SH": "Saint Helenian",
  "KN": "Nevisian",
  "LC": "Saint Lucian",
  "VC": "Vincentian",
  "WS": "Samoan",
  "SM": "Sammarinese",
  "ST": "São Toméan",
  "SA": "Saudi Arabian",
  "SN": "Senegalese",
  "RS": "Serbian",
  "SC": "Seychellois",
  "SL": "Sierra Leonean",
  "SG": "Singaporean",
  "SX": "St. Maartener",
  "SK": "Slovakian",
  "SI": "Slovenian",
  "SB": "Solomon Islander",
  "SO": "Somalian",
  "ZA": "South African",
  "GS": "South Georgian",
  "KR": "South Korean",
  "SS": "South Sudanese",
  "ES": "Spanish",
  "SD": "Sudanese",
  "SR": "Surinamese",
  "SZ": "Swazi",
  "SE": "Swedish",
  "CH": "Swiss",
  "TW": "Taiwanese",
  "TJ": "Tajikistani",
  "TZ": "Tanzanian",
  "TH": "Thai",
  "TG": "Togolese",
  "TK": "Tokelauan",
  "TO": "Tongan",
  "TR": "Turkish",
  "TM": "Turkmen",
  "TC": "Turks and Caicos Islander",
  "TV": "Tuvaluan",
  "UA": "Ukranian",
  "AE": "Emirati",
  "GB": "British",
  "UY": "Uruguay",
  "UZ": "Uzbekistan",
  "VU": "Vanuatu",
  "VA": "Vatican",
  "VN": "Vietnam",
  "WF": "Wallis and Futuna",
  "EH": "Western Sahara",
},
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

          this.$store
            .dispatch('auth/register', dataForm)
            .then(data => {
          formToSend.append('xnQsjsdp','26ded01eee3cbb74693abaeee34e2f8acbb50ca314ea68813ba8b57665b4dc48');  
          formToSend.append('zc_gad','');
          formToSend.append('xmIwtLD','902ae1508809b664f4a8880feb72264315a8f92dcadde00bd65c96b2b9cbbafb');
          formToSend.append('actionType', 'Q29udGFjdHM=');
          formToSend.append('returnURL','https&#x3a;&#x2f;&#x2f;market.globatalent.com');
          formToSend.append('First Name', dataForm.firstName);
          formToSend.append('Last Name', dataForm.lastName);
          formToSend.append('Date of Birth', (dataForm.birthDate.getMonth() + 1).toString().padStart(2, 0) + '/' + dataForm.birthDate.getDate().toString().padStart(2, 0) + '/' + dataForm.birthDate.getFullYear().toString());
          formToSend.append('Email', dataForm.email);
          formToSend.append('Mailing Country', dataForm.country); 
          formToSend.append('Other Country', dataForm.citizenship);
          formToSend.append('CONTACTCF6', 'B2C');
          if (this.$route.query.utm_source !== undefined) {
            formToSend.append('Lead Source', 'Affiliate&#x20;Network');
            formToSend.append('CONTACTCF10', this.$route.query.utm_source ); //AFFILIATE NETWORK
            formToSend.append('CONTACTCF1', this.$route.query.utm_campaign ); //CAMPAIGN
          }

          const request = new XMLHttpRequest();
          request.open("POST", "https://crm.zoho.com/crm/WebToContactForm");
          request.send(formToSend);

          if (this.$route.query.utm_source !== undefined) {
          if (this.$route.query.utm_source.toLowerCase() === "biggico") {
            this.axios.get('https://biggi.co/api/v4/trackconversion/SVQVDZPxbg/?clickId=' + this.$route.query.click_id )
          }
          else if (this.$route.query.utm_source.toLowerCase() === "futmondo") {
            this.axios.get('https://beta.futmondo.com/mondos/globatalent/grant?user_id=' + this.$route.query.user_id + '&utm_campaign=' + this.$route.query.utm_campaign)
          }
          else if (this.$route.query.utm_source.toLowerCase() === "basketmondo") {
            this.axios.get('https://beta.basketmondo.com/mondos/globatalent/grant?user_id=' + this.$route.query.user_id + '&utm_campaign=' + this.$route.query.utm_campaign)
          }
          }
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
