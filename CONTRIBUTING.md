# Contributing to Daisy's Garden

Thanks for your interest in improving the game!

## Reporting bugs and requesting features

Open an issue in the **Issues** tab. Include what you expected to happen, what
actually happened, and your Python version and operating system.

## Submitting changes

1. Fork the repository and create a branch from `main`.
2. Make your change. Keep game rules in `game_logic.py` so they can be tested.
3. Add or update tests in `test_game_logic.py`.
4. Run the checks locally:
   ```
   pip install pytest flake8
   flake8 --max-line-length=100 .
   pytest -v
   ```
5. Open a pull request. All tests must pass before it is merged.

## Coding style

Follow [PEP 8](https://peps.python.org/pep-0008/). The `flake8` linter runs
automatically on every push and pull request.

## Security issues

Do not report security problems in public issues. See [SECURITY.md](SECURITY.md).
