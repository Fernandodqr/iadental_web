from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from requests import request
from rest_framework import viewsets, status
from apps.ObjDetectAPI.serializers import UserSerializers, DetectionSerializers, PacienteSerializers, ImagensSerializers
from .models import Detection
from apps.pacientes.models import Paciente
from apps.imagens.models import Imagens
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
# Import utilites
sys.path.append("..")
#from object_detection.utils import label_map_util
from utils import label_map_util
#from object_detection.utils import visualization_utils as vis_util
from utils import visualization_utils as vis_util

class APIView(View):
    def get(self, request, *args, **Kwargs):
        return HttpResponse('Hello')

class DetectionView(viewsets.ModelViewSet):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializers
#    authentication_classes = (TokenAuthentication,)
#    permission_classes = (IsAuthenticated,)

@api_view(['POST',])
def api_detection_view(request):
        detection = Detection.objects.all()

        if request.method == 'POST':
            serializer = DetectionSerializers

            MODEL_NAME = 'inference_graph'
            IMAGE_NAME = 'P10.jpg'

            CWD_PATH = os.getcwd()

            PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
            PATH_TO_LABELS = os.path.join(CWD_PATH, 'training', 'labelmap.pbtxt')
            PATH_TO_IMAGE = os.path.join(CWD_PATH, IMAGE_NAME)

            NUM_CLASSES = 3

            label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
            categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                                            use_display_name=True)
            category_index = label_map_util.create_category_index(categories)

            detection_graph = tf.Graph()
            with detection_graph.as_default():
                od_graph_def = tf.GraphDef()
                with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                    serialized_graph = fid.read()
                    od_graph_def.ParseFromString(serialized_graph)
                    tf.import_graph_def(od_graph_def, name='')

                sess = tf.Session(graph=detection_graph)

            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            image = cv2.imread(PATH_TO_IMAGE)
            image_expanded = np.expand_dims(image, axis=0)

            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_expanded})

            vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.60)

            cv2.imshow('Object detector', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            serializer.save()

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def external(request):
    paciente = Paciente.get(id=id)

    MODEL_NAME = 'inference_graph'
    IMAGE_NAME = 'P10.jpg'

    CWD_PATH = os.getcwd()

    PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
    PATH_TO_LABELS = os.path.join(CWD_PATH, 'training', 'labelmap.pbtxt')
    PATH_TO_IMAGE = os.path.join(CWD_PATH, IMAGE_NAME)

    NUM_CLASSES = 3

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                                use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    image = cv2.imread(PATH_TO_IMAGE)
    image_expanded = np.expand_dims(image, axis=0)

    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})

    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    cv2.imshow('Object detector', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return render(request, 'index.html', {'paciente': paciente})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializers

class ImagensViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializers

