class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counts = Counter()

        for day_responses in responses:
            seen = set()

            for response in day_responses:
                if response not in seen:
                    counts[response] += 1
                    seen.add(response)

        most_common = responses[0][0]


        for response, count in counts.items():
            if count > counts[most_common]:
                most_common = response
            elif count == counts[most_common] and response < most_common:
                most_common = response

        return most_common