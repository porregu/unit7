def get_max(nums):
    max_number=0
    for y in(nums):
        if len(y)>max_number:
            max_number=len(y)
    return max_number
nums=["abierto","cerrado","los","affvgvgggbgbg"]
print(get_max(nums))