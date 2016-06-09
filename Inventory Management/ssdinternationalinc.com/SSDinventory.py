import csv, operator

f1 = file('ItemExport.csv', 'rU') 		# Warehouse QoH
f2 = file('SSDItemExport.csv', 'rU')	# SSD QoH
f3 = file('SSD.csv', 'wb')				# Merged Inventory

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

SSD_brands = [	'FNH USA', 'BENELLI USA', 'BERETTA USA', 
				'HORNADY AMMUNITION', 'MAGTECH AMMUNITION', 
				'SMITH & WESSON', 'WALTHER ARMS, INC.', 'HECKLER & KOCH']


masterlist1 = list(c1)
masterlist2 = list(c2)

#						   #
# Filter the SSD Inventory #
#						   #
for SSD_row in masterlist2:

	# Iterate through list of SSD brands
	for brand in SSD_brands:

		if SSD_row[4] == brand:

			# Add approved row to result file
			c3.writerow(SSD_row)
			break

#								 #
# Filter the Warehouse Inventory #
#								 #
for wh_row in masterlist1:

	found = False

	# Iterate through list of SSD brands
	for brand in SSD_brands:

		if wh_row[4] == brand:

			found = True
			break

	if not found:
		if wh_row[0] != 'item_no':
			# Add approved row to result file
			c3.writerow(wh_row)