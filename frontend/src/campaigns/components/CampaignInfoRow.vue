<template>
  <el-row>
    <el-col :xs="24" :md="8" :id="id" class="campaignDetails-infoContainer-data-title">
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
    font-family: 'Aller Regular';
  }

  .campaignDetails-infoContainer-data-text {
    font-size: 14px;
    color: $--grey-text;
    font-family: 'Aller Regular';
    margin-bottom: 40px;
    .line {
      display: block;
      width: 75%;
      border-top: 1px solid $--grey-detailCampaign-border;
      margin: auto;
    }
    &.is-last-block {
      max-width: 383px;
    }
  }
</style>
