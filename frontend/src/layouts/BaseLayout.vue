<template>
    <el-container class="main-container">
        <el-header height="auto">
            <gb-header></gb-header>
        </el-header>
        <el-main>
            <slot></slot>
        </el-main>
        <el-footer>
            <gb-footer></gb-footer>
        </el-footer>
    </el-container>
</template>

<script>
  import Header from '@/components/Header.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    /**
     * The name of the layout.
     */
    name: 'base-layout',

    data () {
      return {}
    },

    computed: {},

    mounted: function () {
    },

    methods: {},
    components: {
      'gb-header': Header,
      'gb-footer': Footer,
    },
  }
</script>

<style type="scss" scoped>
    .main-container {
        height: 100%;
    }

    .el-header {
        padding: 0;
    }
    .el-footer {
        padding: 0;
    }
</style>
