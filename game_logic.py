"""Core rules for Daisy's Garden.

These functions have no dependency on turtle graphics, so they can be
unit tested automatically without opening a game window.
"""


def clamp_move(x, step, direction, left, right, gutter):
    """Return the cannon's new x position.

    If the move would push the cannon outside the play area
    (window edge minus the gutter), the cannon stays where it is.
    """
    new_x = x + step * direction
    if left + gutter <= new_x <= right - gutter:
        return new_x
    return x


def lose_life(player_lives):
    """Take away one life.

    Returns a tuple (remaining_lives, game_over). The player has
    MAX_HEALTH hearts and the game ends when a hit lands with no
    hearts left (remaining lives drop below zero).
    """
    remaining = player_lives - 1
    return remaining, remaining < 0


def is_hit(distance, threshold=20):
    """Return True when two sprites are close enough to collide."""
    return distance < threshold


def spawn_x_range(left, right, margin=100):
    """Return the (min_x, max_x) range where new aliens may spawn."""
    low, high = int(left + margin), int(right - margin)
    if low > high:
        raise ValueError("window is too narrow for the spawn margin")
    return low, high
