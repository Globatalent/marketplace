import Transformer from '../../base/transformers/BaseTransformer'
import Athlete from '../models/Athlete'
import Vue from 'vue'


class AthleteTransformer extends Transformer {
  static fetch (athlete) {
    return new Athlete({
      id: athlete.id,
      firstName: athlete.first_name,
      lastName: athlete.last_name,
      birthDate: !!athlete.date_of_birth ? Vue.moment(athlete.date_of_birth) : null,
      sex: athlete.sex,
      country: athlete.country,
      sport: athlete.sport,
      following: athlete.following,
      links: athlete.links,
      pictures: athlete.pictures,
    })
  }
}

export default AthleteTransformer
