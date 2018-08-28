<template>
  <div class="header">
    <el-row justify="left">
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="4" class="text-center">
        <img class="logoHeader" src="~@/assets/img/Globatalent-logo-vert.png" />
      </el-col>
      <el-col :xs="24" :sm="12" :md="16" :lg="18" :xl="20" class="menuContainer">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router>
          <!-- <el-menu-item index="home" :route="{path: '/'}">{{ $tc("message.Home") }}</el-menu-item> -->
          <el-menu-item index="athletes" :route="{name:'athlete.list'}">{{ $tc("message.Athlete",2) }}</el-menu-item>
          <el-submenu index="3">
            <template slot="title">{{email()}}</template>
            <el-menu-item v-if="isAthlete()" index="athlete-profile" :route="{name:'athlete.profile'}">{{ $tc("message.Profile") }}</el-menu-item>
            <el-menu-item v-if="isSupporter()" index="supporter-profile" :route="{name:'supporter.profile'}">{{ $tc("message.Profile") }}</el-menu-item>
            <el-menu-item class="el-menu-item" index="logout" @click="logout()">{{ $tc('message.Logout') }}</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import router from '@/router.js'
import { mapGetters } from 'vuex'

export default {
  name: 'gb-header',
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  computed: {
    ...mapGetters({
      user: 'users/user'
    })
  },
  components: {},
  methods: {
    handleSelect(key, keyPath) {
      console.log('key', key)
      console.log('keyPath', keyPath)
    },
    email() {
      return !!this.user ? this.user.email : null
    },
    isAthlete() {
      return !!this.user ? !!this.user.athlete : false
    },
    isSupporter() {
      return !!this.user ? !!this.user.supporter : false
    },
    logout() {
      this.$confirm('Are you sure you want to log out?', 'Warning', {
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel',
        type: 'warning'
      })
        .then(() => {
          this.$store.dispatch('auth/logout').then(()=>{
            router.push({ name: 'login' })
          })
          this.$message({
            type: 'success',
            message: 'Logout completed'
          })
        })
        .catch(error => {
          debugger
          this.$message({
            type: 'info',
            message: 'Logout canceled'
          })
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  padding: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  box-shadow: 0px 2px 10px 3px #ccc;
}
.logoHeader {
  max-width: 200px;
  margin: 0 auto;
}
.menuContainer {
  text-align: center;
}
.el-menu--horizontal {
  display: inline-block;
  width: auto;
  border: none;
}

@media (min-width: 768px) {
  .logoHeader {
    margin: 0;
  }
  .menuContainer {
    text-align: right;
  }
  .el-menu--horizontal {
    position: relative;
    top: 15px;
  }
}
</style>
