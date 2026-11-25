# Credit and time estimate

Run this after the timing map (stage 2), and put the result on the edit plan before gate 2.

```
python3 tools/estimate.py --gen-seconds <clip lengths> --hooks <hook lengths> --bridge <s> --rate <credits/s> --risk low|medium|high
```

| Input | Where it comes from |
|---|---|
| Clip lengths | Timing map: VO length rounded up, one clip per VO file, 30 s max |
| Rate | The current price per generated second at test resolution (Reel 6 planning used about 7 credits/s at 720p) |
| Risk | **low**: static shots, one person · **medium**: people and actions · **high**: lip sync, comedy timing, hands, darkness, crowds |
| Savings | Reuse body clips as hook cut-ins at no cost; generate the bridge once; use real B-roll wherever it exists |

**Check against past work:** Reel 5 (high risk, 5 body clips + 3 hooks + bridge) comes out at about 1,900 credits and about **1.7 days of hands-on work**. That matches Enjo's real 1–2 days at about 5 h/day. **Higgsfield generation and queue time comes on top and varies**, so add it once the jobs are submitted. Recalibrate with the actuals in `LESSONS.md`.
