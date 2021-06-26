from random import randint


class SortAlgorithms:

    def bubble(nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return nums

    def insertion(nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        return nums

    def pyramid_func(nums, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            SortAlgorithms.pyramid_func(nums, heap_size, largest)

    def pyramid(nums):
        n = len(nums)
        for i in range(n, -1, -1):
            SortAlgorithms.pyramid_func(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            SortAlgorithms.pyramid_func(nums, i, 0)
        return nums

    def quick_func(nums):
        if len(nums) < 2:
            return nums
        low, same, high = [], [], []
        pivot = nums[randint(0, len(nums) - 1)]
        for item in nums:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)
        return SortAlgorithms.quick_func(low) + same + SortAlgorithms.quick_func(high)

    def quick(nums):
        nums = SortAlgorithms.quick_func(nums)
        return nums

    def selection(nums):
        for i in range(len(nums)):
            low_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[low_index]:
                    low_index = j
            nums[i], nums[low_index] = nums[low_index], nums[i]
        return nums

    def shell(nums):
        inc = len(nums) // 2
        while inc:
            for i, el in enumerate(nums):
                while i >= inc and nums[i - inc] > el:
                    nums[i] = nums[i - inc]
                    i -= inc
                nums[i] = el
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
        return nums
