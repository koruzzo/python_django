from app.models import Club_2

def run():
    Club_2.objects.all().delete()

if __name__ == "__main__":
    run()
