import Transformer from '../../base/transformers/BaseTransformer'
import CampaignPicture from '../models/CampaignPicture'

class CampaignPictureTransformer extends Transformer {
  static fetch (picture) {
    return new CampaignPicture({
      id: picture.id,
      campaign: picture.campaign,
      image: picture.image
    })
  }

  static send (picture) {
    let data = {
      'campaign': picture.campaign,
      'image': picture.image,
    }
    if (!!picture.tags) {
      data.tags = picture.tags
    }
    return data
  }
}

export default CampaignPictureTransformer
