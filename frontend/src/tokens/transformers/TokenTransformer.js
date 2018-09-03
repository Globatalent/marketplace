import Transformer from '../../base/transformers/BaseTransformer'
import Token from '../models/Token'


class TokenTransformer extends Transformer {
  static fetch (token) {
    return new Token({
      id: token.id,
      name: token.name,
      code: token.code,
      amount: token.amount,
      price: token.price,
      progression: token.progression,
      unitPrice: token.unit_price,
      remaining: token.remaining,
      currency: token.currency,
    })
  }

  static send(token) {
    return {
      'id': token.id,
      'name': token.name,
      'code': token.code,
      'amount': token.amount,
      'price': token.price,
    }
  }
}

export default TokenTransformer
