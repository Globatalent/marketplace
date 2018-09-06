import Transformer from '../../base/transformers/BaseTransformer'
import Purchase from '../models/Purchase'


class PurchaseTransformer extends Transformer {
  static fetch (purchase) {
    return new Purchase({
      id: purchase.id,
      token: purchase.token,
      amount: purchase.amount,
      status: purchase.status,
      total: purchase.total,
    })
  }

  static send(purchase) {
    return {
      'id': purchase.id,
      'token': purchase.token,
      'amount': purchase.amount,
    }
  }
}

export default PurchaseTransformer
