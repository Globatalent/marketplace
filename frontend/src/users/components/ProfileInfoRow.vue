<template>
  <el-row :gutter="10">
    <el-col :md="8" class="text-right"><strong>{{ fieldName }}</strong></el-col>
    <el-col :md="16" class="text-left">{{ value }}</el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'ProfileInfoRow',
    props: ['fieldName', 'value']
  }
</script>

<style scoped>
 strong {
   font-weight: bold;
 }
</style>
