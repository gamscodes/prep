class Solution:

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if low < high:
            p_ind = self.partition(arr, low, high)
            self.quickSort(arr, low, p_ind - 1)
            self.quickSort(arr, p_ind + 1, high)


arr = [4, 1, 3, 9, 7]
ob = Solution()
ob.quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
