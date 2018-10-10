from marketplace.tokens.models import Token


def create_token(campaign):
    """Helper to create a token related with the campaign. Need to be updated to handle real
    creation of the token.
    """
    return Token.objects.create(
        name=campaign.title,
        code=campaign.title[:4].upper(),
        amount=1000,  # TODO Add dynamic amount of tokens
        price=campaign.funds,
        currency=campaign.currency,
    )
