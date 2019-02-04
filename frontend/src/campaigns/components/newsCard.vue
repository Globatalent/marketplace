<template>
  <el-card :body-style="{ padding: '0px', display: 'flex', 'flex-direction': 'column' }">
    <div class="campaign-info">
    <el-col :span="24">
         <h3 style="padding: 1rem;">{{article[1]}}</h3>
         <div style="padding: 0.5rem 1rem 1rem 1rem;" v-html="article[2]" ></div>
    </el-col>
    </div>
  </el-card>
</template>

<script>
  import VueI18n from 'vue-i18n'

  export default {
    name: 'newsCard',
    props: ['article'],
    data () {
      return {
        isExtended: false
      }
    },
    methods: {
      showMore() {
        this.isExtended = !this.isExtended;
      },
      showMoreMsg() {
        return this.isExtended ? this.$tc("message.showLess") : this.$tc("message.showMore");
      },
      getDescription() {
        return this.isExtended ? this.campaign.giveBack : (this.campaign.giveBack.length > 50 ? this.campaign.giveBack.substring(0,50)+' ...' : this.campaign.giveBack);
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import '../../scss/variables.scss';

  .el-card {
    border-radius: 8px;
    //height: 470px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    margin-bottom: 35px;

    &:hover {
      box-shadow: 0 5px 16px 0 rgba(0, 0, 0, 0.2);
    }

    a:hover {
      text-decoration: none;
    }
  }

  .likeButton {
    margin-left: 15px;
    float: right;
    cursor: pointer;
  }

  .likeIcon {
    font-size: 18px;
    transition: all 0.2s ease-in;
    color: #aaa;
    position: relative;
    top: 2px;

    &.is-following {
      transform: scale(1.2);
      color: #a0a8ab;
    }
  }

  .show-more-msg{
    color: $--color-primary !important;
    background: white;
    position: absolute;
    bottom: 0;
    left: 0;
    cursor: pointer;
  }
  .show-more-container {
    overflow: hidden;
    transition: all .3s ease-out;
  }
  .show-more-container.extended {
    max-height: 100%;
  }

  .campaign-image {
    height: 200px;
    overflow: hidden;
    position: relative;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center top;

    &.is-placeholder-image {
      background-image: url('../../assets/img/user-placeholder-circle.png');
      background-size: 60%;
      background-position: center;
    }
  }

  .campaign-progress {
    overflow: hidden;
    flex-grow: 1;
  }

  .el-progress {
    margin-top: 10px;
  }

  .goal {
    color: #999;
    font-size: 1em;
    line-height: 1em;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 15px;
  }

  .timeLeft {
    display: inline-block;
    font-size: 13px;

    .far {
      margin-right: 10px;
    }
  }

  .campaign-subtitle {
    font-family: 'Aller Regular';
    padding-bottom: 30px;
  }

  .campaign-info {
    color: #687173;
    font-size: 13px;
    display: flex;
    flex-direction: column;
  }

  .campaign-nameBlock {
    padding: 25px 20px 15px 20px;
    border-bottom: 1px solid #f0f0f0;
    min-height: 170px;
  }

  .campaign-progress {
    padding: 12px 20px 12px 20px;
    border-bottom: 1px solid #f0f0f0;
  }

  .campaign-footer {
    padding: 10px 20px 10px 20px;
  }

  .campaign-flag {
    width: 30px;
    height: auto;
    display: inline-block;
    float: right;
    position: absolute;
    right: 10px;
    bottom: 10px;
  }

  .campaign-progress-info {
    display: flex;
    flex-direction: row;
  }

  .campaign-progress-info-funding {
    width: 65%;
  }

  .campaign-progress-rating {
    width: 35%;
    text-align: right;
  }

  .campaign-progress-info-funding-text {
    font-family: 'Aller Bold';
  }

  .campaign-progress-info-funding-qty {
    font-family: 'Aller Regular';
  }

  .fulltext p,
.less {
	display: none;
}

.fulltext:target p,
.fulltext:target .less {
	display: block;
}

.fulltext:target .more {
	display: none;
}
</style>
