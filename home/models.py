from django.db import models

class VisitCounter(models.Model):
    visits = models.IntegerField(default=0)

    def __str__(self):
        return f"Visits: {self.visits}"
