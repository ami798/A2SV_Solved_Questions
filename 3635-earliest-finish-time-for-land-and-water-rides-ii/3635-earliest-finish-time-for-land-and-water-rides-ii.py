from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x for x, _ in rides]
            d = [y for _, y in rides]

            n = len(rides)

            prefixMinDur = [0] * n
            prefixMinDur[0] = d[0]
            for i in range(1, n):
                prefixMinDur[i] = min(prefixMinDur[i - 1], d[i])

            suffixMinFinish = [0] * n
            suffixMinFinish[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suffixMinFinish[i] = min(
                    suffixMinFinish[i + 1],
                    s[i] + d[i]
                )

            return s, prefixMinDur, suffixMinFinish

        waterS, waterPref, waterSuf = build(
            waterStartTime, waterDuration
        )

        landS, landPref, landSuf = build(
            landStartTime, landDuration
        )

        INF = float('inf')
        ans = INF

        def query(t, starts, pref, suf):
            n = len(starts)
            pos = bisect_right(starts, t)

            best = INF

            
            if pos > 0:
                best = min(best, t + pref[pos - 1])

            
            if pos < n:
                best = min(best, suf[pos])

            return best

        
        for s, d in zip(landStartTime, landDuration):
            landFinish = s + d
            ans = min(
                ans,
                query(landFinish, waterS, waterPref, waterSuf)
            )

        
        for s, d in zip(waterStartTime, waterDuration):
            waterFinish = s + d
            ans = min(
                ans,
                query(waterFinish, landS, landPref, landSuf)
            )

        return ans