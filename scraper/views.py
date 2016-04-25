from django.shortcuts import render
import pickle

# Create your views here.
def index(request):
    file = open('/Users/Pat/PycharmProjects/MyProj/namesite/vk.txt', 'r')
    vk = pickle.load(file)
    file.close()

    file = open('/Users/Pat/PycharmProjects/MyProj/namesite/parool.txt', 'r')
    parool = pickle.load(file)
    file.close()

    return render(request, 'scraper/index.html', {'vk':vk,'parool':parool})
