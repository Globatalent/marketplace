<template>
  <gb-base-layout>
    <div class="container">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
          <h2 class="form-lined-title">Invest on {{athlete.firstName}} {{athlete.lastName}}</h2>
          <div class="form-lined">
            <el-form ref="form" label-position="top" class="text-left" :model="form" :rules="rules">
              <el-row :gutter="20">
                <el-col :xs="24">
                  <el-form-item required prop="quantity">
                    <el-input v-bind:placeholder="$tc('message.Quantity')" type="number" v-model="form.quantity" min="0"></el-input>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-form-item class="text-center">
                <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc("message.Invest") }}</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-col>
      </el-row>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'AthleteInvest',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      token: {},
      form: {
        quantity: 0
      },
      rules: {
        quantity: [
          {
            required: true,
            message: 'Please input quantity',
            trigger: 'blur'
          }
        ],
      },
    }
  },
  computed: {
    ...mapGetters({
      athlete: 'athletes/athlete',
      user: 'users/user'
    }),
    progress() {
      if (!!this.token) {
        return Math.round(this.token.progression * 100)
      }
      return 0
    }
  },
  created() {
    const id = this.$route.params.athleteId
    this.$store.dispatch('athletes/fetch', id).then(() => {
      this.token = this.athlete.token ? this.athlete.token : {}
    })
  },
  methods: {
    isSupporter() {
      return !!this.user && !!this.user.supporter
    },
    collected() {
      if (!!this.token) {
        return (this.token.amount - this.token.remaining) * this.token.unitPrice
      }
      return 0
    },
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = Object.assign({}, this.form)
          this.saveInvest(dataForm)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    saveInvest(data) {
      console.log('Saving invest ...');

      // this.$store
      //   .dispatch('athletes/update', data)
      //   .then(response => {

      //   })
      //   .catch(error => {})
    },
  }
}
</script>

<style scoped>
@import '../../scss/variables.scss';
</style>
