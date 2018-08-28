def is_following(supporter, athlete):
    """Checks if the given supporter is following the given athlete."""
    return supporter.following.filter(pk=athlete.pk).exists()
