base_percentages = []
sum_totals = []

nuc_counts = [[4, 3, 4, 4], [9, 6, 8, 7], [6, 4, 2, 6], [9, 6, 8, 10], [12, 6, 9, 9], [12, 2, 4, 12], [5, 3, 4, 6], [24, 14, 16, 21], [3, 2, 5, 2], [10, 10, 0, 10]]
masses = [135.128, 111.103, 151.128, 125.107]
sum_total = 0

#Grab a set
#multiply 4 by 125.128

#Put the masses and sums in
for index in range(len(nuc_counts)):

    base_masses = []

    sums = 0
    
    current_set = nuc_counts[index]
    
    for four_indexes in range(4):
        current_number = current_set[four_indexes]
        current_mass = masses[four_indexes]

        base_mass = current_number * current_mass

        #put the set in base_mass
        base_masses.append(base_mass)

        #running sum of the 4 items
        sums += base_mass
        sums = round(sums, 1)
                
    base_percentages.append(base_masses)
    
    sum_totals.append(sums)
    
    sums = 0
    
for current_set in base_percentages:
    
    for index in range(4):
        
        current_number = current_set[index]
        
        current_sum = sum_totals[index]

        base_percentage = (current_number /current_sum) * 100
        
        print(base_percentage)
        

        
        #base_percentages[index] = base_percentage

print(base_percentages)
print(sum_totals)
