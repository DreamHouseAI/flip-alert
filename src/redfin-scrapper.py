'''Install the redfin unofficial wrapper package using "python3 -m pip install redfin" in your terminal'''
'''It looks like it is blocked by Redfin not working anymore'''

from redfin import Redfin
client = Redfin()

print(type(client))

address = '4544 Radnor St, Detroit Michigan'

response = client.search(address)
url = response['payload']['exactMatch']['url']
initial_info = client.initial_info(url)

property_id = initial_info['payload']['propertyId']
mls_data = client.below_the_fold(property_id)

listing_id = initial_info['payload']['listingId']
avm_details = client.avm_details(property_id, listing_id)