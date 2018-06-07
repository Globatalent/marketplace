<template>
    <el-container class="main-container">
        <el-main class="is-vertical-center">
            <slot></slot>
        </el-main>
    </el-container>
</template>

<script>

  export default {
    name: 'minimal-layout',

    data () {
      return {}
    },

    computed: {},

    mounted: function () {
    },

    methods: {},
    components: {
    },
  }
</script>

<style type="scss" scoped>
    .main-container {
        height: 100%;
    }
</style>
