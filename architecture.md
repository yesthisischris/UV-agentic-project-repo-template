<br>

---

## 7 . “Skateboard → Scooter → Bicycle → Car” branch strategy

| Branch    | Policy                                    | Protections |
|-----------|-------------------------------------------|-------------|
| `main`    | Always deployable (latest stable “car”).  | required CI, Semantic PR title |
| `bicycle` | Feature integration and testing.          | required CI |
| `scooter` | New features once “skateboard” is solid.  | CI optional |
| `dev`     | Rapid local experiments (“skateboard”).   | none        |

Merge order: `dev` → PR into `scooter` → PR into `bicycle` → milestone release bumps `bicycle` → PR into `main`.

<br>

---

## 8 . How to cut a release

1. Merge PRs with **Conventional Commit titles** (`feat:`, `fix:`…).  
2. Push tag `vX.Y.Z` *or* run `/release` slash‑command on GH.  
3. Workflow `release.yml`:
   * computes new version with `semantic‑release`,
   * builds wheel + sdist,
   * pushes to PyPI,
   * creates GitHub Release notes from commit messages,
   * bumps `CHANGELOG.md`.

<br>

---

### Use it today

```bash
gh repo create my‑agent --template langgraph-mcp-template
```
