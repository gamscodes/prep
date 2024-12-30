class Solution:

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1

            while arr[j] > pivot and j >= low + 1:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSort(self, arr, low, high):
        if low < high:
            p_ind = self.partition(arr, low, high)
            self.quickSort(arr, low, p_ind - 1)
            self.quickSort(arr, p_ind + 1, high)


arr = [4, 1, 3, 9, 7]
ob = Solution()
ob.quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
