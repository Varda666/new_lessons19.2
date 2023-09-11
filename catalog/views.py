from django.shortcuts import render

# Create your views here.

def catalog_home(request):
    return render(request, 'home.html')


def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'contacts.html')



def catalog_contacts_post(request):
    messages_list = []
    message_dict = {}
    if request.method == 'POST':
        message_dict['name'] = request.POST.get('name')
        message_dict['phone'] = request.POST.get('phone')
        message_dict['message'] = request.POST.get('message')
        messages_list.append(message_dict)
    print(messages_list)
    return render(request, 'index.html')
