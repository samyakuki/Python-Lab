from statistics import mean, median, mode
numbers = list(map(int, input("Enter numbers separated by spaces:").split()))
mean_value = mean(numbers)
median_value = median(numbers)
try:
    mode_value = mode(numbers)
except:
    mode_value = "Mode is not present in the list"
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")