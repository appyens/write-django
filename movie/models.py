from django.db import models

# Create your models here.


class GenreModel(models.Model):
    """
    Genre mapping for book model
    """
    genre = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Object representation
        """
        return self.genre


class CountryModel(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class LanguageModel(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class PersonModel(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Male')
    )
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    gender = models.CharField(max_length=128, choices=GENDERS)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)


class MovieModel(models.Model):
    RESOLUTION = (
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )

    RATINGS = (
        ('UNRATED', 'NR - Not Rate'),
        ('G', 'G - General Audiences'),
        ('PG', 'PG – Parental Guidance Suggested'),
        ('PG13', 'PG-13 – Parents Strongly Cautioned'),
        ('R', 'R – Restricted'),
        ('NC17', 'NC-17 – Adults Only'),
        ('A', 'A – Adults Only'),
        ('UA', 'Indian - UA'),
    )

    title = models.CharField(max_length=256)
    slug = models.SlugField()
    resolution = models.CharField(max_length=128, choices=RESOLUTION)
    rating = models.CharField(max_length=128, choices=RATINGS)
    country = models.ForeignKey(CountryModel, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(LanguageModel, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(to=GenreModel, on_delete=models.DO_NOTHING)
    year = models.IntegerField()
    plot = models.TextField()
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    director = models.ForeignKey(
        to=PersonModel,
        on_delete=models.SET_NULL,
        related_name='directed',
        null=True, blank=True)
    writers = models.ManyToManyField(
        to=PersonModel, related_name='writing_credits', blank=True)
    actors = models.ManyToManyField(
        to=PersonModel, through='RoleModel', related_name='acting_credits', blank=True)
    imdb_link = models.URLField()
    wikipedia = models.URLField()
    poster = models.ImageField(upload_to='movie/poster/%s' % slug)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class RoleModel(models.Model):
    movie = models.ForeignKey(MovieModel, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(PersonModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    class Meta:
        unique_together = ('movie', 'person', 'name')

    def __str__(self):
        return "{} {} {}".format(self.movie.id, self.person.id, self.name)
