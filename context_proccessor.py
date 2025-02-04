from blog.models import Category

def general_context(request):

    context = {
        'category' : Category.objects.filter(status=True),
    }
    
    return context