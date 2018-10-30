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
      'id': user.id,
      'first_name': user.firstName,
      'last_name': user.lastName,
      'email': user.email,
      'birth_date': user.birthDate,
      'avatar': user.avatar,
      'country': user.country,
      'citizenship': user.citizenship,
    }
    if (!!user.password && user.password !== "") {
      data['password'] = user.password
    }
    return data
  }
}

export default UserTransformer
