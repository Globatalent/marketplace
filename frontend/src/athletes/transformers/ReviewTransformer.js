import Transformer from '../../base/transformers/BaseTransformer'
import Review from '../models/Review'


class ReviewTransformer extends Transformer {
  static fetch (review) {
    return new Review({
      id: review.id,
      text: review.text,
      state: review.state,
      reviewer: review.reviewer,
    })
  }
}

export default ReviewTransformer
