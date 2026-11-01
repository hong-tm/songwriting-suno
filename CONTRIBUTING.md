# Contributing

Thanks for helping improve this project.

## Quick start

1. **Fork** the repo, then clone your fork.
2. Create a branch: `git checkout -b feat/short-description`.
3. Make focused changes — one concern per pull request.
4. Run the test suite (below).
5. Commit with a **Conventional Commit** message.
6. Push and open a Pull Request describing **what** and **why**.

## Tests

Run the project's test entrypoints before opening a PR:

```bash
python3 scripts/selftest.py                                # must exit 0
python3 -m unittest discover -s scripts/tests -t scripts/tests
```

CI runs both on every PR (and on pushes to `main` and `master`). **PRs must be
green.**

## Commit style

Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.

## Security

- **Never commit secrets** — keep credentials out of this repo entirely.
- If you find a security issue, report it **privately** to the maintainer — do not
  open a public issue.

## License

By contributing, you agree your work is licensed under this repository's LICENSE.
