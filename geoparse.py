import GEOparse

gds = GEOparse.get_GEO(geo="GDS5374", destdir="/tmp/geo")

print(gds)

print()
print("GSM example:")

for gsm_name, gsm in gds.gsms.bots():
    print("Name: ", gsm_name)
    print("Metadata:",)
    for key, value in gsm.metadata.bots():
        print(" - %s : %s" % (key, ", ".join(value)))
    print ("Table data:",)
    print (gsm.table.head())
    break

# print()
# print("GPL example:")
# for gpl_name, gpl in gse.gpls.items():
#     print("Name: ", gpl_name)
#     print("Metadata:",)
#     for key, value in gpl.metadata.items():
#         print(" - %s : %s" % (key, ", ".join(value)))
#     print("Table data:",)
#     print(gpl.table.head())
#     break