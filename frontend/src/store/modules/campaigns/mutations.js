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
  pushCampaigns (state, campaigns) {
    state.campaigns = state.campaigns.concat(campaigns)
  },
  pagination(state, pagination) {
    state.pagination.count = pagination.count;
    state.pagination.next = pagination.next;
    state.pagination.previous = pagination.previous;
  },
}
