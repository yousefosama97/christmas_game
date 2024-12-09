from django.shortcuts import render

# Create your views here.

# Define the Secret Santa pairings (this could also be dynamic if needed)
secret_friends = {
    "Alice": "Bob",
    "Bob": "Charlie",
    "Charlie": "David",
    "David": "Eve",
    "Eve": "Frank",
    "Frank": "Grace",
    "Grace": "Hannah",
    "Hannah": "Ian",
    "Ian": "Jack",
    "Jack": "Alice"
}

def home(request):
    # Create a list of kids (keys from secret_friends)
    kids = list(secret_friends.keys())
    
    if request.method == 'POST':
        selected_kid_name = request.POST.get('selected_kid')
        
        # Find the Secret Santa partner from the dictionary
        secret_santa_name = secret_friends.get(selected_kid_name)
        
        # Return the result after the "Find your Secret Santa" button is clicked
        return render(request, 'secret_santa/result.html', {
            'selected_kid': selected_kid_name,
            'secret_santa': secret_santa_name
        })

    return render(request, 'secret_santa/home.html', {'kids': kids})
