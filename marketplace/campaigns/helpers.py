from options.models import Option

from marketplace.tokens.models import Token


def generate_token_code(string):
    code = "{}T".format(
        "".join(list(map(lambda x: x[:1], string.upper().split(" ")[:2])))
    )
    return "{}{}".format(code[0] * (3 - len(code)), code)


def create_token(campaign):
    """Helper to create a token related with the campaign. Need to be updated to handle real
    creation of the token.
    """
    token_price = Option.objects.get_value("DEFAULT_TOKEN_PRICE", 5.0)
    return Token.objects.create(
        name=campaign.title,
        code=generate_token_code(campaign.title),
        amount=campaign.funds // token_price,
        price=campaign.funds,
        currency=campaign.currency,
    )
