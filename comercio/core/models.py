from django.db import models

#Model da categoria
class Categoria(models.Model):
    titulo = models.CharField(max_length = 300)
    categoriaPrimaria = models.BooleanField(default = False)

    def __str__(self):
        return self.titulo

#Model do produto
class Produto(models.Model):
    mainimage = models.ImageField(upload_to='produtos/', blank=True)
    nome = models.CharField(max_length=300)
    slug = models.SlugField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    previa_texto = models.TextField(max_length=200, verbose_name='Prévia do texto')
    texto_detalhado = models.TextField(max_length=1000, verbose_name='Texto detalhado')
    preco = models.FloatField()

    def __str__(self):
        return self.name
