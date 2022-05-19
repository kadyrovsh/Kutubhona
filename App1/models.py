from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=10)
    guvohnoma = models.CharField(max_length=10, blank=True)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    bitiruvchi = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.ism} {self.guruh}"

class Muallif(models.Model):
    Jins = (
        ("Erkak","Erkak"),
        ("Ayol","Ayol"),
    )
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    kitoblar_soni = models.SmallIntegerField(default=1)
    trik = models.BooleanField()
    jins = models.CharField(choices=Jins, max_length=5)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=20)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.nom}"

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sana = models.DateField()
    qaytardi = models.CharField(max_length=5, choices=(("Ha","Ha"),("Yo'q","Yo'q")))
    qaytarish_sana = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.student.ism


