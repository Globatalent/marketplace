import Transformer from '../../base/transformers/BaseTransformer'
import Supporter from '../models/Supporter'

class SupporterTransformer extends Transformer {
  static fetch (supporter) {
    return new Supporter({
      id: supporter.id,
      firstName: supporter.first_name,
      lastName: supporter.last_name,
    })
  }
  static send (supporter) {
    return {
      'id': supporter.id,
      'first_name': supporter.firstName,
      'last_name': supporter.lastName,

    }
  }
}

export default SupporterTransformer
