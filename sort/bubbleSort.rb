def bubble_sort(list)
  iterations = list.size - 2

  return list unless iterations > 0 # already sorted

  swaps = 2

  while swaps > 1 do
    swaps = 0

    0.upto(iterations) do |i|
      if list[i] > list[i + 1]
        list[i], list[i + 1] = list[i + 1], list[i] # swap values
        swaps += 1
      end
    end

    iterations -= 1
  end

  list
end
