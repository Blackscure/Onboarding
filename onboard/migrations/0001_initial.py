# Generated by Django 4.2.7 on 2023-11-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('business_name', models.CharField(max_length=100)),
                ('business_categories', models.CharField(choices=[('Fintech', 'Fintech'), ('Learning Institution', 'Learning Institution'), ('Transportation', 'Transportation')], max_length=100)),
                ('business_registration_date', models.DateField()),
                ('county', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Bungoma', 'Bungoma'), ('Kiambu', 'Kiambu'), ('Nyanza', 'Nyanza')], max_length=100)),
                ('sub_county', models.CharField(choices=[('Westlands', 'Westlands'), ('Dagoretti North', 'Dagoretti North'), ('Dagoretti South', 'Dagoretti South'), ('Langata', 'Langata'), ('Kibra', 'Kibra'), ('Changamwe', 'Changamwe'), ('Jomvu', 'Jomvu'), ('Kisauni', 'Kisauni'), ('Nyali', 'Nyali'), ('Likoni', 'Likoni'), ('Mvita', 'Mvita'), ('Bungoma East', 'Bungoma East'), ('Bungoma West', 'Bungoma West'), ('Bungoma North', 'Bungoma North'), ('Mount Elgon', 'Mount Elgon'), ('Sirisia', 'Sirisia'), ('Kimilili', 'Kimilili'), ('Tongaren', 'Tongaren'), ('Webuye East', 'Webuye East'), ('Webuye West', 'Webuye West'), ('Kanduyi', 'Kanduyi'), ('Kiambu', 'Kiambu'), ('Kiambaa', 'Kiambaa'), ('Ruiru', 'Ruiru'), ('Kabete', 'Kabete'), ('Gatundu South', 'Gatundu South'), ('Gatundu North', 'Gatundu North'), ('Thika Town', 'Thika Town'), ('Juja', 'Juja'), ('Lari', 'Lari'), ('Kikuyu', 'Kikuyu'), ('Limuru', 'Limuru'), ('Githunguri', 'Githunguri')], max_length=100)),
                ('ward', models.CharField(choices=[('Parklands/Highridge', 'Parklands/Highridge'), ('Karura', 'Karura'), ('Kangemi', 'Kangemi'), ('Mountain View', 'Mountain View'), ('Kitisuru', 'Kitisuru'), ('Loresho', 'Loresho'), ('Lavington', 'Lavington'), ('Kyuna', 'Kyuna'), ('Spring Valley', 'Spring Valley'), ('Airport', 'Airport'), ('Changamwe', 'Changamwe'), ('Chaani', 'Chaani'), ('Jomvu Kuu', 'Jomvu Kuu'), ('Miritini', 'Miritini'), ('Magongo', 'Magongo'), ('Mikindani', 'Mikindani'), ('Bokoli', 'Bokoli'), ('Ndivisi', 'Ndivisi'), ('Webuye East', 'Webuye East'), ('Webuye West', 'Webuye West'), ('Cheptais', 'Cheptais'), ('Mount Elgon', 'Mount Elgon'), ('Lwandanyi', 'Lwandanyi'), ('Sirisia', 'Sirisia'), ('Namwela', 'Namwela'), ('Maeni', 'Maeni'), ('Kimilili', 'Kimilili'), ('Kamukuywa/Kaptama', 'Kamukuywa/Kaptama'), ('Milima', 'Milima'), ('Tongaren', 'Tongaren'), ('Marakaru/Tuuti', 'Marakaru/Tuuti'), ('Matulo', 'Matulo'), ('Webuye East', 'Webuye East'), ('Kabuchai/Chwele', 'Kabuchai/Chwele'), ('Bukembe West', 'Bukembe West'), ('Bukembe East', 'Bukembe East'), ('Bwake/Luuya', 'Bwake/Luuya'), ('Kanduyi', 'Kanduyi'), ('Bwake/Luuya', 'Bwake/Luuya'), ('Bukembe West', 'Bukembe West'), ('Bukembe East', 'Bukembe East')], max_length=100)),
                ('building_name', models.CharField(max_length=100)),
                ('floor', models.CharField(max_length=100)),
            ],
        ),
    ]
