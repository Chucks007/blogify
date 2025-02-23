# blogs/views.py (or blogs/proxy.py)
import requests
from django.http import JsonResponse

def proxy_zenquotes(request):
    """
    Makes a server-to-server request to ZenQuotes API and returns the JSON response.
    """
    api_url = 'https://zenquotes.io/api/random'
    try:
        # Make a request to ZenQuotes API
        api_response = requests.get(api_url)
        # Parse the JSON response
        data = api_response.json()
        # Return the data as JSON response
        return JsonResponse(data, safe=False)
    except Exception as e:
        # In case of error, return error details
        return JsonResponse({'error': str(e)}, status=500)
