from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d  = {
        'title': 'Home',
        'content': 'Welcome to the home page',
        'paragraph' :'I remember as a child, and as a young budding naturalist, spending \
all my time observing and testing the world around me—moving pieces, \
altering the flow of things, and documenting ways the world responded \
to me. Now, as an adult and a professional naturalist, I have  approached language in the same way, not from an academic point of view but as a \
curious child still building little mud dams in creeks and chasing after \
frogs. So this book is an odd thing: it is a naturalists walk through the \ language-making landscape of the English language, and following in \
the naturalists tradition it combines observation, experimentation, \
speculation, and documentation—activities we dont normally \
associate with language.',
        'age': 20,
        'name' : 'John',
        'Birthday': datetime.datetime(2000, 1, 1),
        'lst' : ['python', 'is', 'interesting'],
        'courses' : [{
            'name': 'math',
            'code': 'MTH101',
            'fee': 1000
        }, 
        {
            'name': 'physics',
            'code': 'PHY101',
            'fee': 2000

        },
        {
            'name': 'chemistry',
            'code': 'CHM101',
            'fee': 1500
        },
        ]

    }
    return render(request, 'home.html', context=d) 
