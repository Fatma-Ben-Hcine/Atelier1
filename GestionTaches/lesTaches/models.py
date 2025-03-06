from django.db import models 
from datetime import datetime, timedelta, date  
from django.utils.html import format_html  
def get_default_schedule_date(): 

    return datetime.now().date() + timedelta(days=7) 

class Task(models.Model): 
    name = models.CharField(max_length=250)  
    description = models.TextField() 
    created_date = models.DateField(auto_now_add=True)  
    closed = models.BooleanField(default=False)  
    due_date = models.DateField(null=True)  
    schedule_date = models.DateField(default=get_default_schedule_date)  
    def __str__(self): 
        return self.name 
    def mark_as_closed(self): 
        
        self.closed = True 
        self.save() 
    def colored_due_date(self): 
           
            if not self.due_date: 
                return format_html("<span style='color:gray'>Pas de date limite</span>") 
            
            today = date.today() 
            if self.due_date > today + timedelta(days=7): 
                color = "green" 
            elif today <= self.due_date <= today + timedelta(days=7): 
                color = "orange" 
            elif self.due_date < today: 
                color = "red" 
            else: 
                color = "black"  # Cas par défaut 
    
            due_date_str = self.due_date.strftime("%d %B %Y") 
            return format_html("<span style='color:%s'>%s</span>" % (color, due_date_str)) 
    
        # Permet d'utiliser cette méthode comme un champ dans l'admin 
    colored_due_date.short_description = "Date limite (colorée)" 
