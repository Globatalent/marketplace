import Transformer from '../../base/transformers/BaseTransformer'
import User from '../models/User'

class UserTransformer extends Transformer {
  static fetch (user) {
    return new User({
      id: user.id,
      email: user.email,
    })
  }
}

export default UserTransformer
