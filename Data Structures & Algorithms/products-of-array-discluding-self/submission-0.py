class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefixProduct = 1
        suffixProduct = 1
        prefixProducts = []
        suffixProducts = []
        products = []

        for i in range(length):
            prefixProducts.append(prefixProduct)
            prefixProduct *= nums[i]
        
        for i in range(length - 1, -1, -1):
            suffixProducts.insert(0, suffixProduct)
            suffixProduct *= nums[i]
        
        for i in range(length):
            products.append(prefixProducts[i] * suffixProducts[i])
        
        return products
