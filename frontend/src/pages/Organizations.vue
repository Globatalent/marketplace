<template>
  <!-- <gb-base-layout> -->
		<div>
			    <el-row type="flex">
      <el-col :xs="24" :sm="{span: 12, offset: 10}" >
        <a href="/">
          <img class="logoHeader" src="@/assets/img/logo-header.png" style="max-width: 240px;" />
        </a>
      </el-col>
    </el-row>
			<el-col :xs="24" :sm="{span: 12, offset: 6}">
				<br>
		<el-row>
			<el-col style="background-color: #51a5dd;color:#fff;padding:24px;text-align:center;font-size:48px;" :xs="12" :sm="{span: 4}">
				1
			</el-col>
						<el-col style="background-color: #2f62ab;color:#fff;padding:24px" :xs="12" :sm="{span: 16, offset: 2}">
							Globatalent is a global marketplace that allows from people all
over the world to fund and trade in their favorite athletes, clubs
and sports idols, and increase fan engagement.
			</el-col>
		</el-row>
				<el-row>
			<el-col style="background-color: #51a5dd;color:#fff;padding:24px;text-align:center;font-size:48px;" :xs="12" :sm="{span: 4}">
				2
			</el-col>
						<el-col style="background-color: #2f62ab;color:#fff;padding:24px" :xs="12" :sm="{span: 16, offset: 2}">
							We give everyone the chance to have a stake in athletes and idols,
and even bet on future talent. We have made it our goal to bring the
best sports stars in the world to this platform.
			</el-col>
		</el-row>
				<el-row>
			<el-col style="background-color: #51a5dd;color:#fff;padding:24px;text-align:center;font-size:48px;" :xs="12" :sm="{span: 4}">
				3
			</el-col>
						<el-col style="background-color: #2f62ab;color:#fff;padding:24px" :xs="12" :sm="{span: 16, offset: 2}">
						Begin now and we will help you to start your campaign. Be the first to experiment the new revolution in the sports world
			</el-col>
		</el-row>
		<br>
    <el-row>
		<h4 class="campaign-name" style="text-align: center">Are you an athlete, club or organization?</h4>
    <h4 class="campaign-name" style="text-align: center">We can help you to <span style="color:	#0375B2">start a campaign now!!</span></h4>
		</el-row>
		<el-row>

    <!-- Note :
   - You can modify the font style and form style to suit your website. 
   - Code lines with comments ���Do not remove this code���  are required for the form to work properly, make sure that you do not remove these lines of code. 
   - The Mandatory check script can modified as to suit your business needs. 
   - It is important that you test the modified form before going live.-->
<el-col :xs="24" :sm="{span: 12, offset: 4}">

