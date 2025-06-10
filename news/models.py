from django.db import models

class New(models.Model):

    class Section(models.TextChoices):
        INFORMATION = 'Informations'
        RESOURCES = 'Ressources'
        EVENTS = 'Événements'
        OPPORTUNITIES = 'Opportunités'
        PROFILES ='Profils'
    photo = models.ImageField(default='img/news/default.jpg', blank=True, null=True, upload_to="img/news/")
    section = models.fields.CharField(choices=Section.choices, max_length=15)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    source =models.CharField(max_length=42)
    author =models.CharField(max_length=42)
    website = models.fields.URLField(null=True, blank=True)   
    date = models.DateField(
        auto_now_add=True,
        auto_now=False,
        # argument to give this field a more readable name in the Django administration interface.
        verbose_name="date"
    )
    publicationdate = models.DateTimeField(
        auto_now_add=False,
        auto_now=False,
        verbose_name="Publication date"
    )

    def __str__(self):
        return self.title[:50]



