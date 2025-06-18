# users/management/commands/populate_db.py

import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Nationalities, Categories, Clubs, Disciplines, Events, Coaches, Athletes, Participations, Trainings, Injuries, MedicalHistory
from users.models import CustomUser

# --- DATOS COMPLETOS DE TUS SCRIPTS ---
NATIONALITIES_DATA = ['United States', 'Brazil', 'Spain', 'Kenya', 'Jamaica', 'China', 'Germany', 'Australia', 'Japan', 'Canada']
CATEGORIES_DATA = [('Youth', 14, 17), ('Junior', 18, 20), ('Senior', 21, 35), ('Masters', 36, 50), ('Veteran', 51, 65)]
CLUBS_DATA = [
    ('Eagle Athletics Club', 'New York', 'United States'), ('Samba Runners', 'Rio de Janeiro', 'Brazil'),
    ('Madrid Speedsters', 'Madrid', 'Spain'), ('Nairobi Marathoners', 'Nairobi', 'Kenya'),
    ('Kingston Sprinters', 'Kingston', 'Jamaica'), ('Beijing Aquatic Club', 'Beijing', 'China'),
    ('Berlin Throwers', 'Berlin', 'Germany'), ('Sydney Track Team', 'Sydney', 'Australia'),
    ('Tokyo Jumpers', 'Tokyo', 'Japan'), ('Toronto Cyclists', 'Toronto', 'Canada')
]
DISCIPLINES_DATA = ['100m Dash', '200m Dash', 'Marathon', 'Long Jump', 'High Jump', 'Shot Put', '100m Freestyle Swim', 'Road Cycling']
EVENTS_DATA = [
    ('National Championships 2025', '2025-06-15', 'New York, United States'), ('Rio Carnival Run', '2025-04-10', 'Rio de Janeiro, Brazil'),
    ('Madrid Spring Classic', '2025-05-05', 'Madrid, Spain'), ('Nairobi City Marathon', '2025-07-20', 'Nairobi, Kenya'),
    ('Kingston Invitational', '2025-03-22', 'Kingston, Jamaica'), ('Beijing Aquatic Games', '2025-08-12', 'Beijing, China'),
    ('Berlin Throwdown', '2025-09-01', 'Berlin, Germany'), ('Sydney Speed Fest', '2025-11-10', 'Sydney, Australia')
]
COACHES_DATA = [('John Smith', 'Sprinting'), ('Maria Silva', 'Distance Running'), ('Liu Wei', 'Swimming Techniques'), ('Thomas Müller', 'Strength Training'), ('Aisha Kimani', 'Endurance Coaching')]
ATHLETES_DATA = [
    'Andrew Torres', 'Michael Gomez', 'Jorge Heath', 'Daniel Brewer', 'Christina Mueller', 'Joseph Montoya', 'Kevin Villa', 'Morgan Wagner',
    'Robert Dyer DVM', 'Jeffrey Hahn', 'Linda Sanders', 'Marissa Jones', 'Cameron Alexander', 'Michael Riddle', 'Cory Donovan', 'James Horn',
    'Natalie Marsh DDS', 'Latoya Vaughn', 'John Nolan', 'Alicia Wilson', 'Rebecca Perry', 'Sandra Taylor', 'Kimberly Ford', 'Cassandra Hicks',
    'Cheryl Case', 'Ashley Jones', 'Michele Gonzalez', 'Beth Hogan', 'Daniel Barajas', 'Monica Michael', 'Kimberly Wu', 'Kelly Wright',
    'Sabrina Wright', 'Debra Ross', 'April Melendez', 'Ronald Delgado', 'Dustin Beard', 'Shannon Anderson', 'Megan Miller', 'Ronald Jones',
    'Cristina Kelly', 'James West MD', 'Stephen Butler', 'Richard Lee', 'Ryan Best', 'Lisa Austin', 'Elizabeth Frost', 'Joseph Watson',
    'Melissa Morris', 'Jose Cordova', 'Leslie Smith', 'Amanda Thomas', 'Michael Ellis', 'Ariana Liu', 'Sandra Carter', 'Kelly Conley',
    'Joseph Mason', 'Brendan Hernandez', 'Gary Fernandez', 'Robert Adams', 'Jerry Moore', 'Krystal Blair', 'Adam Sanchez', 'Bridget Perkins',
    'Joseph Thomas', 'Jessica Miles', 'Douglas Chen', 'Beth Austin', 'Joseph Smith', 'Michael Daniels', 'William Morgan', 'Renee Wheeler',
    'Luis Smith', 'Jamie Williams', 'Lindsey Hill', 'Christina Todd', 'Debra Ortiz', 'Kelly Hamilton', 'Cristina Smith', 'Clinton Vargas',
    'Kimberly Hicks', 'John Fleming', 'Jeremy Powell', 'Stephanie Santiago', 'Joel Rios', 'Brian Clark', 'Jason Parsons', 'Amy Shannon',
    'Aaron Henderson', 'Kenneth Smith', 'Jill Ramirez', 'Jason Mitchell', 'Jonathan Schmitt', 'Christopher Allen', 'Christopher Gilbert',
    'Miss Patricia Smith', 'Tyler Greene', 'Tanya Edwards', 'Andrew Hughes', 'Terry Austin'
]
USERS_DATA = [
    {'username': 'johnsonjoshua', 'role': 'athlete'}, {'username': 'thomas26', 'role': 'athlete'}, {'username': 'crescencia31', 'role': 'athlete'},
    {'username': 'fernandosevilla', 'role': 'athlete'}, {'username': 'qcocci', 'role': 'coach'}, {'username': 'dwright', 'role': 'athlete'},
    {'username': 'natalia93', 'role': 'admin'}, {'username': 'wbohnbach', 'role': 'admin'}, {'username': 'christophemaillot', 'role': 'admin'},
    {'username': 'mjesus', 'role': 'coach'}, {'username': 'rogerpinto', 'role': 'coach'}, {'username': 'robinsonarthur', 'role': 'athlete'},
    {'username': 'brianromero', 'role': 'admin'}, {'username': 'tygo51', 'role': 'athlete'}, {'username': 'gracia12', 'role': 'admin'},
    {'username': 'maria-manuela24', 'role': 'athlete'}, {'username': 'griseldacalderon', 'role': 'athlete'}, {'username': 'de-haasnora', 'role': 'athlete'},
    {'username': 'antoine14', 'role': 'coach'}, {'username': 'chartiervincent', 'role': 'athlete'}, {'username': 'stoffelszmaurits', 'role': 'athlete'},
    {'username': 'helmuth32', 'role': 'athlete'}, {'username': 'jbenigni', 'role': 'admin'}, {'username': 'maria-dolores87', 'role': 'coach'},
    {'username': 'martinemily', 'role': 'admin'}, {'username': 'amanda70', 'role': 'coach'}, {'username': 'nverbruggen', 'role': 'admin'},
    {'username': 'gilbertreynaud', 'role': 'admin'}, {'username': 'claudiomanzoni', 'role': 'coach'}, {'username': 'liviatrentin', 'role': 'admin'},
    {'username': 'ljunk', 'role': 'coach'}, {'username': 'siempeterse', 'role': 'coach'}, {'username': 'guilherme34', 'role': 'admin'},
    {'username': 'herrmannthekla', 'role': 'coach'}, {'username': 'ljordan', 'role': 'admin'}, {'username': 'kevintrapp', 'role': 'athlete'},
    {'username': 'scott74', 'role': 'coach'}, {'username': 'llettiere', 'role': 'coach'}, {'username': 'brandon16', 'role': 'admin'},
    {'username': 'milovan-der-zijl', 'role': 'coach'}, {'username': 'selinavan-de-pavert', 'role': 'coach'}, {'username': 'usantoro', 'role': 'athlete'},
    {'username': 'noortje17', 'role': 'athlete'}, {'username': 'williamsonjimmy', 'role': 'athlete'}, {'username': 'kescolano', 'role': 'coach'},
    {'username': 'felicia64', 'role': 'admin'}, {'username': 'matthieu39', 'role': 'admin'}, {'username': 'robin74', 'role': 'admin'},
    {'username': 'rzijlmans', 'role': 'admin'}, {'username': 'arcosmarco', 'role': 'coach'}, {'username': 'paganinigian', 'role': 'admin'},
    {'username': 'lillyrosemann', 'role': 'admin'}, {'username': 'odescalchimonica', 'role': 'coach'}, {'username': 'araujomaria-luiza', 'role': 'athlete'},
    {'username': 'ycabezas', 'role': 'admin'}, {'username': 'clementeric', 'role': 'admin'}, {'username': 'ermannosonnino', 'role': 'coach'},
    {'username': 'escuderoruth', 'role': 'admin'}, {'username': 'daviesabdul', 'role': 'coach'}, {'username': 'maria-fernandacervantes', 'role': 'coach'},
    {'username': 'tallen', 'role': 'athlete'}, {'username': 'ross52', 'role': 'athlete'}, {'username': 'omoraleda', 'role': 'coach'},
    {'username': 'salgaripaloma', 'role': 'coach'}, {'username': 'sina46', 'role': 'athlete'}, {'username': 'mauriziomastroianni', 'role': 'admin'},
    {'username': 'kyle35', 'role': 'admin'}, {'username': 'rfonseca', 'role': 'athlete'}, {'username': 'mcastro', 'role': 'coach'},
    {'username': 'richard60', 'role': 'admin'}, {'username': 'da-cunhapedro', 'role': 'athlete'}, {'username': 'kellysmith', 'role': 'athlete'},
    {'username': 'palaumodesta', 'role': 'coach'}, {'username': 'caiovieira', 'role': 'coach'}, {'username': 'flavio77', 'role': 'coach'},
    {'username': 'acostarhonda', 'role': 'admin'}, {'username': 'michael90', 'role': 'coach'}, {'username': 'geraldine73', 'role': 'athlete'},
    {'username': 'nadiapardo', 'role': 'admin'}, {'username': 'lucianoborgia', 'role': 'coach'}, {'username': 'emanuel43', 'role': 'athlete'},
    {'username': 'larapinto', 'role': 'admin'}, {'username': 'ninthe55', 'role': 'admin'}, {'username': 'dmoraes', 'role': 'coach'},
    {'username': 'sofialamas', 'role': 'coach'}, {'username': 'nicole52', 'role': 'athlete'}, {'username': 'corinne88', 'role': 'admin'},
    {'username': 'rcomisso', 'role': 'athlete'}, {'username': 'whitney78', 'role': 'coach'}, {'username': 'ybailey', 'role': 'coach'},
    {'username': 'derrick99', 'role': 'coach'}, {'username': 'mitchell01', 'role': 'athlete'}, {'username': 'danielroland', 'role': 'admin'},
    {'username': 'glaunay', 'role': 'athlete'}, {'username': 'davirios', 'role': 'coach'}, {'username': 'zvan-der-loo', 'role': 'admin'},
    {'username': 'melissa71', 'role': 'athlete'}, {'username': 'williamsmelvin', 'role': 'admin'}, {'username': 'diego28', 'role': 'admin'},
    {'username': 'xbonneau', 'role': 'admin'}
]