<div id='crmWebToEntityForm' style='width:600px;margin:auto;'>
  <form action='https://crm.zoho.com/crm/WebToLeadForm' name=WebToLeads3718183000000277001 method='POST' onSubmit='javascript:document.charset="UTF-8";' accept-charset='UTF-8'>

	 <!-- Do not remove this code. -->
	<input type='text' style='display:none;' name='xnQsjsdp' value='26ded01eee3cbb74693abaeee34e2f8acbb50ca314ea68813ba8b57665b4dc48'/>
	<input type='hidden' name='zc_gad' id='zc_gad' value=''/>
	<input type='text' style='display:none;' name='xmIwtLD' value='902ae1508809b664f4a8880feb7226435ad252e90c524204e2b557a276287e3b'/>
	<input type='text' style='display:none;'  name='actionType' value='TGVhZHM='/>

	<input type='text' style='display:none;' name='returnURL' value='https://market.globatalent.com' /> 
	 <!-- Do not remove this code. -->

	<table style='width:600px;background-color:white;color:black'>

	<!-- <tr style="padding:6px;border-spacing:0px;border-width:0px;"><td colspan='2' style='text-align:left;color:black;font-size:14px;padding:6px;border-spacing:0px;border-width:0px;'><strong>Request information</strong></td></tr> -->

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td  style='nowrap:nowrap;text-align:left;width:200px;padding:6px;border-spacing:0px;border-width:0px;'>Your first name<span style='color:red;'>*</span></td><td style='width:250px;' ><input type='text' style='width:250px;'  maxlength='40' name='First Name' /></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td  style='nowrap:nowrap;text-align:left;width:200px;padding:6px;border-spacing:0px;border-width:0px;'>Your last name<span style='color:red;'>*</span></td><td style='width:250px;' ><input type='text' style='width:250px;'  maxlength='80' name='Last Name' /></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td  style='nowrap:nowrap;text-align:left;width:200px;padding:6px;border-spacing:0px;border-width:0px;'>Club/Athlete name<span style='color:red;'>*</span></td><td style='width:250px;' ><input type='text' style='width:250px;'  maxlength='100' name='Company' /></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td  style='nowrap:nowrap;text-align:left;width:200px;padding:6px;border-spacing:0px;border-width:0px;'>Email<span style='color:red;'>*</span></td><td style='width:250px;' ><input type='text' style='width:250px;'  maxlength='100' name='Email' /></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td  style='nowrap:nowrap;text-align:left;width:200px;padding:6px;border-spacing:0px;border-width:0px;'>Phone</td><td style='width:250px;' ><input type='text' style='width:250px;'  maxlength='30' name='Phone' /></td></tr>

	<tr><td  style='nowrap:nowrap;text-align:left;width:200px;'>How did you find us?</td><td style='width:250px;'>
		<select style='width:250px;' name='Lead Source'>
			<option value='-None-'>-None-</option>
			<option value='Advertisement'>Advertisement</option>
			<option value='Affiliate&#x20;Partner'>Affiliate Partner</option>
			<option value='Chat'>Chat</option>
			<option value='Cold&#x20;Call'>Cold Call</option>
			<option value='Employee&#x20;Referral'>Employee Referral</option>
			<option value='External&#x20;Referral'>External Referral</option>
			<option value='GBT&#x20;Web&#x20;site'>GBT Web site</option>
			<option value='Seminar&#x20;Partner'>Seminar Partner</option>
			<option value='Trade&#x20;Show'>Trade Show</option>
			<option value='Web&#x20;Download'>Web Download</option>
			<option value='Facebook'>Facebook</option>
			<option value='Twitter'>Twitter</option>
			<option value='Google&#x2b;'>Google&#x2b;</option>
		</select></td></tr>

	<tr style='display:none;' ><td style='nowrap:nowrap;text-align:left;font-size:12px;font-family:Georgia;width:50%'>client type</td><td style='width:250px;'>
		<select style='width:250px;' name='LEADCF1'>
			<option value='-None-'>-None-</option>
		<option selected value='B2B'>B2B</option>
			<option value='B2C'>B2C</option>
			<option value='Token&#x20;listing'>Token listing</option>
		</select></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td  style='nowrap:nowrap;text-align:left;width:200px;padding:6px;border-spacing:0px;border-width:0px;'>Tell us about your project<span style='color:red;'>*</span> </td><td> <textarea name='Description' placeholder="Tell us what project you need to tokenize" maxlength='32000' style='width:250px;'>&nbsp;</textarea></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td colspan='2'><div class='dIB vat mT2' align='left' style='color: rgb(0, 0, 0); font-size: 12px; font-family: sans-serif;display: inline-block;vertical-align: top;'><div class='displayPurpose  f13'><label class='newCustomchkbox-md dIB w100per'><input autocomplete='off' onclick='disableSubmit()' id='privacyTool' type='checkbox' name='privacyTool'><span class='chkbxIcon'></span></label></div></div><div class='fw200 dIB vat mL5' style='nowrap:nowrap;text-align:left;vertical-align: top;margin-top: 3px;line-height: 14px;width:90%;display: inline-block;color:black'>   I agree to the <a href='http://globatalent.com/termsandconditions' title='http://globatalent.com/termsandconditions' target='_blank'>Privacy Policy and Terms of Service</a>.</div></td></tr>

	<tr style="padding:6px;border-spacing:0px;border-width:0px;"><td colspan='2' style='text-align:center; padding-top:15px;padding:6px;border-spacing:0px;border-width:0px;'>
		<input id='formsubmit' type='submit' value='Submit' />
		<input onclick='disableSubmitwhileReset()' type='reset' style='color:black' value='Reset' />
	    </td>
	</tr>
   </table>
	</form>
