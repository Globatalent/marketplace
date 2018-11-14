import Transformer from '../../base/transformers/BaseTransformer'


class UserTransformer extends Transformer {
  static fetch (user) {
    return {
      id: user.id,
      firstName: user.first_name,
      lastName: user.last_name,
      password: user.password,
      email: user.email,
      birthDate: user.birth_date,
      avatar: user.avatar,
      country: user.country,
      citizenship: user.citizenship,
    }
  }

  static send(user) {
    let data = {
      'first_name': user.firstName,
      'last_name': user.lastName,
      'email': user.email,
      'birth_date': user.birthDate.toISOString().split('T')[0],
      'avatar': user.avatar,
      'country': user.country,
      'citizenship': user.citizenship,
    }
    if (!!user.password && user.password !== "") {
      data['password'] = user.password
    }
    return data
  }
  static sendPartial(user) {
    let data = {}
    if(user.hasOwnProperty('firstName')) {
      data['first_name'] = user.firstName
    }
    if(user.hasOwnProperty('lastName')) {
      data['last_name'] = user.lastName
    }
    if(user.hasOwnProperty('email')) {
      data['email'] = user.email
    }
    if(user.hasOwnProperty('birthDate')) {
      data['birth_date'] = user.birthDate.toISOString().split('T')[0]
    }
    if(user.hasOwnProperty('avatar')) {
      data['avatar'] = user.avatar
    }
    if(user.hasOwnProperty('country')) {
      data['country'] = user.country
    }
    if(user.hasOwnProperty('country')) {
      data['citizenship'] = user.citizenship
    }

    if (!!user.password && user.password !== "") {
      data['password'] = user.password
    }
    return data
  }
}

export default UserTransformer
