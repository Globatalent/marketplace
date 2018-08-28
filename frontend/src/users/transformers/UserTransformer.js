import Transformer from '../../base/transformers/BaseTransformer'
import User from '../models/User'
import AthleteTransformer from '../../athletes/transformers/AthleteTransformer'
import SupporterTransformer from '../../supporters/transformers/SupporterTransformer'


class UserTransformer extends Transformer {
  static fetch (user) {
    let newUser = new User({
      id: user.id,
      email: user.email,
    })
    if (user.athlete){
      newUser.athlete = AthleteTransformer.fetch(user.athlete)
    }
    if (user.supporter){
      newUser.supporter = SupporterTransformer.fetch(user.supporter)
    }
    return newUser
  }
}

export default UserTransformer
