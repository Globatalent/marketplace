export default [
  {
    path: '/login',
    name: 'login',
    component: resolve => require(['@/auth/pages/Login.vue'], resolve),
  },
  {
    path: '/register',
    name: 'registration',
    component: resolve => require(['@/auth/pages/Registration.vue'], resolve),
  },
  {
    path: '/restore-password/:restorePasswordCode/',
    name: 'restore.password',
    component: resolve => require(['@/auth/pages/RestorePassword.vue'], resolve),
    props: true,
  },
  {
    path: '/forgot',
    name: 'forgot',
    component: resolve => require(['@/auth/pages/Forgot.vue'], resolve),
  },
  {
    path: '/verified/:verificationCode/',
    name: 'verified',
    component: resolve => require(['@/auth/pages/Verified.vue'], resolve),
    props: true,
  },
  // Athletes
  {
    path: '/athlete-profile',
    name: 'athlete.profile',
    component: resolve => require(['@/athletes/pages/AthleteProfile.vue'], resolve),
    meta: {
      auth: true,
    },
  },
  {
    path: '/athletes',
    name: 'athlete.list',
    component: resolve => require(['@/athletes/pages/AthleteList.vue'], resolve),
  },
  {
    path: '/athletes/:athleteId',
    name: 'athlete.details',
    component: resolve => require(['@/athletes/pages/AthleteDetails.vue'], resolve),
    props: true,
  },

  {
    path: '/purchases/:athleteId',
    name: 'athlete.invest',
    component: resolve => require(['@/athletes/pages/AthleteInvest.vue'], resolve),
    meta: {
      auth: true,
    },
  },
  {
    path: '/purchased/:purchaseId',
    name: 'athlete.invested',
    component: resolve => require(['@/athletes/pages/AthleteInvested.vue'], resolve),
    props: true,
    meta: {
      auth: true,
    },
  },

  // User
  {
    path: '/profile',
    name: 'profile',
    component: resolve => require(['@/auth/pages/Profile.vue'], resolve),
    meta: {
      auth: true,
    },
  },
  {
    path: '/notifications',
    name: 'notifications',
    component: resolve => require(['@/actions/pages/Notifications.vue'], resolve),
  },

  // Campaigns
  {
    path: '/campaigns',
    name: 'campaign.list',
    component: resolve => require(['@/campaigns/pages/CampaignList.vue'], resolve),
  },
  {
    path: '/campaigns/:campaignId',
    name: 'campaign.details',
    component: resolve => require(['@/campaigns/pages/CampaignDetails.vue'], resolve),
    props: true,
  },

  // 404
  {
    path: '/404',
    name: 'not-found',
    component: resolve => require(['@/pages/NotFound.vue'], resolve),
  },
  // Redirects
  {
    path: '/',
    redirect: '/campaigns',
  },
  {
    path: '/*',
    redirect: '/404',
  },
]
