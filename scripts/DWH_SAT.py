from api.models import D_Sex, D_AgeGrp, D_Type

def run():
    """Importe les données préconstruites pour les dimensions."""

    D_Sex.objects.bulk_create([
        D_Sex(sex_code='H'),
        D_Sex(sex_code='F'),
    ])

    D_AgeGrp.objects.bulk_create([
        D_AgeGrp(age_label='1_4_ans'),
        D_AgeGrp(age_label='5_9_ans'),
        D_AgeGrp(age_label='10_14_ans'),
        D_AgeGrp(age_label='15_19_ans'),
        D_AgeGrp(age_label='20_24_ans'),
        D_AgeGrp(age_label='25_29_ans'),
        D_AgeGrp(age_label='30_34_ans'),
        D_AgeGrp(age_label='35_39_ans'),
        D_AgeGrp(age_label='40_44_ans'),
        D_AgeGrp(age_label='45_49_ans'),
        D_AgeGrp(age_label='50_54_ans'),
        D_AgeGrp(age_label='55_59_ans'),
        D_AgeGrp(age_label='60_64_ans'),
        D_AgeGrp(age_label='65_69_ans'),
        D_AgeGrp(age_label='70_74_ans'),
        D_AgeGrp(age_label='75_79_ans'),
        D_AgeGrp(age_label='80_99_ans'),
        D_AgeGrp(age_label='nr'),
    ])
    D_Type.objects.bulk_create([
        D_Type(type_label='clubs'),
        D_Type(type_label='epa'),
    ])