# Actions

Actions are at the heart of the adv3 command-processing system. When a player types a command, the parser creates an action object that goes through verification, precondition checks, and execution. This section covers how to work with that process and how to create your own verbs.

- **[Action Results](action-results.md)** — How actions report success, failure, and side effects
- **[Verify, Check, and When to Use Which](verify-check.md)** — The two-stage validation model and how to choose between them
- **[How to Create Verbs](creating-verbs.md)** — Defining new actions with grammar rules and handler methods
- **[Custom Preconditions](preconditions.md)** — Writing preconditions that must be satisfied before an action runs
- **[Implicit Action Reports](implied-actions.md)** — Controlling how automatically-triggered actions are described to the player

For a deeper look at how actions flow through the system, see the [Action Resolution](../../architecture/action-resolution.md) architecture deep-dive.
