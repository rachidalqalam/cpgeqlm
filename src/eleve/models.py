from django.db import models

SEXE_CHOICES = (
    ("HOMME", "Homme"),
    ("FEMME", "Femme"),
)

class Annee(models.Model):
    nom = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.nom


class Filiere(models.Model):
    annee = models.ForeignKey(Annee, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.nom

class Module(models.Model):
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.filiere.annee.nom + ' - ' + self.filiere.nom + ' - ' + self.nom

class Eleve(models.Model):
    nom = models.CharField(max_length=50, blank=True)
    prenom = models.CharField(max_length=50, blank=True)
    sexe = models.CharField(max_length=5, choices=SEXE_CHOICES)
    cin = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    telephone_tuteur = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    ville = models.CharField(max_length=20, blank=True)
    adresse = models.CharField(max_length=250, blank=True)
    date_de_naissance = models.DateField(blank=True)
    etablissement = models.CharField(max_length=30, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom + ' ' + self.prenom