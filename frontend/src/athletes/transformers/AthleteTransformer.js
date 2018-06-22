import Transformer from '../../base/transformers/BaseTransformer'
import Athlete from '../models/Athlete'

class AthleteTransformer extends Transformer {
  static fetch (athlete) {
    return new Athlete({
      id: athlete.id,
      firstName: athlete.first_name,
      lastName: athlete.last_name,
      country: athlete.country,
      sport: athlete.sport,
      links: athlete.links,
      pictures: athlete.pictures,
    })
  }
}

export default AthleteTransformer
