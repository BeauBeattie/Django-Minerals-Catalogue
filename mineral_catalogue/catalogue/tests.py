from django.test import TestCase
from django.urls import reverse
from django.test import TransactionTestCase


from .models import Mineral


class MineralModelTests(TestCase):
    def test_model_creation(self):
        mineral = Mineral.objects.create(
            name='Vesuvianite',
            image_filename='240px-Vesuvianite.jpg',
            image_caption='Vesuvianite from the Jeffrey Mine in Asbestos, '
                          'Quebec',
            category='Sorosilicate',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            group='Sulfides',
            strunz_classification='09.BG.35',
            crystal_system='Tetragonal 4/m 2/m 2/m',
            unit_cell='a = 15.52 Å, c = 11.82 Å; Z = 2',
            color='Yellow, green, brown; colorless to white, blue, violet, '
                  'bluish green, pink, red, black, commonly zoned',
            crystal_symmetry='Tetragonal 4/m 2/m 2/m',
            cleavage='Poor on {110} and {100} very poor on {001}',
            mohs_scale_hardness='6-7',
            luster='Vitreous to resinous',
            streak='White',
            diaphaneity='Subtransparent to Translucent',
            optical_properties='Uniaxial (-)',
            refractive_index='nω = 1.703 - 1.752 nε = 1.700 - 1.746',
            crystal_habit='Short pyramidal to long prismatic crystals common, '
                          'massive to columnar',
            specific_gravity='7.20 - 7.22',
        )
        self.assertEqual(mineral.name, 'Vesuvianite')


class MineralViewTests(TransactionTestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Test Mineral",
            luster="Test luster"
        )
        self.mineral2 = Mineral.objects.create(
            name="Second test mineral"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('catalogue:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'catalogue/home.html')
        self.assertContains(resp, self.mineral.name)
        # Tests title template tag
        self.assertContains(resp, self.mineral2.name.title())

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('catalogue:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalogue/detail.html')
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertContains(resp, self.mineral.luster)

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('catalogue:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalogue/detail.html')
        self.assertIn(resp.context['mineral'], [self.mineral, self.mineral2])
