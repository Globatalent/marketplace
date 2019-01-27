<template>
  <div class="header">
    <el-row type="flex" justify="left">
      <el-col :xs="24" class="menuContainer">
        <a href="/">
          <img class="logoHeader" src="@/assets/img/logo-header.png" />
        </a>
        <div id="menu" :class="{ active: isActive }">
          <el-menu @select="handleSelect" class="el-menu-demo" mode="horizontal" router>
            <!-- <el-menu-item index="home" :route="{path: '/'}">{{ $tc("message.Home") }}</el-menu-item> -->
            <el-menu-item index="campaigns" :route="{name:'campaign.list'}">{{ $tc("message.Campaign",2) }}</el-menu-item>
            <el-menu-item index="news" :route="{name:'news'}">{{ $tc("message.News") }}</el-menu-item>
            <el-menu-item index="faq" :route="{name:'faq'}">{{ $tc("message.Faq") }}</el-menu-item>
            <el-menu-item><a href="https://web.globatalent.com">{{ $tc("message.Corporate") }}</a></el-menu-item>
          </el-menu>  
          <el-menu class="el-menu-right" mode="horizontal" router>
            <el-menu-item class="el-menu-item lang-switcher">
              <el-select v-model="$i18n.locale">
                <el-option v-for="(lang, i) in langs" :key="`Lang${i}`" :value="lang.value">{{ lang.title }}</el-option>
              </el-select>
            </el-menu-item>
            <el-submenu class="submenu" index="3" v-if="!!user">
              <template slot="title">{{email()}}</template>
              <el-menu-item index="campaign.create" :route="{name: 'campaign.create'}">{{ $tc("message.CreateCampaign") }}</el-menu-item>
              <el-menu-item index="profile" :route="{name: 'profile'}">{{ $tc("message.Profile") }}</el-menu-item>
              <el-menu-item class="el-menu-item" index="" @click="logout()">{{ $tc('message.Logout') }}</el-menu-item>
            </el-submenu>
            <el-menu-item class="el-menu-item" index="login" :route="{name:'login'}" v-if="!user">{{ $tc("message.SignIn") }}</el-menu-item>
            <el-menu-item class="el-menu-item" index="registration" :route="{name:'registration'}" v-if="!user">
              <span class="btn">{{ $tc("message.SignUp") }}</span>
            </el-menu-item>
            <el-menu-item class="el-menu-item submenu-collapsed" index="campaign.create" :route="{name: 'campaign.create'}" v-if="!!user">{{ $tc("message.CreateCampaign") }}</el-menu-item>
            <el-menu-item class="el-menu-item submenu-collapsed" index="profile" :route="{name: 'profile'}" v-if="!!user">{{ $tc("message.Profile") }}</el-menu-item>
            <el-menu-item class="el-menu-item submenu-collapsed" index="" @click="logout()" v-if="!!user">{{ $tc('message.Logout') }}</el-menu-item>
            <el-menu-item class="el-menu-item" index="notifications" :route="{name:'notifications'}" v-if="!!user">
              <el-badge :value="unread" :max="99" class="item" v-if="unread > 0">
                <el-button size="small" icon="el-icon-bell" circle></el-button>
              </el-badge>
              <el-button size="small" icon="el-icon-bell" circle v-else></el-button>
            </el-menu-item>
            <el-menu-item class="el-menu-item submenu-collapsed" v-for="(lang, i) in langs" :key="`Lang${i}`" @click="pickLanguage(lang.value)">{{ lang.title }}</el-menu-item>
          </el-menu>
        </div>
        <div id="toggle" @click="select()">
          <div class="span" id="top" :class="{ active: isActive }"></div>
          <div class="span" id="middle" :class="{ active: isActive }"></div>
          <div class="span" id="bottom" :class="{ active: isActive }"></div>
        </div>
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
      langs: [
        {'title': this.$tc("message.English"), 'value': 'en-US'},
        {'title': this.$tc("message.Spanish"), 'value': 'es-ES'},
        {'title': this.$tc("message.Chinese"), 'value': 'zh-CN'},
        {'title': this.$tc("message.Russian"), 'value': 'ru-RU'},
        {'title': this.$tc("message.Portuguese"), 'value': 'pt-PT'},
      ],
      isActive: false,
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
    },
    pickLanguage(lang) {
      this.$i18n.locale = lang;
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    select: function() {
      this.isActive = !this.isActive;
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
  max-width: 240px;
  float: left;
  vertical-align: bottom;
}
.el-menu--horizontal {
  border: none;
  font-family: 'Aller Bold';
  font-size: 16px;
  color: #888893;
  margin-left: 20px;
  display: inline-block;
}
.el-menu-right {
  float: right;
  .el-select {
    float: left;
  }
}
.el-menu-item a {
  text-decoration: none;
}
.el-menu-item {
  &:hover,
  &.is-active {
    color: #2b7cba !important;
  }
}
.submenu-collapsed {
  display: none;
}
#toggle {
  position: absolute;
  right: 20px;
  top: 14px;
  z-index: 999;
  width: 40px;
  height: 40px;
  cursor: pointer;
  float: right;
  transition: all .3s ease-out;
  visibility: hidden;
  opacity: 0;
}
#toggle .span {
  border-radius: 10px;
  background: #2b7cba;
  transition: all 0.3s ease-out;
  backface-visibility: hidden;
}
#top.span.active {
  transform: rotate(45deg) translateX(3px) translateY(5px);
}
#middle.span.active {
  opacity: 0;
}
#bottom.span.active {
  transform: rotate(-45deg) translateX(8px) translateY(-10px);
}
@media only screen and (max-width: 768px) {
  .logoHeader {
    display: block;
    max-width: 170px;
    margin-top: 15px;
  }
  .el-menu--horizontal {
    width: 100%;
    margin-left: 0;
    margin: 80px 0 30px 0;
    display: block;
  }
  .el-menu-demo {
    margin: 80px 0 0 0;
  }
  .el-menu-right {
    margin: 0 0 30px 0;
  }
  .submenu, .lang-switcher {
    display: none !important;
  }
  .submenu-collapsed {
    display: block;
  }
  #toggle {
    visibility: visible;
    opacity: 1;
    margin-top: 6px;
  }
  #toggle .span {
    height: 4px;
    margin: 5px 0;
    transition: all .3s ease-out;
    backface-visibility: visible;
    visibility: visible;
    opacity: 1;
  }
  #menu .el-menu-item {
    display: none;
  }
  #menu ul {
    display: none;
  }
  #menu.active {    
    visibility: visible;
    opacity: 0.98;
    transition: all .5s ease-out;
    .el-menu--horizontal .el-menu-item {
      text-align: center;
      float: none;
      display: block;
      height: 100%;
      width: 100%;
      border-top: 1px solid #EAEAEB;
      font-size: 18px;
    }
    ul {
      display: block;
    }
  }
}
</style>
