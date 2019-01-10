from django.shortcuts import render
import json
from .models import Mineral
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
import random


def make_minerals(mineral):
    fields = {
        'name': None,
        'image filename': None,
        'image caption': None,
        'category': None,
        'formula': None,
        'group': None,
        'strunz classification': None,
        'crystal system': None,
        'unit cell': None,
        'color': None,
        'crystal symmetry': None,
        'cleavage': None,
        'mohs scale hardness': None,
        'luster': None,
        'streak': None,
        'diaphaneity': None,
        'optical properties': None,
        'refractive index': None,
        'crystal habit': None,
        'specific gravity': None,
    }
    for key, value in mineral.items():
        fields[key] = value
    return fields


def add_to_database():
    with open('minerals.json', encoding='utf-8') as file:
        minerals = json.load(file)
        for mineral in minerals:
            try:
                fields = make_minerals(mineral)
                Mineral(
                    name=fields['name'],
                    image_filename=fields['image filename'],
                    image_caption=fields['image caption'],
                    category=fields['category'],
                    formula=fields['formula'],
                    group=fields['group'],
                    strunz_classification=fields['strunz classification'],
                    crystal_system=fields['crystal system'],
                    unit_cell=fields['unit cell'],
                    color=fields['color'],
                    crystal_symmetry=fields['crystal symmetry'],
                    cleavage=fields['cleavage'],
                    mohs_scale_hardness=fields['mohs scale hardness'],
                    luster=fields['luster'],
                    streak=fields['streak'],
                    diaphaneity=fields['diaphaneity'],
                    optical_properties=fields['optical properties'],
                    refractive_index=fields['refractive index'],
                    crystal_habit=fields['crystal habit'],
                    specific_gravity=fields['specific gravity']
                ).save()
            except IntegrityError:
                continue


def home(request):
    add_to_database()
    minerals = Mineral.objects.all()
    return render(request, 'catalogue/home.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'catalogue/detail.html', {'mineral': mineral})


def random_detail(request):
    all_minerals = Mineral.objects.all()
    mineral = random.choice(all_minerals)
    return render(request, 'catalogue/detail.html', {'mineral': mineral})
