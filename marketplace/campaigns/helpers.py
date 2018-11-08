from options.models import Option

from marketplace.tokens.models import Token


def create_token(campaign):
    """Helper to create a token related with the campaign. Need to be updated to handle real
    creation of the token.
    """
    token_price = Option.objects.get_value("DEFAULT_TOKEN_PRICE", 5.0)
    return Token.objects.create(
        name=campaign.title,
        code=campaign.title[:4].upper(),
        amount=campaign.funds // token_price,
        price=campaign.funds,
        currency=campaign.currency,
    )
