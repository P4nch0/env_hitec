from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<form>"
                        "<label>Hello World: </label>"
                        "<input type='text' />"
                        "<br />"
                        "<input type='submit' value='Submit'/>"
                        "</form>")

def root(request):
    return HttpResponse("Root page")
