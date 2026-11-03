[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/loren1204/Daisy-s-Garden/badge)](https://scorecard.dev/viewer/?uri=github.com/loren1204/Daisy-s-Garden)
[![Tests](https://github.com/loren1204/Daisy-s-Garden/actions/workflows/tests.yml/badge.svg)](https://github.com/loren1204/Daisy-s-Garden/actions/workflows/tests.yml)

# Daisy's Garden

A re-imagined Space Invaders game written in Python with the `turtle` module.
You play as a pixel daisy defending the garden from falling vines.

**Welcome page:** https://loren1204.github.io/Daisy-s-Garden/

## Features

- **Character customization:** custom `.png` and `.gif` sprites for the player, enemies and background
- **Lives system:** three hearts act as extra lives; one is lost each time a vine reaches the ground or touches the daisy
- **Score and timer** shown on screen
- **Tested game rules:** movement, collision and lives logic live in `game_logic.py` and are covered by automated tests

## How to run

1. Install Python 3.10 or newer (`turtle` is included with Python).
2. Put these image files in the same folder as the script: `background.png`, `pixeldaisy.gif`, `vines.gif`, `smaller_heart.gif`.
3. Run:
   ```
   python daisys_garden.py
   ```

**Controls:** Left / Right arrows to move, Space to fire, Q to quit.

## Running the tests

```
pip install pytest flake8
flake8 --max-line-length=100 .
pytest -v
```

Tests and linting also run automatically on every push through GitHub Actions.

## Libraries used

- **turtle:** draws the graphics and handles keyboard input
- **random:** spawns vines at random positions within the window

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) to report bugs or submit changes.
Please report security problems privately rather than in public issues.

## License

Released under the MIT License. See [LICENSE](LICENSE).
