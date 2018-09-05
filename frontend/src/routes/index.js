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
    meta: {
      auth: true,
    },
  },
  {
    path: '/athletes/:athleteId',
    name: 'athlete.details',
    component: resolve => require(['@/athletes/pages/AthleteDetails.vue'], resolve),
    props: true,
    meta: {
      auth: true,
    },
  },

  {
    path: '/purchases/:athleteId',
    name: 'athlete.invest',
    component: resolve => require(['@/athletes/pages/AthleteInvest.vue'], resolve),
    meta: {
      auth: true,
    },
  },

  // Supporters
  {
    path: '/supporter-profile',
    name: 'supporter.profile',
    component: resolve => require(['@/supporters/pages/SupporterProfile.vue'], resolve),
    meta: {
      auth: true,
    },
  },

  {
    path: '/notifications',
    name: 'notifications',
    component: resolve => require(['@/notifications/pages/Notifications.vue'], resolve),
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
    redirect: '/login',
  },
  {
    path: '/*',
    redirect: '/404',
  },
]
