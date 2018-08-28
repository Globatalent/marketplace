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
}

export default SupporterTransformer
