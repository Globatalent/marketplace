<template>
  <el-col :xs="24">
    <h2 class="form-lined-title text-center">{{ $tc("message.Funding") }}</h2>
    <div class="form-lined">
        <el-form-item :label="$tc('message.FundsRequirement')">
          <el-input type="text" v-model="form.funds"></el-input>
            <el-select v-model="form.currency" placeholder="Select">
              <el-option
                v-for="item in currencies"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
        </el-form-item>
        <el-form-item :label="$tc('message.HowYouUseFunds')">
          <el-input type="text" v-model="form.use"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.GiveBack')">
          <el-input type="text" v-model="form.giveBack"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.RevenueFor')">
          <div v-for="(revenue, index) in form.revenues" :key="index">
            {{ revenue.year }}
            <el-input type="text"  v-model="revenue.amount"></el-input>
            <el-select v-model="revenue.currency" placeholder="Select">
              <el-option
                v-for="item in currencies"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
        </el-form-item>
        <el-form-item :label="$tc('message.IncomeFor')">
          <div v-for="(income, index) in form.incomes" :key="index">
            {{ income.year }}
            <el-input type="text"  v-model="income.amount"></el-input>
            <el-select v-model="income.currency" placeholder="Select">
              <el-option
                v-for="item in currencies"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
        </el-form-item>
        <el-form-item :label="$tc('message.Examples')">
          <el-input type="text" v-model="form.examples"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Recommendations')">
        <el-upload
            :action="options.action"
            :name="options.name"
            :headers="options.headers"
            :data="options.data"
            :file-list="form.recommendations">
            <el-button size="small" type="primary">Upload</el-button>
          </el-upload>
        </el-form-item>
    </div>
    <el-form-item>
      <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{ $tc("message.SaveContinute") }}</el-button>
    </el-form-item>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'


export default {
  name: 'Funding',
  components: {
  },
  data() {
    return {
      // Form
      currencies: [{value: "USD", label: "USD"}],
      form: {
        currency: "USD",
        funds: null,
        use: null,
        giveBack: null,
        revenues: [],
        incomes: [],
        examples: null,
        recommendations: [],
      },
      options: {
        action: `${Vue.axios.defaults.baseURL}/api/v1/recommendations/`,
        name: 'file',
        headers: {
          Authorization: this.$store.getters['auth/header'],
        },
      }
    }
  },
  computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
      user: 'users/user'
    })
  },
  created() {
    this.$store.dispatch('campaigns/fetch', this.$route.params.campaignId).then( () => {
      if (!!this.campaign && !!this.campaign.id) {
        this.options.data = {
          campaign: this.campaign.id
        }
        this.form = { ... this.campaign }
        this.form.recommendations = this.campaign.recommendations.map( (recomendation) => {

          return {name: recomendation.file.substring(recomendation.file.lastIndexOf('/') + 1), url: recomendation.file}
        })
        this.form.revenues = this.initialRevenues(this.campaign)
        this.form.incomes = this.initialIncomes(this.campaign)
        if (!this.form.currency) {
          this.form.currency = "USD"
        }
      }
    })
  },
  methods: {
      initialRevenues(campaign) {
        const currentYear = new Date().getFullYear()
        const initialRevenues = [...Array(3).keys()].map( diff => {
          return {
            id: null,
            campaign: this.campaign.id,
            year: currentYear - diff,
            amount: null,
            currency: "USD",
          }
        })
        return initialRevenues.map( revenue => {
          const revenues = campaign.revenues.filter( item => item.year == revenue.year)
          if ( revenues.length > 0 ) return revenues[0]
          return revenue
        })
      },
      initialIncomes(campaign) {
        const currentYear = new Date().getFullYear()
        const initialIncomes = [...Array(5).keys()].map( diff => {
          return {
            id: null,
            campaign: this.campaign.id,
            year: currentYear + diff + 1,
            amount: null,
            currency: "USD",
          }
        })
        return initialIncomes.map( income => {
          const incomes = campaign.incomes.filter( item => item.year == income.year)
          if ( incomes.length > 0 ) return incomes[0]
          return income
        })
      },
      onSaveAndContinue() {
        const payload = {
          id: this.campaign.id,
          currency: this.form.currency,
          funds: this.form.funds,
          use: this.form.use,
          giveBack: this.form.giveBack,
          revenues: this.form.revenues,
          incomes: this.form.incomes,
          examples: this.form.examples,
        }
        this.$store.dispatch('campaigns/update', payload)
      }
  }
}
</script>

<style type="scss" scoped>
</style>
