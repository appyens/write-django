from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Genre(models.Model):
    """
    Genre mapping for book model
    """
    genre = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Object representation
        """
        return self.genre


class Language(models.Model):
    """
    Language table definition
    """
    language = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Object representation
        """
        return self.language


class Author(models.Model):
    """
    Author table definition
    """
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256)
    slug = models.SlugField(blank=True)
    dob = models.DateField(blank=True, null=True)
    death = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    wikipedia = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        """
        Object representation
        """
        return self.fullname

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
            super().save(**kwargs)


class Publisher(models.Model):
    """
    Book publisher table schema
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book table schema
    """
    title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    edition = models.SmallIntegerField(default=1)
    pages = models.IntegerField(blank=True)
    year = models.IntegerField(blank=True)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, related_name='books')
    description = models.TextField(max_length=1000)
    isbn = models.CharField(verbose_name='ISBN', max_length=13, blank=True)
    isbn_13 = models.CharField(verbose_name='ISBN-13',  max_length=17, blank=True)
    store_link = models.URLField(blank=True)
    wikipedia = models.URLField(blank=True)
    front_cover = models.ImageField(upload_to='book/covers/front/', blank=True)
    back_cover = models.ImageField(upload_to='book/covers/back/', blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created_on'

    def __str__(self):
        """
        Object representation
        """
        return self.title

    def get_absolute_url(self):
        """
        Create url for model instance
        :return:
        """
        return reverse('book:book_detail', args=[self.slug])

    def save(self, **kwargs):
        """
        Custom save implementation
        :param kwargs:
        :return:
        """
        if not self.slug:
            self.slug = slugify(self.title)
            super(Book, self).save(**kwargs)

    @classmethod
    def total_books(cls):
        """
        Get total book instance count
        :return:
        """
        return cls.objects.count()


