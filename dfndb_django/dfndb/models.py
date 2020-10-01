from django.db import models
import idutils # for DOI validation: https://idutils.readthedocs.io/en/latest/
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class DOIField(models.CharField):
   description = "Digital Object Identifier (DOI)"
   def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 128;
        super(DOIField, self).__init__(*args, **kwargs)
   def validate(self, value, obj):
        super().validate(value, obj)
        if not idutils.is_doi(value):
           raise ValidationError(
              _('%(value)s is not a valid DOI'),
               params={'value': value},
           )
   def get_url(self):
     pass      # implement a method to resolve the URL of a DOI
   def get_name(self):
     pass      # implement a method to fetch the document name

class YearField(models.IntegerField):
   def __init__(self, *args, **kwargs):
      super(YearField, self).__init__(*args, **kwargs)
   def validate(self, value, obj):
      super().validate(value, obj)
      if (value < 1791 or value > datetime.date.today().year):
         raise ValidationError("Invalid year")

# over-normalisation, don't need a full contact info DB
#class Person(models.Model):
#   name = models.CharField()
   
class Paper(models.Model):
  DOI = DOIField(null=False, unique=True)
  paper_tag = models.SlugField(max_length=100, unique=True)  # SlugField is a CharField with validation, like my DOIField
  year = YearField(default=datetime.date.today().year)
  title = models.CharField(max_length=300)
  #authors = models.ManyToManyField(
  authors = models.CharField(max_length=500)
  url = models.URLField(null=True, blank=True)
  created_on = models.DateField(auto_now_add=True)
  accepted = models.BooleanField(default=False)

  def __str__(self):
    return self.paper_tag

# I don't like Material having a column for each chemical compound - that seems nasty.
# Instead I will use one of Django's special ManyToManyFields with a "Through" relationship.
# This specifies the table a mapping table with an extra column for the composition number
# actually, don't even need a "through" for this.

class Compound(models.Model):
  formula = models.CharField(max_length=20, unique=True) #  "Li"
  name = models.CharField(max_length=100, unique=True) #  "Lithium"
  def __str__(self):
    return "%s (%s)"%(self.name,self.formula)

class CompositionPart(models.Model):
  compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
  amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
  def __str__(self):
    return "%s%d"%(self.compound.formula,self.amount)

class Material(models.Model):
  name =  models.CharField(max_length=100, unique=True)
  composition = models.ManyToManyField(CompositionPart)
  polymer = models.IntegerField(default=0,validators=[MinValueValidator(0)])
  created_on = models.DateField(auto_now_add=True)
  accepted = models.BooleanField(default=False)
  def __str__(self):
    return self.name


