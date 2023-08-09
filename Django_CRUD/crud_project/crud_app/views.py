from django.shortcuts import render, redirect
import json

data_file_path = 'data.json'  # Path to the JSON data file

# Create view function
def create(request):
    if request.method == 'POST':
        # Retrieve the data from the form
        name = request.POST['name']
        age = request.POST['age']
        city = request.POST['city']
        
        # Read existing data from the JSON file
        with open(data_file_path, 'r') as f:
            data = json.load(f)
        
        # Update the data with the new entry
        data['name'] = name
        data['age'] = age
        data['city'] = city
        
        # Write the updated data back to the JSON file
        with open(data_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        return redirect('read')  # Redirect to the read route

    return render(request, 'create.html')


# Read view function
def read(request):
    with open(data_file_path, 'r') as f:
        data = json.load(f)

    return render(request, 'read.html', {'data': data})

# Update view function
def update(request):
    if request.method == 'POST':
        # Retrieve the data from the form
        name = request.POST['name']
        age = request.POST['age']
        city = request.POST['city']

        # Read existing data from the JSON file
        with open(data_file_path, 'r') as f:
            data = json.load(f)

        # Update the data with the new values
        data['name'] = name
        data['age'] = age
        data['city'] = city

        # Write the updated data back to the JSON file
        with open(data_file_path, 'w') as f:
            json.dump(data, f, indent=4)

        return redirect('read')  # Redirect to the read route

    return render(request, 'update.html')


# Delete view function

def delete(request):
    if request.method == 'POST':
        # Clear the data by writing an empty dictionary to the JSON file
        with open(data_file_path, 'w') as f:
            json.dump({}, f, indent=4)

        return redirect('read')  # Redirect to the read route

    return render(request, 'delete.html')
