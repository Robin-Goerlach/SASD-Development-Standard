# C#/.NET Code Review Checklist

- [ ] Change belongs to the correct project and layer.
- [ ] No new circular or accidental dependency was introduced.
- [ ] Nullable contracts are correct; `!` is justified.
- [ ] Public API and XML comments are updated where required.
- [ ] Async code avoids blocking and propagates cancellation.
- [ ] Resources are disposed correctly.
- [ ] Expected outcomes and exceptions are modeled appropriately.
- [ ] Error messages and logs expose no secrets or sensitive internals.
- [ ] Structured logging uses stable property names and appropriate levels.
- [ ] Configuration is typed, validated and not hard-coded.
- [ ] Persistence changes include migration and compatibility considerations.
- [ ] Tests cover behavior, error paths and relevant integrations.
- [ ] Analyzer suppressions are narrow and documented.
- [ ] Packages, target frameworks and publish settings are intentional.
- [ ] Documentation, changelog or ADR was updated when needed.
