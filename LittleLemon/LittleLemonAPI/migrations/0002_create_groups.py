from django.db import migrations
from django.contrib.auth.models import Group, Permission

def create_groups(apps, schema_editor):
    # Create Manager group
    manager_group, created = Group.objects.get_or_create(name='Manager')
    
    # Create Delivery crew group
    delivery_crew_group, created = Group.objects.get_or_create(name='Delivery crew')

class Migration(migrations.Migration):
    dependencies = [
        ('LittleLemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]