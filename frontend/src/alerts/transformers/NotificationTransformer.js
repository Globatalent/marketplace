import Transformer from '../../base/transformers/BaseTransformer'
import Notification from '../models/Notification'
import ActionTransformer from './ActionTransformer'


class NotificationTransformer extends Transformer {
  static fetch (notification) {
    return new Notification({
      id: notification.id,
      read: notification.read,
      readAt: notification.read_at,
      action: ActionTransformer.fetch(notification.action),
    })
  }

  static send(athlete) {
    return {
      'id': notification.id,
      'read': notification.read,
    }
  }
}

export default NotificationTransformer
