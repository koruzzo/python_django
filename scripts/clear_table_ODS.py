from api.models import  D_Date

def run():
    D_Date.objects.all().delete()

if __name__ == "__main__":
    run()
