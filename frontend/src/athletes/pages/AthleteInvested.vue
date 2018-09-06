<template>
  <gb-base-layout>
    <div class="container">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
          <h2 class="form-lined-title">Invested on {{athlete.firstName}} {{athlete.lastName}}</h2>
          <div class="form-lined">
            <el-row :gutter="20">
              <el-col :xs="24" class="text-left">
                <p>Thank you for your interest in the athlete {{athlete.firstName}} {{athlete.lastName}}.</p>
                <p>To complete your investment make a transfer of "xxx" Globatokens within 24 hours to the address:</p>
                <p class="text-center">3BXbD7LJmScJrV6GaSMfus4uGmsKw8jZyD</p>
                <img src="~@/assets/img/frame.png" class="qrImage">
              </el-col>
            </el-row>
            <el-row>
              <el-col :xs="24">
                <el-button type="primary" class="is-uppercase" @click.prevent="goClose()">{{ $tc("message.Close") }}</el-button>
              </el-col>
            </el-row>
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
  name: 'AthleteInvested',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters({
      athlete: 'athletes/athlete',
      purchase: 'tokens/purchase',
      user: 'users/user'
    })
  },
  created() {
    const id = this.$route.params.purchaseId
    this.$store.dispatch('tokens/fetchPurchase', id)
  },
  methods: {
    goClose() {
      router.push({ name: 'athlete.list' })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../scss/variables.scss';
.qrImage{
  max-width: 250px;
  margin: 0 auto 20px auto;
}
</style>
