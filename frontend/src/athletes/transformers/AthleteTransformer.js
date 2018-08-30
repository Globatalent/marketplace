import Transformer from '../../base/transformers/BaseTransformer'
import Athlete from '../models/Athlete'
import Vue from 'vue'
import TokenTransformer from '@/tokens/transformers/TokenTransformer'


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
      token: !!athlete.token? TokenTransformer.fetch(athlete.token) : null,
    })
  }

  static send(athlete) {
    return {
      'id': athlete.id,
      'first_name': athlete.firstName,
      'last_name': athlete.lastName,
      'date_of_birth': !!athlete.birthDate? Vue.moment(athlete.birthDate).format('YYYY-MM-DD') : null,
      'sex': athlete.sex,
      'country': athlete.country,
      'sport': athlete.sport,
    }
  }
}

export default AthleteTransformer
