class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        sortedArray = sorted(words)
        print(sortedArray)
        dicto = {}
        freq_array = []

        for i in sortedArray:
            if i in dicto:
                dicto[i] += 1
            else:
                dicto[i] = 1

        print(dicto)
        while(True):
            maximum = 0
            if len(freq_array) == k:
                break
            for key in dicto:
                if dicto[key] > maximum:
                    maximum = dicto[key]
            for keyo in dicto:
                if (dicto[keyo] == maximum) and (len(freq_array) != k):
                    freq_array.append(keyo)
                    dicto[keyo] = 0
                elif len(freq_array) == k:
                    break
        return freq_array


if __name__ == '__main__':
    answer = Solution()
    result = answer.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
    print(result)
