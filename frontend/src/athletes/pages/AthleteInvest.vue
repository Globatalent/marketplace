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
                  <el-form-item required prop="amount">
                    <el-input v-bind:placeholder="$tc('message.Quantity')" type="number" v-model="form.amount" min="0">
                      <template slot="append">GBT</template>
                    </el-input>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-row>
                <el-col :xs="24" :sm="12">
                  <el-form-item class="text-center">
                    <el-button type="primary" class="is-uppercase" @click.prevent="goBack()">&lt; {{ $tc("message.Back") }}</el-button>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12">
                  <el-form-item class="text-center">
                    <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc("message.Invest") }}</el-button>
                  </el-form-item>
                </el-col>
              </el-row>
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
import router from '@/router.js'

export default {
  name: 'AthleteInvest',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      token: {},
      form: {
        amount: 0
      },
      rules: {
        amount: [
          {
            required: true,
            message: 'Please input quantity',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  computed: {
    ...mapGetters({
      athlete: 'athletes/athlete',
      user: 'users/user'
    })
  },
  created() {
    const id = this.$route.params.athleteId
    this.$store.dispatch('athletes/fetch', id).then(() => {
      this.token = this.athlete.token ? this.athlete.token : {}
    })
  },
  methods: {
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = {
            token: this.athlete.token.id,
            ...this.form,
          }
          this.saveInvest(dataForm)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    saveInvest(data) {
      this.$store
        .dispatch('tokens/purchase', data)
        .then(response => {
        })
        .catch(error => {})
    },
    goBack(){
      router.go(-1)
    }
  }
}
</script>

<style scoped>
@import '../../scss/variables.scss';
</style>
