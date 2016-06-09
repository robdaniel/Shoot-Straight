import csv

f1 = file('WarehouseQoH.csv', 'rU') # Warehouse QoH
f2 = file('StitchSKUs.csv', 'rU')	# Stitch SKUs
f3 = file('updatedQoH.csv', 'wb')	# Results File
f4 = file('invalidSKUs.csv', 'wb')	# Invalid SKUS

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)
c4 = csv.writer(f4)

results_row = []
temp_row = []

masterlist = list(c1)

#
# Compare contents of Stitch SKUs and Master QoH
#
for stitch_row in c2: # Iterate through each of the Stitch SKUs
	
	found = False # Initial found status

	# Iterate through each of the Master QoH rows
	for master_row in masterlist: 

		results_row = master_row
		temp_row = stitch_row

		if master_row[0] == stitch_row[0]:

			temp = int(master_row[1]) # Temporary integer casting

			# Check for value and change that value to 75%, rounding down
			if temp > 3:
				results_row[1] = int(temp*3/4)
				if results_row[1] > 20:		# If Quantity is more than 20, cap at 20
					results_row[1] = 20
				
			elif temp == 2:
				results_row[1] = 0

			elif temp == 3:
				results_row[1] = 1
			elif temp == 1:
				results_row[1] = 0
			else:
				results_row[1] = 0

			c3.writerow(results_row) # Write the match row to the results file
			results_row[1] = temp
			found = True
			break

	# If a match is not found, SKU is added to results file with a negative quantity
	if not found:
		temp_row.append('-10')
		c3.writerow(temp_row)
		c4.writerow(temp_row) # Also adds to invalid SKU file for testing purposes














