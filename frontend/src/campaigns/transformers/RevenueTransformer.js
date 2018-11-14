import Transformer from '../../base/transformers/BaseTransformer'
import Revenue from '../models/Revenue'
import getCurrencySymbol from '@/base/helpers/currencies'

class RevenueTransformer extends Transformer {
  static fetch (revenue) {
    return new Revenue({
      id: revenue.id,
      campaign: revenue.campaign,
      amount: revenue.amount,
      year: revenue.year,
      currency: revenue.currency,
      currencySymbol: getCurrencySymbol(revenue.currency),
    })
  }

  static send (revenue) {
    return {
      id: revenue.id,
      campaign: revenue.campaign,
      amount: revenue.amount,
      year: revenue.year,
      currency: revenue.currency,
    }
  }
}

export default RevenueTransformer
