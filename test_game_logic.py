"""Automated tests for the Daisy's Garden game rules."""

import pytest

from game_logic import clamp_move, is_hit, lose_life, spawn_x_range


def test_move_right_inside_bounds():
    assert clamp_move(0, 10, 1, -300, 300, 15) == 10


def test_move_left_inside_bounds():
    assert clamp_move(0, 10, -1, -300, 300, 15) == -10


def test_move_blocked_at_right_edge():
    assert clamp_move(280, 10, 1, -300, 300, 15) == 280


def test_stationary_cannon_does_not_move():
    assert clamp_move(50, 10, 0, -300, 300, 15) == 50


def test_lose_life_keeps_game_running():
    assert lose_life(3) == (2, False)


def test_last_heart_lost_is_not_game_over_yet():
    assert lose_life(1) == (0, False)


def test_hit_with_no_hearts_left_ends_game():
    assert lose_life(0) == (-1, True)


def test_collision_detection():
    assert is_hit(5)
    assert not is_hit(25)


def test_spawn_range_respects_margin():
    assert spawn_x_range(-300, 300) == (-200, 200)


def test_spawn_range_rejects_tiny_window():
    with pytest.raises(ValueError):
        spawn_x_range(-50, 50)
