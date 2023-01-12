from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import NewYearPainting

def store_data_in_db(img_path):
    painting_img = File(open(img_path, 'rb'))
    painting_img.name = 'example.jpg'
    painting = NewYearPainting(name="example", type="example_type", image=painting_img, keywords="example_keyword")
    painting.save()
