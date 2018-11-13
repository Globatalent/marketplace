<template>
  <el-row :gutter="50">
    <el-col :xs="24" :md="8" :id="id" class="campaignDetails-infoContainer-data-title text-right">
      {{ title }}
    </el-col>
    <el-col :xs="24" :md="16" class="campaignDetails-infoContainer-data-text">
      <slot></slot>
      <span class="line"></span>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'CampaignInfoRow',
    props: {
      id: {
        required: false,
        type: String
      },
      title: {
        type: String
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import '../../scss/variables.scss';

  .campaignDetails-infoContainer-data-title {
    color: black;
    font-size: 20px;
    line-height: 25px;
    font-family: 'OpenSans Regular';
  }

  .campaignDetails-infoContainer-data-text {
    font-size: 14px;
    color: $--grey-text;
    font-family: 'OpenSans Regular';
    margin-bottom: 40px;
    .line {
      margin-top: 20px;
      display: block;
      width: 100%;
      max-width: 400px;
      border-top: 1px solid $--grey-detailCampaign-border;
    }
    &.is-last-block {
      max-width: 383px;
    }
  }
</style>
