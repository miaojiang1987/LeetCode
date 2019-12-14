from bisect import bisect_left
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        output = []

        for i in range(len(searchWord)):
            w = searchWord[:i+1]
            output.append([])
            index = bisect_left(products, w)
            while len(output[-1]) < 3 and index < len(products) and w in products[index]:
                output[-1].append((products[index]))
                index += 1

        return output