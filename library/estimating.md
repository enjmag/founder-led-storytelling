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

**Check against past work:** Reel 5 (high risk, 5 body clips + 3 hooks + bridge) comes out at about 1,900 credits and about 2.8 working days in this estimator. You've said a 60 s reel takes 1–2 days at about 5 h/day when the edit is quicker, and that 4,000+ credits a month covers normal demand. Once there are real numbers, adjust the time constants in `tools/estimate.py` using the actuals in `LESSONS.md`.
