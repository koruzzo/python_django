from api.models import  D_Date #A modifier selon le besoin

def run():
    D_Date.objects.all().delete()#A modifier selon le besoin

if __name__ == "__main__":
    run()
