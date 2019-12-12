from django.conf.global_settings import MEDIA_URL
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (ListView, UpdateView, DeleteView, CreateView)
from django.views.generic.detail import DetailView
from .models import Paciente, Clinica
from apps.imagens.models import Imagens
# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'        # Teste FERNANDO (12/12/2019): Tensorflow allocation memory
import sys
# imports pdf report
import io
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

# Import utilites
sys.path.append("..")
from utils import label_map_util
from utils import visualization_utils as vis_util


class PacientesList(ListView):
    model = Paciente

    def get_queryset(self):
        clinica_logada = self.request.user.paciente.clinicas
        return Paciente.objects.filter(clinicas=clinica_logada)

#def EditDetect(request):
#    return render(request, 'pacientes/paciente_edita_achado.html')

#class PacienteEdit(UpdateView):
#    model = Paciente
#    fields = '__all__'
#    success_url = 'pacientes/'

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = '__all__'
    success_url = '/pacientes'

class PacienteDelete(DeleteView):
    model = Paciente


#    success_url = reverse_lazy('list_pacientes')

class PacienteNovo(CreateView):
    model = Paciente
    fields = '__all__'

    def form_valid(self, form):
        paciente = form.save(commit=False)
        username = paciente.nome.split(' ')[0] + \
                   paciente.nome.split(' ')[-1]
        paciente.clinicas = self.request.user.paciente.clinicas
        paciente.user = User.objects.create(username=username)
        paciente.save()
        #return super(PacienteNovo, self).form_valid(form)
        return redirect('list_pacientes')

class PacienteDetail(DetailView):
    model = Paciente

def detect(request, id):
    imagens = Imagens.objects.get(id=id)
    paciente = Paciente

    arq = imagens.arquivo.url           # TESTE FERNANDO
    img = arq.split('/')                # TESTE FERNANDO
    IMAGE_NAME_NEW = img[3]             # TESTE FERNANDO

    MODEL_NAME = 'inference_graph'
    IMAGE_NAME = 'P11.jpg'

    CWD_PATH = os.getcwd()

    PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
    PATH_TO_LABELS = os.path.join(CWD_PATH, 'training', 'labelmap.pbtxt')
    PATH_TO_IMAGE = os.path.join(CWD_PATH, 'media', 'imagens', IMAGE_NAME_NEW)

    NUM_CLASSES = 3

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                                use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.compat.v1.Session(graph=detection_graph)

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

    # Fernando: Imprime LABELs and SCORES (01/12/19)
    print([category_index.get(value) for index, value in enumerate(classes[0]) if scores[0, index] > 0.5])
    threshold = 0.5  # in order to get higher percentages you need to lower this number; usually at 0.01 you get 100% predicted objects
    print(len(np.where(scores[0] > threshold)[0]) / num_detections[0])
    # The following code replaces the 'print ([category_index...' statement
    global achados
    achados = []
    for index, value in enumerate(classes[0]):
        object_dict = {}
        if scores[0, index] > threshold:
            object_dict[(category_index.get(value)).get('name').encode('utf8')] = \
                '{}%'.format(int(100*scores[0, index]))
            achados.append(object_dict)
    print('Teste: ', achados)

    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    DETECT_NAME = 'analise.png'
    PATH_TO_DETECT = os.path.join(CWD_PATH, 'media', 'detection', DETECT_NAME)
    cv2.imwrite(PATH_TO_DETECT, image)


    #cv2.imshow('Object detector', image)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

    #return render(request, 'edita-achado.html', { 'imagens':imagens})
    return render(request, 'pacientes/paciente_edita_achado.html', {'paciente': paciente, 'imagens': imagens, 'achados': achados})

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Erros Rendering PDF", status=400)

class Pdf(View):
    def get(self, request):
        #imagens = Imagens.objects.get(id=id)
        paciente = Paciente
        params = {
            'achados': achados,
            #'paciente': Paciente.objects.get(id=id),
            'paciente': Paciente.objects.filter(),
            'nomee': Paciente,
            'request': request,
        }
        return Render.render('pacientes/laudo.html', params, 'mylaudo')


