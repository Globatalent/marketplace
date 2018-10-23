'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  BASE_URL: JSON.stringify(process.env.BASE_URL || 'https://market-api.dekaside.com')
})