class Command(BaseCommand):
    help = 'Populates the database with initial data from scripts.'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        # Limpia en orden inverso para evitar problemas de claves foráneas
        CustomUser.objects.filter(is_superuser=False).delete()
        Trainings.objects.all().delete()
        Participations.objects.all().delete()
        MedicalHistory.objects.all().delete()
        Injuries.objects.all().delete()
        Athletes.objects.all().delete()
        Coaches.objects.all().delete()
        Events.objects.all().delete()
        Disciplines.objects.all().delete()
        Clubs.objects.all().delete()
        Categories.objects.all().delete()
        Nationalities.objects.all().delete()

        self.stdout.write("Populating independent tables...")
        nationalities = [Nationalities.objects.create(name=name) for name in NATIONALITIES_DATA]
        categories = [Categories.objects.create(name=name, min_age=min_age, max_age=max_age) for name, min_age, max_age in CATEGORIES_DATA]
        clubs = [Clubs.objects.create(name=name, city=city, country=country) for name, city, country in CLUBS_DATA]
        disciplines = [Disciplines.objects.create(name=name) for name in DISCIPLINES_DATA]
        events = [Events.objects.create(name=name, date=date, location=location) for name, date, location in EVENTS_DATA]
        coaches = [Coaches.objects.create(name=name, specialty=specialty) for name, specialty in COACHES_DATA]

        self.stdout.write("Populating athletes...")
        athletes_list = []
        for athlete_name in ATHLETES_DATA:
            athlete = Athletes.objects.create(
                name=athlete_name,
                birth_date=f"{random.randint(1960, 2009)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                gender=random.choice(['Male', 'Female', 'Other']),
                nationality=random.choice(nationalities),
                category=random.choice(categories),
                club=random.choice(clubs)
            )
            athletes_list.append(athlete)
        
        available_athletes_for_users = list(athletes_list)

        self.stdout.write("Populating users...")
        for user_data in USERS_DATA:
            user = CustomUser.objects.create_user(
                username=user_data['username'],
                email=f"{user_data['username']}@athletica.com",
                password='password123',
                role=user_data['role']
            )

            if user.role == 'admin':
                user.is_staff = True
                user.save()
            elif user.role == 'athlete':
                if available_athletes_for_users:
                    assigned_athlete = random.choice(available_athletes_for_users)
                    user.athlete = assigned_athlete
                    user.save()
                    available_athletes_for_users.remove(assigned_athlete)
            elif user.role == 'coach':
                user.coach = random.choice(coaches)
                user.save()
        
        self.stdout.write("Populating dependent tables (Injuries, Trainings, etc.)...")
        
        for i in range(15):
            Injuries.objects.create(
                athlete=random.choice(athletes_list),
                description=random.choice(['Strained hamstring', 'Ankle sprain', 'Shin splints', 'Lower back pain']),
                date=date.today() - timedelta(days=random.randint(10, 365)),
                estimated_duration_days=random.choice([14, 21, 30, 45, 60])
            )
            
        for i in range(10):
            MedicalHistory.objects.create(
                athlete=random.choice(athletes_list),
                date=date.today() - timedelta(days=random.randint(30, 500)),
                observations=random.choice(['Routine check-up, all clear.', 'Recovered from minor injury.', 'Physiotherapy recommended.'])
            )

        training_types = ['Sprint drills','Endurance run','Gym strength','Flexibility','Agility circuit','Interval training','Technical skills']
        for i in range(100):
            Trainings.objects.create(
                athlete=random.choice(athletes_list),
                coach=random.choice(coaches),
                date=date.today() - timedelta(days=random.randint(1, 60)),
                duration_minutes=random.randint(30, 120),
                training_type=random.choice(training_types)
            )

        for i in range(100):
            result_time = f"{random.randint(9, 20):02d}.{random.randint(0, 99):02d}s"
            Participations.objects.create(
                athlete=random.choice(athletes_list),
                event=random.choice(events),
                discipline=random.choice(disciplines),
                result=result_time,
                position=random.randint(1, 50)
            )

        self.stdout.write(self.style.SUCCESS('Database successfully populated! All tables are filled.'))