</div>
</el-col>
    </el-row>
		<br>
		    <!-- <el-row v-loading.fullscreen="loadingCampaigns" v-if="campaigns.length > 0">
      <el-col>
        <masonry :cols="{default: 4, 992: 3, 750: 2, 500: 1}" :gutter="{default: '40px', 750: '20px'}">
          <gb-campaign-list-card v-for="campaign in campaigns" :key="campaign.id"
                                 :campaign="campaign"></gb-campaign-list-card>
        </masonry>
      </el-col>
    </el-row>
    <div class="campaignList-noResults text-center" v-else>
      <h2>{{ $tc('message.NoResults') }}</h2>
    </div> -->
      </el-col>
  <!-- </gb-base-layout> -->
	</div>
</template>

<script>
 	var mndFileds=new Array('Company','First Name','Last Name','Email','Description');
 	var fldLangVal=new Array('Company','First Name','Last Name','Email','Description');
	var name='';
	var email=''; 
  
function disableSubmitwhileReset()
	{		
	var submitbutton = document.getElementById('formsubmit');
	if(document.getElementById('privacyTool')!=undefined || document.getElementById('consentTool')!=undefined)
	{
		submitbutton.setAttribute('disabled', true);
	submitbutton.setAttribute('style','opacity:0.5;');
 }
	else
	{
		submitbutton.removeAttribute('disabled');
	}
} 
function disableSubmit()
	{		
	var isprivacyToolAvail = false;
	var isconsentToolAvail = false;
	var bothtoolAvail = false;
	var privacytool='';
	var consenttool='';
	var submitbutton = document.getElementById('formsubmit');
	if(document.getElementById('privacyTool')!=undefined && document.getElementById('consentTool')!=undefined)
	{
			isprivacyToolAvail=true;
			privacytool = document.getElementById('privacyTool');
			isconsentToolAvail=true;
			consenttool=document.getElementById('consentTool');
			bothtoolAvail=true;
	}

	if(document.getElementById('privacyTool')!=undefined)
	{
			isprivacyToolAvail=true;
			privacytool = document.getElementById('privacyTool');
	}
	if(document.getElementById('consentTool')!=undefined)
	{
			isconsentToolAvail=true;
			consenttool=document.getElementById('consentTool');
	}
	if(submitbutton.hasAttribute('disabled') && bothtoolAvail && consenttool.checked && privacytool.checked)
	{
			submitbutton.removeAttribute('disabled');
	submitbutton.removeAttribute('style','opacity: none;');}
	else if(submitbutton.hasAttribute('disabled') && isprivacyToolAvail && privacytool.checked && consenttool=='')
	{
			submitbutton.removeAttribute('disabled');
	submitbutton.removeAttribute('style','opacity: none;');}
	else if(submitbutton.hasAttribute('disabled') && isconsentToolAvail && consenttool.checked && privacytool=='')
	{
			submitbutton.removeAttribute('disabled');
submitbutton.removeAttribute('style','opacity: none;');
	}
	else
	{
			submitbutton.setAttribute('disabled', true);
	submitbutton.setAttribute('style','opacity: 0.5;');}
}

 	  function checkMandatory3718183000000277001() {
		for(i=0;i<mndFileds.length;i++) {
		  var fieldObj=document.forms['WebToLeads3718183000000277001'][mndFileds[i]];
		  if(fieldObj) {
			if (((fieldObj.value).replace(/^\s+|\s+$/g, '')).length==0) {
			 if(fieldObj.type =='file')
				{ 
				 alert('Please select a file to upload.'); 
				 fieldObj.focus(); 
				 return false;
				} 
			alert(fldLangVal[i] +' cannot be empty.'); 
   	   	  	  fieldObj.focus();
   	   	  	  return false;
			}  else if(fieldObj.nodeName=='SELECT') {
  	   	   	 if(fieldObj.options[fieldObj.selectedIndex].value=='-None-') {
				alert(fldLangVal[i] +' cannot be none.'); 
				fieldObj.focus();
				return false;
			   }
			} else if(fieldObj.type =='checkbox'){
 	 	 	 if(fieldObj.checked == false){
				alert('Please accept  '+fldLangVal[i]);
				fieldObj.focus();
				return false;
			   } 
			 } 
			 try {
			     if(fieldObj.name == 'Last Name') {
				name = fieldObj.value;
 	 	 	    }
			} catch (e) {}
		    }
		}
	     }	   
