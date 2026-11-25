-- Usage rows for the re-bundle. Run AFTER this builder subagent run completes
-- (subagent usage rows are written to muse.db only when the run finishes).
-- Write the rows unchanged, one JSON object per line, to usage.jsonl in this
-- work dir, then re-bundle with --muse-usage usage.jsonl added.
-- Agent: 223b75ad-6d54-4b32-b531-108b7cfcf8ed (builder subagent, model muse-spark-1.3).
-- Parent agent d01feded-817f-45cb-9577-8f9a9c3b1673 is NOT bundled (its session
-- is only a --parent-session link), so only the builder agent_id is needed.
SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('223b75ad-6d54-4b32-b531-108b7cfcf8ed') ORDER BY u.created_at DESC LIMIT 500
