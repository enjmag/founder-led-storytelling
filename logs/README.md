# Logs

Copy both files into each project folder (`projects/<client>-<reel>/`).

**delivery-log.csv** has one row per export. The agent fills it at stage 8. Only Enjo sets `status = Approved` and `approved_by`. Status values: Draft · Sent · Changes requested · Approved · Uploaded.

**hook-scoreboard.csv** has one row per hook once it's live, checked about 3 and 7 days after posting. `hook_type` uses one tag: confession · number · contradiction · origin · comedy · question · object. The agent marks `winner` and writes one line in LESSONS.md about why it probably won. Treat this as a pattern guess, not proof, until the same pattern has won about 3 times.
