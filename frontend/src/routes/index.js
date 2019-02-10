export default [
  {
    path: '/login',
    name: 'login',
    component: resolve => require(['@/auth/pages/Login.vue'], resolve)
  },
  {
    path: '/register',
    name: 'registration',
    component: resolve => require(['@/auth/pages/Registration.vue'], resolve)
  },
  {
    path: '/restore-password/:restorePasswordCode/',
    name: 'restore.password',
    component: resolve => require(['@/auth/pages/RestorePassword.vue'], resolve),
    props: true
  },
  {
    path: '/forgot',
    name: 'forgot',
    component: resolve => require(['@/auth/pages/Forgot.vue'], resolve)
  },
  {
    path: '/verified/:verificationCode/',
    name: 'verified',
    component: resolve => require(['@/auth/pages/Verified.vue'], resolve),
    props: true
  },

  // User
  {
    path: '/profile',
    name: 'profile',
    component: resolve => require(['@/users/pages/Profile.vue'], resolve),
    meta: {
      auth: true
    }
  },
  {
    path: '/notifications',
    name: 'notifications',
    component: resolve => require(['@/actions/pages/Notifications.vue'], resolve)
  },

  // Campaigns
  {
    path: '/campaigns',
    name: 'campaign.list',
    component: resolve => require(['@/campaigns/pages/CampaignList.vue'], resolve)
  },
  {
    path: '/campaigns/create',
    name: 'campaign.create',
    component: resolve => require(['@/campaigns/pages/CampaignCreate.vue'], resolve),
    props: true,
    meta: {
      auth: true
    }
  },
  {
    path: '/campaigns/:campaignId/edit/:step',
    name: 'campaign.edit',
    component: resolve => require(['@/campaigns/pages/CampaignEdit.vue'], resolve),
    props: true,
    meta: {
      auth: true
    }
  },
  {
    path: '/campaigns/:campaignId/success',
    name: 'campaign.success',
    component: resolve => require(['@/campaigns/pages/CampaignSuccess.vue'], resolve),
    props: true,
    meta: {
      auth: true
    }
  },
  {
    path: '/campaigns/:campaignId',
    name: 'campaign.details',
    component: resolve => require(['@/campaigns/pages/CampaignDetails.vue'], resolve),
    props: true
  },
  {
    path: '/purchases/:campaignId',
    name: 'campaign.invest',
    component: resolve => require(['@/campaigns/pages/CampaignInvest.vue'], resolve),
    meta: {
      auth: true
    }
  },
  {
    path: '/purchased/:purchaseId',
    name: 'campaign.invested',
    component: resolve => require(['@/campaigns/pages/CampaignInvested.vue'], resolve),
    props: true,
    meta: {
      auth: true
    }
  },

  {
    path: '/purchase',
    name: 'purchase',
    component: resolve => require(['@/pages/Purchase.vue'], resolve),
    meta: {
      auth: true
    }
  },
  {
    path: '/faq',
    name: 'faq',
    component: resolve => require(['@/pages/Faq.vue'], resolve)
  },
  {
    path: '/terms',
    name: 'terms',
    component: resolve => require(['@/pages/Terms.vue'], resolve)
  },
  {
    path: '/risks',
    name: 'risks',
    component: resolve => require(['@/pages/Risks.vue'], resolve)
  },

  {
    path: '/about',
    name: 'about',
    component: resolve => require(['@/pages/About.vue'], resolve)
  },
  {
    path: '/contact',
    name: 'contact',
    component: resolve => require(['@/pages/Contact.vue'], resolve)
  },
  {
    path: '/press',
    name: 'press',
    component: resolve => require(['@/pages/Press.vue'], resolve)
  },
  {
    path: '/deck',
    name: 'deck',
    component: resolve => require(['@/pages/Deck.vue'], resolve)
  },
  // 404
  {
    path: '/404',
    name: 'not-found',
    component: resolve => require(['@/pages/NotFound.vue'], resolve)
  },
  {
    path: '/manteinance',
    name: 'manteninance',
    component: resolve => require(['@/pages/Manteinance.vue'], resolve)
  },
  {
    path: '/privacy',
    name: 'privacy',
    component: resolve => require(['@/pages/Privacy.vue'], resolve)
  },
  // Redirects
  {
    path: '/',
    redirect: '/campaigns'
  },
  // {
  //   path: '/',
  //   redirect: '/manteinance'
  // },
  {
    path: '/*',
    redirect: '/404'
  }
]
