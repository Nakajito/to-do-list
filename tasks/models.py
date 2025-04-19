from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Titulo',
        help_text='Titulo de la tarea',
        )
    
    is_completed = models.BooleanField(
        default=False,
        verbose_name='¿Tarea completada?',
        help_text='Si la tarea esta completa',
        )
    
    created_at = models.DateField(
        verbose_name='Fecha de creación',
        help_text = 'Es la fecha en que se creó la tarea',
        auto_now_add=True
        )
    
    due_to = models.DateField(
        verbose_name='Fecha limite',
        help_text = 'Coloca la fecha limite para completar la actividad'
        )
    
    description = models.TextField(
        verbose_name='Descripción',
        help_text='Descrición de la tarea'
    )
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = [ 'is_completed', 'created_at', ]
        
    
    def __str__(self):
        return f'{self.title} - Completada ({self.created_at})' if self.is_completed else f'{self.title} - Pendiente ({self.created_at})' 