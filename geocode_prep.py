def geocode(address_df):
    import pandas as pd
    import requests
    google_api_key = "YOUR_GOOGLE_MAPS_KEY"
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def geocode2(row):
        try:
            address = row
            params = {'key' : google_api_key, 'sensor': 'false', 'address': address}
            r = requests.get(url, params=params)
            results = r.json()['results']
            location = results[0]['geometry']['location']
            return(location['lat'], location['lng'])
        except:
            return 'Could not geocode'
    
    address_df['Lat_Long'] = address_df['Address'].apply(lambda x : geocode2(x))
    address_df['Lat'] = address_df['Lat_Long'].apply(lambda x : x[0])
    address_df['Lon'] = address_df['Lat_Long'].apply(lambda x : x[1])
    address_df = address_df.drop('Lat_Long', axis=1)
    return address_df