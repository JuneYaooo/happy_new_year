from django.shortcuts import render
from .models import NewYearPainting
import random
from django.conf import settings
from django.core.files import File


def generate_new_painting(keyword, style):
    # code to generate the painting and message
    # here you can look up the painting in the database
    # or generate a new one using the keyword and style
    # and return it
    # img_name = 'rabbit.jpg'
    # painting = get_local_image(img_name)
    path = 'new_year_paintings/rabbit.jpg'
    generated_blessing = generate_blessing()
    painting = f'{settings.MEDIA_URL}{path}'
    return painting, generated_blessing

def generate_painting(request):
    painting = None
    message = None
    if request.method == 'POST':
        keyword = request.POST['keyword']
        painting_style = request.POST['painting_style']
        # generate the painting and message here
        painting, message = generate_new_painting(keyword, painting_style)

    else:
        pass
    print('painting',{'painting': painting, 'message': message})
    return render(request, 'index.html', {'painting': painting, 'message': message})

def generate_blessing():
    """
    Randomly generate a new year blessing
    """
    # a list of blessings
    blessings = ["新年快乐", "祝您健康长寿", "万事如意", "祝你吉星高照", "财源广进", "福寿安康", "生意兴隆", "天天快乐", "身体健康", "工作顺利", "喜气洋洋", "祝你幸福美满"]
    return random.choice(blessings)

def store_data_in_db(img_path):
    painting_img = File(open(img_path, 'rb'))
    painting_img.name = 'example.jpg'
    painting = NewYearPainting(name="example", type="example_type", image=painting_img, keywords="example_keyword")
    painting.save()
