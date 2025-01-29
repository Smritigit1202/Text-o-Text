
from django.shortcuts import render

def counter(request):
    word_count = None  # Initialize word_count as None (default)
    text = ''  # Default empty text
    if request.method == 'POST':
        text = request.POST.get('text', '')  # Get the input text
        word_count = len(text.split())  # Calculate the word count
    
    return render(request, 'word_counter/counter.html', {'word_count': word_count, 'text': text})
