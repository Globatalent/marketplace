<template>
  <div class="header">
    <el-row type="flex" justify="left">
      <el-col :xs="24" class="menuContainer">
        <a href="/">
          <img class="logoHeader" src="@/assets/img/logo-header.png" style="max-width: 240px;" />
        </a>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router>
          <!-- <el-menu-item index="home" :route="{path: '/'}">{{ $tc("message.Home") }}</el-menu-item> -->
          <el-menu-item index="campaigns" :route="{name:'campaign.list'}">{{ $tc("message.Campaign",2) }}</el-menu-item>
          <el-menu-item index="news" :route="{name:'news'}">{{ $tc("message.News") }}</el-menu-item>
          <el-menu-item index="faq" :route="{name:'faq'}">{{ $tc("message.Faq") }}</el-menu-item>
        </el-menu>
        <el-menu :default-active="activeIndex" class="el-menu-right" mode="horizontal" router>
          <!-- <el-select v-model="$i18n.locale">
            <el-option v-for="(lang, i) in langs" :key="`Lang${i}`" :value="lang">{{ lang }}</el-option>
          </el-select> -->
          <el-submenu index="3" v-if="!!user">
            <template slot="title">{{email()}}</template>
            <el-menu-item index="campaign.create" :route="{name: 'campaign.create'}">{{ $tc("message.CreateCampaign") }}</el-menu-item>
            <el-menu-item index="profile" :route="{name: 'profile'}">{{ $tc("message.Profile") }}</el-menu-item>
            <el-menu-item class="el-menu-item" index="" @click="logout()">{{ $tc('message.Logout') }}</el-menu-item>
          </el-submenu>
          <el-menu-item class="el-menu-item" index="login" :route="{name:'login'}" v-else>{{ $tc("message.SignIn") }}</el-menu-item>
          <el-menu-item class="el-menu-item" index="registration" :route="{name:'registration'}" v-if="!user">
            <span class="btn">{{ $tc("message.SignUp") }}</span></el-menu-item>
          <el-menu-item class="el-menu-item" index="notifications" :route="{name:'notifications'}" v-if="!!user">
            <el-badge :value="unread" :max="99" class="item" v-if="unread > 0">
              <el-button size="small" icon="el-icon-bell" circle></el-button>
            </el-badge>
            <el-button size="small" icon="el-icon-bell" circle v-else></el-button>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import router from '@/router.js'
import { mapGetters } from 'vuex'
import VueI18n from 'vue-i18n'

export default {
  name: 'gb-header',
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      langs: ['en', 'es']
    }
  },
  computed: {
    ...mapGetters({
      user: 'users/user',
      unread: 'actions/unread'
    })
  },
  created() {
    if (!!this.user) {
      this.$store.dispatch('actions/unread')
    }
  },
  components: {},
  methods: {
    email() {
      return !!this.user ? this.user.email : null
    },
    logout() {
      this.$confirm('Are you sure you want to log out?', 'Warning', {
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel',
        type: 'warning'
      })
        .then(() => {
          this.$store.dispatch('auth/logout').then(() => {
            router.push({ name: 'campaign.list' })
          })
          this.$message({
            type: 'success',
            message: 'Logout completed'
          })
        })
        .catch(error => {
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
  margin-bottom: 20px;
  padding: 20px 20px;
}
.logoHeader {
  max-width: 200px;
  margin: 0 auto;
  display: inline-block;
  vertical-align: bottom;
}

.el-menu--horizontal {
  display: inline-block;
  width: auto;
  border: none;
}
.el-menu-demo,
.el-menu-right {
  font-family: 'OpenSans SemiBold';
  font-size: 16px;
  color: #888893;
}
.el-menu-demo {
  margin-left: 20px;
}
.el-menu-right {
  float: right;
  .el-select {
    float: left;
  }
}

.el-menu-item {
  &:hover,
  &.is-active {
    color: #2b7cba !important;
  }
}

@media (min-width: 768px) {
  .logoHeader {
    margin: 0;
  }
  .el-menu--horizontal {
    position: relative;
    top: 15px;
  }
}
</style>
