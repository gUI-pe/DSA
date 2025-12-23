from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        book = defaultdict(int)
        # creates a dict to keep how many times an int is called
        for i in nums:
            book[i] += 1
        # sorts the dict by value in acs order
        book = dict(sorted(book.items(), key=lambda item: item[1]))

        bookAnswers = list(book.keys())

        answer = []
        for _ in range (k):
            answer.append(bookAnswers.pop())

        return answer
