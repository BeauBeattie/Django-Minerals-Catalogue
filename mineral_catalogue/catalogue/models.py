from django.db import models


class Mineral(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image_filename = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    strunz_classification = models.CharField(blank=True, max_length=255)
    color = models.CharField(blank=True, max_length=255)
    crystal_system = models.CharField(blank=True, max_length=255)
    unit_cell = models.CharField(blank=True, max_length=255)
    crystal_symmetry = models.CharField(blank=True, max_length=255)
    cleavage = models.CharField(blank=True, max_length=255)
    mohs_scale_hardness = models.CharField(blank=True, max_length=255)
    luster = models.CharField(blank=True, max_length=255)
    streak = models.CharField(blank=True, max_length=255)
    diaphaneity = models.CharField(blank=True, max_length=255)
    optical_properties = models.CharField(blank=True, max_length=255)
    refractive_index = models.CharField(blank=True, max_length=255)
    crystal_habit = models.CharField(blank=True, max_length=255)
    specific_gravity = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name
