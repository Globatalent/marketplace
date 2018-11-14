import Transformer from '../../base/transformers/BaseTransformer'
import Income from '../models/Income'
import getCurrencySymbol from '@/base/helpers/currencies'

class IncomeTransformer extends Transformer {
  static fetch (income) {
    return new Income({
      id: income.id,
      campaign: income.campaign,
      amount: income.amount,
      year: income.year,
      currency: income.currency,
      currencySymbol: getCurrencySymbol(income.currency),
    })
  }

  static send (income) {
    return {
      id: income.id,
      campaign: income.campaign,
      amount: income.amount,
      year: income.year,
      currency: income.currency,
    }
  }
}

export default IncomeTransformer
