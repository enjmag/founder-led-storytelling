#!/usr/bin/env python3
"""Credit and time estimator for a founder-led reel.

Example:
  python3 tools/estimate.py --gen-seconds 11 9 26 19 6 --hooks 8 10 10 --bridge 4 \
      --rate 7 --risk medium

Gen seconds = the length of each generated clip (the VO length rounded up).
Rate = credits per generated second at your test resolution. Reel 6 planning
used about 7 credits/s (Seedance 2.5 at 720p via Higgsfield). Check the
current price before quoting.
"""
import argparse

RETRY = {"low": 0.5, "medium": 1.0, "high": 1.5}  # extra generations per shot


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--gen-seconds", type=float, nargs="*", default=[], help="body/closing generated clip lengths")
    p.add_argument("--hooks", type=float, nargs="*", default=[], help="generated hook lengths")
    p.add_argument("--bridge", type=float, default=0, help="generated bridge length (made once, reused)")
    p.add_argument("--rate", type=float, default=7.0, help="credits per generated second")
    p.add_argument("--risk", choices=RETRY, default="medium",
                   help="low = static, few people; medium = people + actions; high = lip sync, comedy, hands, darkness")
    p.add_argument("--final-upres", type=float, default=0.0,
                   help="extra multiplier if picks are regenerated at a higher resolution (e.g. 1.0)")
    p.add_argument("--edit-hours-per-variant", type=float, default=0.5,
                   help="assembly + polish per finished export")
    p.add_argument("--variants", type=int, default=6, help="exports, e.g. 3 hooks x (organic + ad) = 6")
    a = p.parse_args()

    clips = a.gen_seconds + a.hooks + ([a.bridge] if a.bridge else [])
    secs = sum(clips)
    base = secs * a.rate
    retries = base * RETRY[a.risk]
    upres = base * a.final_upres
    total = base + retries + upres

    shots = len(clips)
    plan_h = 1 + 0.15 * shots          # brief, timing map, edit plan, prompts
    gen_h = 0.1 * shots * (1 + RETRY[a.risk])  # reviewing picks (queue time is extra, see below)
    edit_h = a.edit_hours_per_variant * a.variants + 1  # assembly, subtitles, sound
    hours = plan_h + gen_h + edit_h

    print(f"Generated seconds: {secs:.0f} s across {shots} clips")
    print(f"Credits: base {base:.0f} + retries {retries:.0f} ({a.risk}) + upres {upres:.0f} = ~{total:.0f}")
    print(f"Hands-on time: plan {plan_h:.1f} h + review {gen_h:.1f} h + edit {edit_h:.1f} h = ~{hours:.1f} h"
          f" (~{hours/5:.1f} working days at 5 h/day)")
    print("Plus Higgsfield generation/queue time, which varies: add it once the generations are submitted.")
    print("These are ESTIMATES. Log the actuals in LESSONS.md so the numbers improve over time.")


if __name__ == "__main__":
    main()
