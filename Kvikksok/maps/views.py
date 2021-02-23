from django.shortcuts import render


def home(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    return render(request, 'maps\home.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})


"""
searchbar function
def get_zipcode_searchbar(query=None):
    queryset = []
    queries = query.split(" ") #removing all whitespace
"""
