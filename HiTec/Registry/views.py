from django.http import HttpResponse

def index(request):
    return HttpResponse("<form>"
                        "<label>Name: </label>"
                        "<input type='text' />"
                        "<br />"
                        "<input type='submit' value='Submit'/>"
                        "</form>")
