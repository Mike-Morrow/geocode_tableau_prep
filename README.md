# geocode_tableau_prep

This script allows you to geocode addresses into lat, lon in Tableau Prep. 

2 things to do in Prep to ensure the script works:

1) Must name your address column 'Address'
2) Must have a 'lat' column and 'lon' column that are decimal data types. You can do this by creating a calculated field and with value 0.0 
