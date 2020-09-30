from django.db import models

# Create your models here.
class model_pizza(models.Model):
	cod_pizza = models.AutoField(primary_key=True)
	sabor = models.CharField(blank=True, max_length=30)
	preco = models.DecimalField(decimal_places=2, max_digits=5)
	descricao = models.TextField()
	Foto = models.ImageField(upload_to='fotos/')

	def __str__(self):
		return self.sabor