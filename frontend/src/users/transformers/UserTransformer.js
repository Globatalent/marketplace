import Transformer from '../../base/transformers/BaseTransformer'
import User from '../models/User'
import AthleteTransformer from '../../athletes/transformers/AthleteTransformer'

class UserTransformer extends Transformer {
  static fetch (user) {
    let newUser = new User({
      id: user.id,
      email: user.email,
    })
    if (user.athlete){
      newUser.athlete = AthleteTransformer.fetch(user.athlete)
    }
    return newUser
  }
}

export default UserTransformer
