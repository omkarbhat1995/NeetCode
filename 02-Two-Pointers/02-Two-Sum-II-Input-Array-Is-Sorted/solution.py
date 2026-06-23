def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Add 1 to convert from 0-indexed to 1-indexed
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, shift the left pointer up
            left += 1
        else:
            # Sum is too large, shift the right pointer down
            right -= 1
            
    return [] # The problem guarantees one valid solution, so we won't hit this