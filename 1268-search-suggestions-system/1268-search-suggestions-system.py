class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []
        products.sort()
        for i, l in enumerate(searchWord):
            temp = []
            for word in products:
                if i < len(word) and l == word[i]:
                    temp.append(word)
            output.append(temp[:3])
            products = temp
            
        return output
        