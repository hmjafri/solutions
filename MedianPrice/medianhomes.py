from statistics import median
from zillow import states, prices

result = {}

# Loop over list of states
for i in range(0, len(states) - 1):
    state = states[i]

    # If this state was encountered earlier in the loop. Just append to the list of medians
    if state in result:
        result[state].append(prices[i])
    else: # Encountering this state the first time. New list of medians to be created 
        result[state] = [prices[i]]

for state in result:
    result[state] = median(result[state])
    
print('State | Median Price')
print('--------------------')

# Produce list of sorted states from the 'result' dictionary 
sorted_states = sorted(result)

# Use sorted_states to print in alphabetical order
for state in sorted_states:
  print('%s    | %f'%(state, result[state]))

# Finally, print the US median
print('US    | %f'%(median(prices)))
