# AI Buddy Workflow

Active repo: `foughtapple/test-project`
Branch: `main`
Allowed modification scope: only this repository unless the user explicitly changes the active project in AI Code Buddy.

Required ChatGPT process:

1. Update `.ai-code-buddy/requirements_memory.md` if the request changes persistent requirements.
2. Make a short plan.
3. Apply changes only in this repo.
4. Finish with the completion phrase below.

Completion phrase after GitHub/repo changes are done:

```text
AI_BUDDY_READY_TO_PULL
```

When AI Code Buddy sends debug output, inspect the failing step, fix the repo, then use the completion phrase again.
