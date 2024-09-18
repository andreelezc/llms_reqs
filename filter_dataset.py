import json

# Load the dataset
with open('input_data/baseline_dataset.json', 'r') as file:
    data = json.load(file)

# Create a new dataset with the specified fields and order
filtered_data = []
for item in data:
    filtered_item = {
        "ID": item["ID"],
        "Image Filename": item["Image Filename"],
        "URL": item["URL"],
        "Caption": item["Caption"],
        "Process Flow": item["Process Flow"]
    }
    filtered_data.append(filtered_item)

# Save the filtered dataset
with open('input_data/filtered_dataset.json', 'w') as file:
    json.dump(filtered_data, file, indent=2)

print('Filtered dataset created successfully.')
