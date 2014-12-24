#Selection Sort
#Created: Decemeber 24th 2014
import random

def selectionSort(unsortedNumbers):
  for i in range(0,len(unsortedNumbers)-1):
    minIndex = i
    for j in range(i, len(unsortedNumbers)):

      #update minIndex when you find a smaller number
      if unsortedNumbers[minIndex] > unsortedNumbers[j]:
        minIndex = j

    #swap the min with the unsortedNumbers[i] (parallel assingment)
    unsortedNumbers[i], unsortedNumbers[minIndex] = unsortedNumbers[minIndex], unsortedNumbers[i]
    

#generate 10 random numbers for testing
unsortedNumbers = [random.randint(1,100) for p in range(0,9)]

#display unsorted array
print "Unsorted array: "  + str(unsortedNumbers)

#selection sort
selectionSort(unsortedNumbers)

#display sorted array
print "Sorted array: "  + str(unsortedNumbers)
