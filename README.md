# geocode_tableau_prep

This script allows you to geocode addresses into lat, lon in Tableau Prep. 

2 things to do in Prep to ensure the script works:

1) Must name your address column 'Address'
2) Must have a 'lat' column and 'lon' column that are decimal data types. You can do this by creating a calculated field and with value 0.0 

This is how things should look like before you add the script step:

![Before Script Step](https://github.com/Mike-Morrow/geocode_tableau_prep/blob/master/Before_Script.JPG?raw=true)

This is what the script step should look like:

*note we've connected to our TabPy Server and we've specified our function name 'geocode'

![Script Step](https://github.com/Mike-Morrow/geocode_tableau_prep/blob/master/Script%20Step.JPG?raw=true)

