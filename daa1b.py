# Interpolation Search vs Binary Search Analysis
# Student Roll Numbers: 1 to 10000


import matplotlib.pyplot as plt
import pandas as pd


# -----------------------------
# Interpolation Search
# -----------------------------

def interpolation_search(arr, target):

    low = 0
    high = len(arr) - 1
    probes = 0


    while low <= high and arr[low] <= target <= arr[high]:

        probes += 1


        pos = low + ((target - arr[low]) * (high - low) //
                     (arr[high] - arr[low]))


        if arr[pos] == target:
            return pos, probes


        elif arr[pos] < target:
            low = pos + 1


        else:
            high = pos - 1


    return -1, probes



# -----------------------------
# Binary Search
# -----------------------------

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    probes = 0


    while low <= high:

        probes += 1


        mid = (low + high) // 2


        if arr[mid] == target:
            return mid, probes


        elif arr[mid] < target:
            low = mid + 1


        else:
            high = mid - 1


    return -1, probes




# -----------------------------
# Main Program
# -----------------------------


# Sorted student roll numbers
roll_numbers = list(range(1, 10001))


# Roll numbers to test
test_roll_numbers = [
    100,
    2500,
    5000,
    7500,
    9999
]


analysis = []


for roll in test_roll_numbers:


    # Interpolation Search
    i_index, i_probe = interpolation_search(
        roll_numbers,
        roll
    )


    # Binary Search
    b_index, b_probe = binary_search(
        roll_numbers,
        roll
    )


    analysis.append([
        roll,
        i_probe,
        b_probe
    ])




# -----------------------------
# Display Table
# -----------------------------


df = pd.DataFrame(
    analysis,
    columns=[
        "Roll Number",
        "Interpolation Search Probes",
        "Binary Search Probes"
    ]
)


print("\nSearch Analysis Table")
print("----------------------")

print(df)




# -----------------------------
# Chart Analysis
# -----------------------------


plt.figure(figsize=(8,5))


plt.plot(
    df["Roll Number"],
    df["Interpolation Search Probes"],
    marker="o",
    label="Interpolation Search"
)


plt.plot(
    df["Roll Number"],
    df["Binary Search Probes"],
    marker="o",
    label="Binary Search"
)



plt.xlabel("Student Roll Number")

plt.ylabel("Number of Probes")

plt.title(
    "Interpolation Search vs Binary Search"
)


plt.legend()

plt.grid(True)


plt.show()