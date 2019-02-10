<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc("message.WeBringTheTalent") }}</h3>
          <h3 class="beginBlock-subTitle">Risk Disclaimer</h3>
        </div>
      </el-col>
    </el-row>
<el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
      All implied conditions, warranties and/or representations, including but not limited to the 
implied conditions, warranties and/or representations of satisfactory quality, fitness for a 
particular purpose, non-infringement, compatibility, security and accuracy are excluded 
from these Terms to the extent that they may be excluded as a matter of applicable law. 
Further, Globatalent does not warrant that the Site will be uninterrupted or error free or 
that any defects will be corrected. To the extent permitted by applicable law, Globatalent 
expressly disclaims all liability howsoever arising whether in contract, tort (or deceit), 
breach of statutory duty, or otherwise (including, but not limited to, liability for any 
negligent acts or omissions), even if foreseeable, to any person in respect of any claims 
or losses of any nature, arising directly or indirectly from or in connection with: (i) 
anything done or the consequences of anything done or omitted to be done wholly or 
partly in reliance upon the whole or any part of the contents of this Site; and (ii) the use 
of any data or materials on this Site or unauthorised access to this Site or otherwise. 
Globatalent will not be responsible for any breach of these Terms caused by 
circumstances beyond its reasonable control. 
 
Information on the Site is not offered as advice on any particular matter and must not be 
treated as a substitute for specific advice. In particular Information on the Site does not 
constitute professional, financial or investment advice and must not be used as a basis 
for making investment decisions and is in no way intended, directly or indirectly, as an 
attempt to market or sell any type of financial instrument. Advice from a suitably qualified 
professional should always be sought in relation to any particular matter or 
circumstances. The contents of this Site do not constitute an invitation to invest in, or 
constitute or form a part of any offer for the sale or subscription of, or any invitation to 
offer to buy or subscribe for, any securities or other financial instruments, nor should it or 
any part of it form the basis of, or be relied upon in any connection with any contract or 
commitment whatsoever. 

      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'risks',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {}
  },

  created() {},
  methods: {}
}
</script>


<style lang="scss" scoped>
  @import '../scss/variables.scss';

  .beginBlock {
    background: url('../assets/img/background-list-title.png');
    background-repeat: no-repeat;
    background-position: center;
  }

  .campaignList-startBlock {
    margin: 30px auto;
    border-top: 1px solid $--grey-detailCampaign-border;
    padding-top: 40px;
    display: block;
    width: 100%;
    max-width: 895px;
    font-size: 0px;
  }

  .campaignList-startBlock-container {
    max-width: 585px;
    display: block;
    margin: 0 auto;
  }

  .campaignList-startBlock-sentence {
    display: inline-block;
    vertical-align: top;
    text-align: right;
    padding-right: 20px;
    padding-right: 0px;
    width: 70%;
    width: 100%;
    text-align: center;
  }

  .campaignList-startBlock-sentence1 {
    font-weight: normal;
    font-family: 'Aller';
    font-size: 36px;
    line-height: 36px;
    margin: 0;
  }

  .campaignList-startBlock-sentence2 {
    font-size: 14px;
  }

  strong {
    font-weight: bold;
  }
</style>
