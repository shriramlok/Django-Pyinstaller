import json
import os

from PIL import Image
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from torch import max
from torchvision.transforms import transforms

from .apps import PredapiConfig


#what  I need to do is that the image will come in some form as data
@api_view(['POST','GET'])
@parser_classes((MultiPartParser,FormParser,))
def resnet_predict(request):
    response_dict = {}
    if request.method == 'GET':
        
        pass
    elif request.method == 'POST':
        im = request.FILES["image"]
        img = Image.open(im) 
        ds_trans = transforms.Compose([
                                transforms.Resize(224),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize( 
                                    mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225]
                                )])
        img2 = ds_trans(img)
        img2 = img2.unsqueeze(0)
        resnet = PredapiConfig.classifier
        resnet.eval()
        outs = resnet(img2)
        _, index = max(outs, 1)
        index = str(int(index))
        #now labels of Imagenet
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # LABEL_FILE = os.path.join(BASE_DIR,'predAPI/classifier/labels.json')
        # LABEL_FILE = 
        labels_data = open(PredapiConfig.labelfile)
        #labels_data = PredapiConfig.labelfile
        labels = json.load(labels_data)
        #labels = JSONParser.parse(labels_data)
        response_dict = {"index" : index,
                            "prediction" : labels[index][1]}
    return Response(response_dict, status=status.HTTP_201_CREATED)




