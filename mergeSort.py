class Solution:
    def mergeSort(self, arr, start, end):

        if start < end:
            mid = (start + end) // 2
            self.mergeSort(arr, start, mid)
            self.mergeSort(arr, mid + 1, end)
            self.merge(arr, start, mid, end)

    def merge(self, arr, start, mid, end):
        left = arr[start : mid + 1]
        right = arr[mid + 1 : end + 1]

        i, j = 0, 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [12, 11, 13, 5, 6, 7]
ob = Solution()
ob.mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
