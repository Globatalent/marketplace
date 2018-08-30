import Transformer from '../../base/transformers/BaseTransformer'
import Action from '../models/Action'


class ActionTransformer extends Transformer {
  static fetch (action) {
    return new Action({
      id: action.id,
      actorContentType: action.actor_content_type,
      actorObjectId: action.actor_object_id,
      verb: action.verb,
      targetContentType: action.target_content_type,
      targetObjectId: action.target_object_id,
      triggerContentType: action.trigger_content_type,
      triggerObjectId: action.trigger_object_id,
      text: action.text,
    })
  }
}

export default ActionTransformer
