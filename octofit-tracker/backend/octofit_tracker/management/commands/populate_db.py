from django.core.management.base import BaseCommand
from octofit_tracker.models.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data, skip objects with id=None
        for obj in User.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.id is not None:
                obj.delete()

        # Create teams
        marvel = Team(name='Marvel', description='Marvel Superheroes')
        marvel.save()
        dc = Team(name='DC', description='DC Superheroes')
        dc.save()

        # Create users
        users = []
        u1 = User(name='Iron Man', email='ironman@marvel.com', team=marvel)
        u1.save()
        users.append(u1)
        u2 = User(name='Captain America', email='cap@marvel.com', team=marvel)
        u2.save()
        users.append(u2)
        u3 = User(name='Thor', email='thor@marvel.com', team=marvel)
        u3.save()
        users.append(u3)
        u4 = User(name='Superman', email='superman@dc.com', team=dc)
        u4.save()
        users.append(u4)
        u5 = User(name='Batman', email='batman@dc.com', team=dc)
        u5.save()
        users.append(u5)
        u6 = User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
        u6.save()
        users.append(u6)

        # Create activities
        a1 = Activity(user=users[0], type='Running', duration=30, calories=300, date='2025-12-10')
        a1.save()
        a2 = Activity(user=users[3], type='Swimming', duration=45, calories=400, date='2025-12-09')
        a2.save()

        # Create workouts
        w1 = Workout(name='Pushups', description='Upper body', suggested_for='All')
        w1.save()
        w2 = Workout(name='Cardio', description='Heart health', suggested_for='Marvel')
        w2.save()

        # Create leaderboard
        l1 = Leaderboard(team=marvel, points=150, rank=1)
        l1.save()
        l2 = Leaderboard(team=dc, points=120, rank=2)
        l2.save()

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
