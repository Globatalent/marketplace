<template>
  <div class="footer">
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center">
        <div class="copy">Copyright Ⓒ 2018 Globatalent</div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'gb-footer'
}
</script>

<style lang="scss" scoped>
.footer {
  padding: 20px;
  margin-top: 20px;
  border-top: 1px solid #ccc;
  box-shadow: 0px 2px 10px 3px #ccc;
}
</style>
