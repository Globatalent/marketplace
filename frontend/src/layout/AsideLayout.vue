<template>
  <el-container class="main-container">
    <el-header height="auto">
      <gb-header></gb-header>
    </el-header>
    <el-container>
      <el-aside width="230px">
        <el-menu default-active="4" class="el-menu-aside">
          <el-menu-item index="1">
            <span>Campaign title</span>
          </el-menu-item>
          <el-menu-item index="2">
            <span>Preview campaign</span>
          </el-menu-item>
          <el-menu-item index="3">
            <span>Pre-Launch Page</span>
          </el-menu-item>
          <el-submenu index="4">
            <template slot="title">
              <span>Campaign Editor</span>
            </template>
            <el-menu-item index="4-1">Card Campaign</el-menu-item>
            <el-menu-item index="4-2">Content</el-menu-item>
            <el-menu-item index="4-3">Career</el-menu-item>
            <el-menu-item index="4-4">Funding</el-menu-item>
          </el-submenu>
          <el-submenu index="5">
            <template slot="title">
              <span>Resources</span>
            </template>
            <el-menu-item index="5-1">Education Center</el-menu-item>
            <el-menu-item index="5-2">Experts Directory</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <slot></slot>
      </el-main>
    </el-container>
    <el-footer>
      <gb-footer></gb-footer>
    </el-footer>
  </el-container>
</template>

<script>
import Header from '@/layout/Header.vue'
import Footer from '@/layout/Footer.vue'

export default {
  name: 'aside-layout',

  data() {
    return {}
  },

  computed: {},

  mounted: function() {},

  methods: {},
  components: {
    'gb-header': Header,
    'gb-footer': Footer
  }
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
