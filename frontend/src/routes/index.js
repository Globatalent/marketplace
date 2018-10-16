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

  // User
  {
    path: '/profile',
    name: 'profile',
    component: resolve => require(['@/users/pages/Profile.vue'], resolve),
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
    path: '/campaigns/create',
    name: 'campaign.create',
    component: resolve => require(['@/campaigns/pages/CampaignCreate.vue'], resolve),
    props: true,
    meta: {
      auth: true,
    },
  },
  {
    path: '/campaigns/:campaignId/edit/:step',
    name: 'campaign.edit',
    component: resolve => require(['@/campaigns/pages/CampaignEdit.vue'], resolve),
    props: true,
    meta: {
      auth: true,
    },
  },
  {
    path: '/campaigns/:campaignId',
    name: 'campaign.details',
    component: resolve => require(['@/campaigns/pages/CampaignDetails.vue'], resolve),
    props: true,
  },
  {
    path: '/purchased/:purchaseId',
    name: 'athlete.invested',
    component: resolve => require(['@/campaigns/pages/CampaignInvested.vue'], resolve),
    props: true,
    meta: {
      auth: true,
    },
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
