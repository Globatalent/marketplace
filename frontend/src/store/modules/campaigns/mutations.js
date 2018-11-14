export default {
  campaign (state, campaign) {
    state.campaign = campaign
  },
  campaigns (state, campaigns) {
    state.campaigns = campaigns
  },
  sports (state, sports) {
    state.sports = sports
  },
  countries (state, countries) {
    state.countries = countries
  },
  pushCampaigns (state, campaigns) {
    state.campaigns = state.campaigns.concat(campaigns)
  },
  pushSports (state, sports) {
    state.sports = state.sports.concat(sports)
  },
  pagination(state, pagination) {
    state.pagination.count = pagination.count;
    state.pagination.next = pagination.next;
    state.pagination.previous = pagination.previous;
  },
}
