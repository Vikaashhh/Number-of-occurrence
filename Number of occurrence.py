class Solution:
    def countFreq(self, arr, target):
        # Pehla function: target ka first occurrence dhoondhta hai
        def firstOccurrence(arr, target):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:  # yahan sahi syntax use kiya
                    result = mid
                    high = mid - 1  # left mein check karte hain
                elif arr[mid] < target:
                    low = mid + 1  # right side jao
                else:
                    high = mid - 1  # left side jao
            return result

        # Doosra function: target ka last occurrence dhoondhta hai
        def lastOccurrence(arr, target):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    result = mid
                    low = mid + 1  # right mein aur dekhte hain
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result

        # Dono occurrences nikaal lo
        first = firstOccurrence(arr, target)
        last = lastOccurrence(arr, target)

        if first == -1 or last == -1:
            return 0  # agar nahi mila toh 0
        else:
            return last - first + 1  # count nikaalo
