import csv

def export_vehicle_data(filename,vehicles):
    with open(filename,mode='w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Brand','Model','Year','Owner','Battery Capacity'])
        for v in vehicles:
            owner = v.get_owner()
            if owner is None:
                owner = "No Owner assigned"
            else:
                owner = owner.replace('owner: ', '')
            battery_capatacity = getattr(v,'battery_capacity','N/A')
            writer.writerow([v.brand,v.model,v.year,owner,battery_capatacity])

        return f"Vehicle data exported to {filename} successfully."