# Repository CI Activation Review Prompt

Review the repository CI activation evidence without inferring success from
workflow source files alone.

Verify separately:

1. repository identity and boundary checks,
2. exact commit SHA,
3. completed GitHub Actions workflow for that SHA,
4. successful Linux and Windows jobs,
5. successful aggregate merge gate,
6. uploaded evidence artifacts,
7. ruleset existence and active enforcement,
8. required-check context and strict policy,
9. force-push and deletion protection,
10. documented rollback path.

Classify each statement as Verified, Prepared, Pending, Failed, or Not
Applicable. Treat test source, workflow YAML, local logs, and a remote successful
run as different evidence classes.
