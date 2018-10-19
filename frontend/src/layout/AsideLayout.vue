<template>
  <el-container class="main-container aside-container">
    <el-header height="auto">
      <gb-header></gb-header>
    </el-header>
    <el-container>
      <el-aside width="230px">
        <el-menu default-active="4" class="el-menu-aside" :default-openeds="['4']" :router="true">
          <!-- <el-menu-item index="1">
            <span>Campaign title</span>
          </el-menu-item>
          <el-menu-item index="2">
            <span>Preview campaign</span>
          </el-menu-item>
          <el-menu-item index="3">
            <span>Pre-Launch Page</span>
          </el-menu-item> -->
          <el-submenu index="4">
            <template slot="title">
              <span>Campaign Editor</span>
            </template>
            <el-menu-item index="card">Card Campaign</el-menu-item>
            <el-menu-item index="content">Content</el-menu-item>
            <el-menu-item index="career" v-if="campaign.kind == 'athlete'">Career</el-menu-item>
            <el-menu-item index="career" v-else>Club</el-menu-item>
            <el-menu-item index="funding">Funding</el-menu-item>
          </el-submenu>
          <!-- <el-submenu index="5">
            <template slot="title">
              <span>Resources</span>
            </template>
            <el-menu-item index="5-1">Education Center</el-menu-item>
            <el-menu-item index="5-2">Experts Directory</el-menu-item>
          </el-submenu> -->
        </el-menu>
      </el-aside>
      <el-main :class="$route.params.step">
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
import { mapGetters } from 'vuex'


export default {
  name: 'aside-layout',
  data() {
    return {}
  },
  computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
      user: 'users/user'
    })
  },
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
