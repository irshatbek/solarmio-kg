# Generated by Django 4.1.2 on 2022-10-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_item_title_alter_item_unit_name_alter_item_capacity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Tables',
            new_name='tables',
        ),
        migrations.AddField(
            model_name='item',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], null=True, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='item',
            name='regions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='regions'),
        ),
    ]