</script>

<script>
  import BaseLayout from '@/layout/BaseLayout.vue'
  import { mapGetters } from 'vuex'
  import CampaignListCard from '@/campaigns/components/CampaignListCard.vue'
  import countries from '@/base/helpers/countries'

  export default {
    name: 'CampaignList',
    components: {
      'gb-base-layout': BaseLayout,
      'gb-campaign-list-card': CampaignListCard
    },
    data () {
      return {
        allCountries: countries,
        search: null,
        sport: null,
        country: null,
        kind: null,
        errorMessage: '',
        loadingCampaigns: false
      }
    },
    computed: {
      ...mapGetters({
        sports: 'campaigns/sports',
        campaigns: 'campaigns/campaigns',
        countryCodes: 'campaigns/countries',
        pagination: 'campaigns/pagination',
        user: 'users/user'
      }),
      countries () {
        let countriesWithLabels = []
        this.countryCodes.forEach(country => {
          countriesWithLabels.push({
            code: country,
            name: this.allCountries[country]
          })
        })
        return countriesWithLabels.sort((a, b) => (a.name > b.name ? 1 : (b.name > a.name) ? -1 : 0))
      }
    },
    created () {
      this.$store.commit('campaigns/sports', [])
      this.$store.dispatch('campaigns/sports')
      this.$store.dispatch('campaigns/countries')
      this.initial()
    },
    mounted () {
      this.checkScroll()
    },
    methods: {
      initial () {
        // Load initial page of campaigns
        this.$store.commit('campaigns/campaigns', [])
        if (!!this.user) {
          this.$store.dispatch('users/fetchUser').then(() => {
            this.$store.dispatch('campaigns/list', {
              filters: {active: 'True'}
            })
          })
        } else {
          this.$store.dispatch('campaigns/list', {
            filters: {
              active: 'True'
            }
          })
          // .then(() => {
          //   console.log(this.campaigns)
          // })
        }
      },
      onSearch (event) {
        // Update the campaign list using the search
        if (event.keyCode === 13) {
          this.filter()
        }
      },
      filter () {
        let filters = {
          active: 'True'
        }
        if (!!this.search && this.search !== '') filters.search = this.search
        if (!!this.sport && this.sport !== '') filters.sport = this.sport
        if (!!this.country && this.country !== '') filters.country = this.country
        if (!!this.kind && this.kind !== '') filters.kind = this.kind
        this.$store.dispatch('campaigns/list', {filters: filters})
      },
      checkScroll () {
        window.onscroll = () => {
          let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight >= document.documentElement.offsetHeight - 500

          if (bottomOfWindow && !this.loadingCampaigns) {
            this.loadingCampaigns = true
            // Gets a new page of campaigns and push them to the current list
            if (!!this.pagination.next) {
              this.$store.dispatch('campaigns/list', {
                filters: {active: 'True'},
                url: this.pagination.next,
                push: true
              }).then(() => {this.loadingCampaigns = false})
            } else {
              this.loadingCampaigns = false
            }
          }
        }
      }
    }

  }
</script>

<style lang="scss" scoped>
  @import '../scss/variables.scss';

  .beginBlock {
    background: url('../assets/img/background-list-title.png');
    background-repeat: no-repeat;
    background-position: center;
  }

  .searchList {
    display: flex;
    flex-direction: row;
    margin-bottom: 35px;
  }

  .searchList-option {
    margin-left: 30px;
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
    font-family: 'OpenSans Regular';
    font-size: 36px;
    line-height: 36px;
    margin: 0;
  }

  .campaignList-startBlock-sentence2 {
    font-size: 14px;
  }

  .startFreeButton {
    display: inline-block;
    vertical-align: top;
    width: 30%;
    font-size: 14px;
    font-family: 'OpenSans SemiBold';
    position: relative;
    top: 6px;
    display: none;
  }
</style>


<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'Organizations',
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
</style>