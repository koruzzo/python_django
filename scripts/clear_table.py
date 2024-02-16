from api.models import (
    # D_Date,
    # D_Federation,
    D_Localisation,
    # D_Sex,
    # D_Type,
    # D_AgeGrp,
    # F_Club,
    # F_Licence
)
def run():
    models_to_clear = [
        # F_Club,
        # F_Licence,
        # D_Date,
        # D_Federation,
        D_Localisation,
        # D_Sex,
        # D_Type,
        # D_AgeGrp
    ]

    for model in models_to_clear:
        model.objects.all().delete()

if __name__ == "__main__":
    run()
