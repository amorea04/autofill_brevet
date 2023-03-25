"""
Fichier répertoriant les fonctions utilisés dans l'app
"""
# %% Imports
import os
import sys
import re
from pypdf import PdfMerger
import img2pdf
from PIL import Image, ImageFont, ImageDraw

# %% Constants
if getattr(sys, 'frozen', False):
    ROOT_DIR = os.path.join(sys._MEIPASS, 'docs/')
else:
    ROOT_DIR = "docs/"
ROOT_DOWNLOADS_DIR = os.path.expanduser("~/Downloads/")
#print(ROOT_DIR, ROOT_DOWNLOADS_DIR)

FNT_FILE = "0_arial.ttf"

FILE_NAME_ATTEST_PROVISOIRE = "0_Attestation_provisoire_ULM_133_FormExa.jpg"
FILE_NAME_DEBUT_FORMATION = "0_134iFormlic.jpg"
FILE_NAME_EPREUVE_SOL = "0_34formexa.jpg"
FILE_NAME_EPREUVE_VOL = "0_35formexa.jpg"


# %% Functions


# %%% Suppression des anciens fichiers
def delete_old_files() -> None:
    filenames_in_docs = os.listdir(ROOT_DIR)
    for filename in filenames_in_docs:
        if not re.match(r"^0_|^\.", filename):
            os.remove(os.path.join(ROOT_DIR, filename))


# %%% sauvegarde de l'image temporaire
def save_temp_image(image_to_save: Image, filename_temp_jpg: str) -> None:
    image_to_save.save(filename_temp_jpg)


# %%% sauvegarde du pdf final
def save_final_pdf(filename_temp_jpg: str, final_filename_pdf: str) -> None:
    image = Image.open(filename_temp_jpg)
    pdf_bytes = img2pdf.convert(image.filename)  # converting into chunks using img2pdf
    file = open(final_filename_pdf, "wb")  # opening or creating pdf file
    file.write(pdf_bytes)  # writing pdf files with chunks
    image.close()
    file.close()  # closing pdf file
    os.remove(filename_temp_jpg)


# %%% Creation des utilitaires pour créer et annoter les fichiers
def create_utils(dict_create_utils: dict) -> tuple[dict]:
    attest_provisoire_jpg_save_temp1 = (
        f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_ATTEST_PROVISOIRE[2:-4]}_temp01.jpg"
    )
    attest_provisoire_pdf_save_final = f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_ATTEST_PROVISOIRE[2:-4]}_filled_{dict_create_utils['nom_candidat']}.pdf"

    debut_formation_jpg_save_temp1 = (
        f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_DEBUT_FORMATION[2:-4]}_temp01.jpg"
    )
    debut_formation_pdf_save_final = f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_DEBUT_FORMATION[2:-4]}_filled_{dict_create_utils['nom_candidat']}.pdf"

    epreuve_sol_jpg_save_temp1 = (
        f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_EPREUVE_SOL[2:-4]}_temp01.jpg"
    )
    epreuve_sol_pdf_save_final = f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_EPREUVE_SOL[2:-4]}_filled_{dict_create_utils['nom_candidat']}.pdf"

    epreuve_vol_jpg_save_temp1 = (
        f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_EPREUVE_VOL[2:-4]}_temp01.jpg"
    )
    epreuve_vol_pdf_save_final = f"{ROOT_DOWNLOADS_DIR}{FILE_NAME_EPREUVE_VOL[2:-4]}_filled_{dict_create_utils['nom_candidat']}.pdf"

    dict_annot_attest_provisoire = {
        ((3242 + 10), (508 + ((710 - 508) / 2))): [
            f"{dict_create_utils['nom_candidat']} {dict_create_utils['prenom_candidat']}",
            (3242, 508, 4545, 710),
        ],  # Nom prénom candidat
        ((1810 + 10), (2040 + ((2240 - 2040) / 2))): [
            f"{dict_create_utils['nom_instructeur']} {dict_create_utils['prenom_instructeur']}",
            (1810, 2040, 4160, 2240),
        ],  # Nom prénom instruct
        ((2140 + 10), (2200 + ((2400 - 2200) / 2))): [
            f"{dict_create_utils['numero_qualification']}",
            (2140, 2200, 4160, 2400),
        ],  # n° qualif instructeur
        ((1570 + 10), (2440 + ((2640 - 2440) / 2))): [
            f"{dict_create_utils['nom_candidat']} {dict_create_utils['prenom_candidat']}",
            (1570, 2440, 4160, 2640),
        ],  # Nom prénom candidat
        ((2800 + 10), (3250 + ((3450 - 3250) / 2))): [
            f"{dict_create_utils['type_ulm']}",
            (2800, 3250, 4260, 3450),
        ],  # type ULM
        ((1210 + 10), (4230 + ((4430 - 4230) / 2))): [
            f"{dict_create_utils['date_deb_attest_provisoire']}",
            (1210, 4230, 2300, 4430),
        ],  # date effet
        ((3360 + 10), (4230 + ((4430 - 4230) / 2))): [
            f"{dict_create_utils['date_fin_attest_provisoire']}",
            (3360, 4230, 4300, 4430),
        ],  # date fin validite
    }

    dict_annot_debut_formation = {
        ((750 + 10), (3680 + ((3850 - 3680) / 2))): [
            f"{dict_create_utils['nom_candidat']}",
            (750, 3680, 2200, 3850),
        ],
        ((750 + 10), (3850 + ((3972 - 3850) / 2))): [
            f"{dict_create_utils['prenom_candidat']}",
            (750, 3850, 2200, 3972),
        ],
        ((2900 + 10), (3676 + ((3850 - 3676) / 2))): [
            f"{dict_create_utils['nom_usage_candidat']}",
            (2900, 3676, 4800, 3850),
        ],
        ((2900 + 10), (3850 + ((3972 - 3850) / 2))): [
            f"{dict_create_utils['date_naissance_candidat']}",
            (2900, 3850, 3560, 3972),
        ],
        ((4268 + 10), (3850 + ((3972 - 3850) / 2))): [
            f"{dict_create_utils['lieu_naissance_candidat']}",
            (4268, 3850, 4800, 3972),
        ],
        ((750 + 10), (3972 + ((4083 - 3972) / 2))): [
            f"{dict_create_utils['adresse_candidat']}",
            (750, 3972, 2200, 4083),
        ],
        ((2900 + 10), (3972 + ((4083 - 3972) / 2))): [
            f"{dict_create_utils['commune_candidat']}",
            (2900, 3972, 3560, 4083),
        ],
        ((4268 + 10), (3972 + ((4083 - 3972) / 2))): [
            f"{dict_create_utils['code_postal_candidat']}",
            (4268, 3972, 4800, 4083),
        ],
        ((750 + 10), (4083 + ((4208 - 4083) / 2))): [
            f"{dict_create_utils['numero_telephone_candidat']}",
            (750, 4083, 2200, 4208),
        ],
        ((2900 + 10), (4083 + ((4208 - 4083) / 2))): [
            f"{dict_create_utils['mail_candidat']}",
            (2900, 4083, 4800, 4208),
        ],
        ((750 + 10), (4208 + ((4386 - 4208) / 2))): [
            f"{dict_create_utils['num_licence_candidat']}",
            (750, 4208, 2200, 4386),
        ],
        ((2900 + 10), (4208 + ((4386 - 4208) / 2))): [
            f"{dict_create_utils['pays_residence_candidat']}",
            (2900, 4208, 4800, 4386),
        ],
        ((1246 + 10), (4800 + (4913 - 4800) / 2)): [
            f"{dict_create_utils['nom_instructeur']}",
            (1246, 4800, 2900, 4913),
        ],
        ((1246 + 10), (4913 + (5038 - 4913) / 2)): [
            f"{dict_create_utils['numero_licence']}",
            (1246, 4913, 2900, 5038),
        ],
        ((1246 + 10), (5038 + (5159 - 5038) / 2)): [
            f"{dict_create_utils['numero_qualification']}",
            (1246, 5038, 2900, 5159),
        ],
        ((1246 + 10), (5159 + (5271 - 5159) / 2)): [
            f"{dict_create_utils['aeorclub_assos']}",
            (1246, 5159, 4800, 5271),
        ],
        ((3787 + 10), (4800 + (4913 - 4800) / 2)): [
            f"{dict_create_utils['prenom_instructeur']}",
            (3787, 4800, 4800, 4913),
        ],
        ((3787 + 10), (4913 + (5038 - 4913) / 2)): [
            f"{dict_create_utils['date_val_licence']}",
            (3787, 4913, 4800, 5038),
        ],
        ((3787 + 10), (5038 + (5159 - 5038) / 2)): [
            f"{dict_create_utils['date_val_qualification']}",
            (3787, 5038, 4800, 5159),
        ],
        ((590 + 10), (5954 + (6256 - 5954) / 2)): [
            f"{dict_create_utils['lieu_redaction']}",
            (590, 5954, 1143, 6256),
        ],
        ((590 + 10), (6256 + (6610 - 6256) / 2)): [
            f"{dict_create_utils['fait_le']}",
            (590, 6256, 1143, 6610),
        ],
    }

    dict_annot_epreuve_sol = {
        ((1600 + 10), (1670 + ((1760 - 1670) / 2))): [
            f"{dict_create_utils['nom_instructeur']} {dict_create_utils['prenom_instructeur']}",
            (1600, 1670, 4160, 1760),
        ],  # Nom prénom candidat
        ((1340 + 10), (1800 + ((1890 - 1800) / 2))): [
            f"{dict_create_utils['numero_qualification'][3:7]}",
            (1340, 1800, 1600, 1890),
        ],  # N° instruct ULM 1
        ((1650 + 10), (1800 + ((1890 - 1800) / 2))): [
            f"{dict_create_utils['numero_qualification'][7:12]}",
            (1650, 1800, 2020, 1890),
        ],  # N° instruct ULM 2
        ((2060 + 10), (1800 + ((1890 - 1800) / 2))): [
            f"{dict_create_utils['numero_qualification'][12:]}",
            (2060, 1800, 2240, 1890),
        ],  # N° instruct ULM 3
        ((2640 + 10), (1800 + ((1890 - 1800) / 2))): [
            f"{dict_create_utils['classe_ulm']}",
            (2640, 1800, 4160, 1890),
        ],  # N° instruct ULM 3
        ((800 + 10), (1930 + ((2020 - 1930) / 2))): [
            f"{dict_create_utils['date_val_qualification'][0:2]}",
            (800, 1930, 990, 2020),
        ],  # date val n° instruct 1
        ((1020 + 10), (1930 + ((2020 - 1930) / 2))): [
            f"{dict_create_utils['date_val_qualification'][3:5]}",
            (1020, 1930, 1170, 2020),
        ],  # date val n° instruct 2
        ((1290 + 10), (1930 + ((2020 - 1930) / 2))): [
            f"{dict_create_utils['date_val_qualification'][8:]}",
            (1290, 1930, 1430, 2020),
        ],  # date val n° instruct 3
        ((2650 + 10), (1930 + ((2020 - 1930) / 2))): [
            f"{dict_create_utils['numero_licence'][0:3]}",
            (2650, 1930, 2820, 2020),
        ],  # N° licence intructeur 1
        ((2850 + 10), (1930 + ((2020 - 1930) / 2))): [
            f"{dict_create_utils['numero_licence'][3:8]}",
            (2850, 1930, 3260, 2020),
        ],  # N° licence intructeur 2
        ((3290 + 10), (1930 + ((2020 - 1930) / 2))): [
            f"{dict_create_utils['numero_licence'][8:]}",
            (3290, 1930, 3950, 2020),
        ],  # N° licence intructeur 3
        ((1220 + 10), (2065 + ((2155 - 2065) / 2))): [
            f"{dict_create_utils['aeorclub_assos']}",
            (1220, 2065, 4160, 2155),
        ],  # Aeroclub
        ((930 + 10), (2200 + ((2290 - 2200) / 2))): [
            f"{dict_create_utils['telephone_instructeur']}",
            (930, 2200, 2240, 2290),
        ],  # telephone instructeur
        ((840 + 10), (2340 + ((2430 - 2340) / 2))): [
            f"{dict_create_utils['mail_instructeur']}",
            (840, 2340, 2240, 2430),
        ],  # courriel instructeur
        ((1360 + 10), (2660 + ((2750 - 2660) / 2))): [
            f"{dict_create_utils['nom_candidat']} {dict_create_utils['prenom_candidat']}",
            (1360, 2660, 4100, 2750),
        ],  # Nom prénom candidat
        ((790 + 10), (2795 + ((2885 - 2795) / 2))): [
            f"{dict_create_utils['date_naissance_candidat'][0:2]}",
            (790, 2795, 920, 2885),
        ],  # date naissance candidat 1
        ((960 + 10), (2795 + ((2885 - 2795) / 2))): [
            f"{dict_create_utils['date_naissance_candidat'][3:5]}",
            (960, 2795, 1070, 2885),
        ],  # date naissance candidat 2
        ((1100 + 10), (2795 + ((2885 - 2795) / 2))): [
            f"{dict_create_utils['date_naissance_candidat'][6:]}",
            (1100, 2795, 1290, 2885),
        ],  # date naissance candidat 3
        ((1370 + 10), (2795 + ((2885 - 2795) / 2))): [
            f"{dict_create_utils['lieu_naissance_candidat']}",
            (1370, 2795, 2950, 2885),
        ],  # lieu naissance candidat
        ((870 + 10), (2930 + ((3020 - 2930) / 2))): [
            f"{dict_create_utils['adresse_candidat']}, {dict_create_utils['code_postal_candidat']} {dict_create_utils['commune_candidat']}",
            (870, 2930, 4270, 3020),
        ],  # Adresse candidat
        ((930 + 10), (3065 + ((3155 - 3065) / 2))): [
            f"{dict_create_utils['numero_telephone_candidat']}",
            (930, 3065, 2240, 3155),
        ],  # telephone candidat
        ((840 + 10), (3200 + ((3290 - 3200) / 2))): [
            f"{dict_create_utils['mail_candidat']}",
            (840, 3200, 2240, 3290),
        ],  # courriel candidat
        ((2120 + 10), (3350 + ((3425 - 3350) / 2))): [
            f"{dict_create_utils['num_licence_candidat'][0:3]}",
            (2120, 3350, 2260, 3425),
        ],  # N° lic candidat 1
        ((2290 + 10), (3350 + ((3425 - 3350) / 2))): [
            f"{dict_create_utils['num_licence_candidat'][3:8]}",
            (2290, 3350, 2690, 3425),
        ],  # N° lic candidat 2
        ((2730 + 10), (3350 + ((3425 - 3350) / 2))): [
            f"{dict_create_utils['num_licence_candidat'][8:]}",
            (2730, 3350, 3400, 3425),
        ],  # N° lic candidat 3
        ((2000 + 10), (3610 + ((3700 - 3610) / 2))): [
            f"{dict_create_utils['date_ep_sol'][0:2]}",
            (2000, 3610, 2170, 3700),
        ],  # date ep sol 1
        ((2210 + 10), (3610 + ((3700 - 3610) / 2))): [
            f"{dict_create_utils['date_ep_sol'][3:5]}",
            (2210, 3610, 2370, 3700),
        ],  # date ep sol 2
        ((2495 + 10), (3610 + ((3700 - 3610) / 2))): [
            f"{dict_create_utils['date_ep_sol'][8:]}",
            (2495, 3610, 2610, 3700),
        ],  # date ep sol 3
        ((1760 + 10), (5785 + ((5875 - 5785) / 2))): [
            f"{dict_create_utils['num_ident_ulm']}",
            (1760, 5785, 3150, 5875),
        ],  # ident ULM
        ((740 + 10), (5965 + ((6055 - 5965) / 2))): [
            f"{dict_create_utils['lieu_redaction']}",
            (740, 5965, 1680, 6055),
        ],  # Fait a
        ((1760 + 10), (5965 + ((6055 - 5965) / 2))): [
            f"{dict_create_utils['fait_le'][0:2]}",
            (1760, 5965, 1910, 6055),
        ],  # fait le 1
        ((1940 + 10), (5965 + ((6055 - 5965) / 2))): [
            f"{dict_create_utils['fait_le'][3:5]}",
            (1940, 5965, 2050, 6055),
        ],  # fait le 2
        ((2170 + 10), (5965 + ((6055 - 5965) / 2))): [
            f"{dict_create_utils['fait_le'][8:]}",
            (2170, 5965, 2285, 6055),
        ],  # fait le 3
    }

    dict_annot_epreuve_vol = {
        ((1600 + 10), (1750 + ((1840 - 1750) / 2))): [
            f"{dict_create_utils['nom_instructeur']} {dict_create_utils['prenom_instructeur']}",
            (1600, 1750, 4160, 1840),
        ],  # Nom prénom candidat
        ((1340 + 10), (1900 + ((1990 - 1900) / 2))): [
            f"{dict_create_utils['numero_qualification'][3:7]}",
            (1340, 1900, 1600, 1990),
        ],  # N° instruct ULM 1
        ((1650 + 10), (1900 + ((1990 - 1900) / 2))): [
            f"{dict_create_utils['numero_qualification'][7:12]}",
            (1650, 1900, 2020, 1990),
        ],  # N° instruct ULM 2
        ((2060 + 10), (1900 + ((1990 - 1900) / 2))): [
            f"{dict_create_utils['numero_qualification'][12:]}",
            (2060, 1900, 2240, 1990),
        ],  # N° instruct ULM 3
        ((2640 + 10), (1900 + ((1990 - 1900) / 2))): [
            f"{dict_create_utils['classe_ulm']}",
            (2640, 1900, 4160, 1990),
        ],  # N° instruct ULM 3
        ((800 + 10), (2030 + ((2120 - 2030) / 2))): [
            f"{dict_create_utils['date_val_qualification'][0:2]}",
            (800, 2030, 990, 2120),
        ],  # date val n° instruct 1
        ((1020 + 10), (2030 + ((2120 - 2030) / 2))): [
            f"{dict_create_utils['date_val_qualification'][3:5]}",
            (1020, 2030, 1170, 2120),
        ],  # date val n° instruct 2
        ((1290 + 10), (2030 + ((2120 - 2030) / 2))): [
            f"{dict_create_utils['date_val_qualification'][8:]}",
            (1290, 2030, 1430, 2120),
        ],  # date val n° instruct 3
        ((2650 + 10), (2030 + ((2120 - 2030) / 2))): [
            f"{dict_create_utils['numero_licence'][0:3]}",
            (2650, 2030, 2820, 2120),
        ],  # N° licence intructeur 1
        ((2850 + 10), (2030 + ((2120 - 2030) / 2))): [
            f"{dict_create_utils['numero_licence'][3:8]}",
            (2850, 2030, 3260, 2120),
        ],  # N° licence intructeur 2
        ((3290 + 10), (2030 + ((2120 - 2030) / 2))): [
            f"{dict_create_utils['numero_licence'][8:]}",
            (3290, 2030, 3950, 2120),
        ],  # N° licence intructeur 3
        ((1220 + 10), (2165 + ((2255 - 2165) / 2))): [
            f"{dict_create_utils['aeorclub_assos']}",
            (1220, 2165, 4160, 2255),
        ],  # Aeroclub
        ((930 + 10), (2300 + ((2390 - 2300) / 2))): [
            f"{dict_create_utils['telephone_instructeur']}",
            (930, 2300, 2240, 2390),
        ],  # telephone instructeur
        ((840 + 10), (2440 + ((2530 - 2440) / 2))): [
            f"{dict_create_utils['mail_instructeur']}",
            (840, 2440, 2240, 2530),
        ],  # courriel instructeur
        ((1360 + 10), (2760 + ((2850 - 2760) / 2))): [
            f"{dict_create_utils['nom_candidat']} {dict_create_utils['prenom_candidat']}",
            (1360, 2760, 4100, 2850),
        ],  # Nom prénom candidat
        ((790 + 10), (2895 + ((2985 - 2895) / 2))): [
            f"{dict_create_utils['date_naissance_candidat'][0:2]}",
            (790, 2895, 920, 2985),
        ],  # date naissance candidat 1
        ((960 + 10), (2895 + ((2985 - 2895) / 2))): [
            f"{dict_create_utils['date_naissance_candidat'][3:5]}",
            (960, 2895, 1070, 2985),
        ],  # date naissance candidat 2
        ((1100 + 10), (2895 + ((2985 - 2895) / 2))): [
            f"{dict_create_utils['date_naissance_candidat'][6:]}",
            (1100, 2895, 1290, 2985),
        ],  # date naissance candidat 3
        ((1370 + 10), (2895 + ((2985 - 2895) / 2))): [
            f"{dict_create_utils['lieu_naissance_candidat']}",
            (1370, 2895, 2950, 2985),
        ],  # lieu naissance candidat
        ((870 + 10), (3030 + ((3120 - 3030) / 2))): [
            f"{dict_create_utils['adresse_candidat']}, {dict_create_utils['code_postal_candidat']} {dict_create_utils['commune_candidat']}",
            (870, 3030, 4270, 3120),
        ],  # Adresse candidat
        ((930 + 10), (3175 + ((3255 - 3175) / 2))): [
            f"{dict_create_utils['numero_telephone_candidat']}",
            (930, 3175, 2240, 3255),
        ],  # telephone candidat
        ((840 + 10), (3295 + ((3385 - 3295) / 2))): [
            f"{dict_create_utils['mail_candidat']}",
            (840, 3295, 2240, 3385),
        ],  # courriel candidat
        ((2120 + 10), (3430 + ((3520 - 3430) / 2))): [
            f"{dict_create_utils['num_licence_candidat'][0:3]}",
            (2120, 3430, 2260, 3520),
        ],  # N° lic candidat 1
        ((2290 + 10), (3430 + ((3520 - 3430) / 2))): [
            f"{dict_create_utils['num_licence_candidat'][3:8]}",
            (2290, 3430, 2690, 3520),
        ],  # N° lic candidat 2
        ((2730 + 10), (3430 + ((3520 - 3430) / 2))): [
            f"{dict_create_utils['num_licence_candidat'][8:]}",
            (2730, 3430, 3400, 3520),
        ],  # N° lic candidat 3
        ((1620 + 10), (3710 + ((3800 - 3710) / 2))): [
            f"{dict_create_utils['date_ep_vol'][0:2]}",
            (1620, 3710, 1790, 3800),
        ],  # date ep vol 1
        ((1820 + 10), (3710 + ((3800 - 3710) / 2))): [
            f"{dict_create_utils['date_ep_vol'][3:5]}",
            (1820, 3710, 1970, 3800),
        ],  # date ep vol 2
        ((2105 + 10), (3710 + ((3800 - 3710) / 2))): [
            f"{dict_create_utils['date_ep_vol'][8:]}",
            (2105, 3710, 2220, 3800),
        ],  # date ep vol 3
        ((1760 + 10), (5580 + ((5670 - 5580) / 2))): [
            f"{dict_create_utils['num_ident_ulm']}",
            (1760, 5580, 3150, 5670),
        ],  # ident ULM
        ((740 + 10), (5750 + ((5840 - 5750) / 2))): [
            f"{dict_create_utils['lieu_redaction']}",
            (740, 5750, 1680, 5840),
        ],  # Fait a
        ((1760 + 10), (5750 + ((5840 - 5750) / 2))): [
            f"{dict_create_utils['fait_le'][0:2]}",
            (1760, 5750, 1910, 5840),
        ],  # fait le 1
        ((1940 + 10), (5750 + ((5840 - 5750) / 2))): [
            f"{dict_create_utils['fait_le'][3:5]}",
            (1940, 5750, 2050, 5840),
        ],  # fait le 2
        ((2170 + 10), (5750 + ((5840 - 5750) / 2))): [
            f"{dict_create_utils['fait_le'][8:]}",
            (2170, 5750, 2285, 5840),
        ],  # fait le 3
    }

    utils_attest_provisoire = {
        "filename_original": FILE_NAME_ATTEST_PROVISOIRE,
        "filename_jpg_temp": attest_provisoire_jpg_save_temp1,
        "filename_final": attest_provisoire_pdf_save_final,
        "dict_annotate": dict_annot_attest_provisoire,
    }

    utils_debut_formation = {
        "filename_original": FILE_NAME_DEBUT_FORMATION,
        "filename_jpg_temp": debut_formation_jpg_save_temp1,
        "filename_final": debut_formation_pdf_save_final,
        "dict_annotate": dict_annot_debut_formation,
    }

    utils_epreuve_sol = {
        "filename_original": FILE_NAME_EPREUVE_SOL,
        "filename_jpg_temp": epreuve_sol_jpg_save_temp1,
        "filename_final": epreuve_sol_pdf_save_final,
        "dict_annotate": dict_annot_epreuve_sol,
    }

    utils_epreuve_vol = {
        "filename_original": FILE_NAME_EPREUVE_VOL,
        "filename_jpg_temp": epreuve_vol_jpg_save_temp1,
        "filename_final": epreuve_vol_pdf_save_final,
        "dict_annotate": dict_annot_epreuve_vol,
    }

    return (
        utils_attest_provisoire,
        utils_debut_formation,
        utils_epreuve_sol,
        utils_epreuve_vol,
    )


# %%% Annotation de l'attestation provisoire
def add_annotations_general(utils_annotate: dict) -> Image:
    img = Image.open(f"{ROOT_DIR}{utils_annotate['filename_original']}")
    image_editable = ImageDraw.Draw(img)

    dict_annotate = utils_annotate["dict_annotate"]

    for bbox, text in dict_annotate.items():
        fontsize = 100
        fnt = ImageFont.truetype(f"{ROOT_DIR}{FNT_FILE}", fontsize)
        maxbox_dim = text[1]
        textbox_dims = image_editable.textbbox(
            bbox, text[0], font=fnt, anchor="lm"
        )  # (left, top, right, bottom)
        box_width = maxbox_dim[2] - maxbox_dim[0]
        text_width = (textbox_dims[2] - textbox_dims[0]) + 20
        box_height = maxbox_dim[3] - maxbox_dim[1]
        text_height = (textbox_dims[3] - textbox_dims[1]) + 10
        while (text_width > box_width) or (text_height > box_height):
            # Réduire la taille de police
            fontsize -= 5
            fnt = ImageFont.truetype(f"{ROOT_DIR}{FNT_FILE}", fontsize)
            textbox_dims = image_editable.textbbox(bbox, text[0], font=fnt, anchor="lm")
            box_width = maxbox_dim[2] - maxbox_dim[0]
            text_width = textbox_dims[2] - textbox_dims[0]
            box_height = maxbox_dim[3] - maxbox_dim[1]
            text_height = textbox_dims[3] - textbox_dims[1]

        image_editable.text(bbox, text[0], (0, 0, 0), font=fnt, anchor="lm")

    return img


# %%% Ajout des boxes sur le formualaire épreuve sol
def add_annotations_boxes_ep_vol(
    dict_create_boxes: dict, image_to_annot: Image
) -> Image:
    img = image_to_annot
    image_editable = ImageDraw.Draw(img)

    image_editable.rectangle(
        (2305, 2450, 2385, 2540), outline="white", fill="white"
    )  # @courriel_instructeur
    image_editable.rectangle(
        (2305, 3310, 2385, 3400), outline="white", fill="white"
    )  # @courriel_candidat

    if dict_create_boxes["options_apte_checklist"] == "Apte":
        image_editable.rectangle(
            (2850, 3860, 2920, 3940), outline="black", fill="black"
        )  # fill_APTE
    elif dict_create_boxes["options_apte_checklist"] == "Ajourne":
        image_editable.rectangle(
            (1708, 3860, 1778, 3940), outline="black", fill="black"
        )  # fill_ajourne

    if dict_create_boxes["brevet_init_or_not"] == "Premier brevet":
        image_editable.rectangle(
            (410, 4050, 500, 4130), outline="black", fill="black"
        )  # fill_premier_brevet
        if dict_create_boxes["type_ulm"] == "Paramoteur":
            image_editable.rectangle(
                (1495, 4500, 1565, 4580), outline="black", fill="black"
            )  # fill_paramoteur_brevet
        elif dict_create_boxes["type_ulm"] == "Multiaxe":
            image_editable.rectangle(
                (450, 4500, 520, 4580), outline="black", fill="black"
            )  # fill_multiaxe_brevet
    elif dict_create_boxes["brevet_init_or_not"] == "Ajout classe":
        image_editable.rectangle(
            (410, 4150, 500, 4230), outline="black", fill="black"
        )  # fill_ajout_classe
        if (
            len(dict_create_boxes["emport_pass_or_not"]) > 0
            and dict_create_boxes["emport_pass_or_not"][0] == "Emport de passager"
        ):
            image_editable.rectangle(
                (650, 4700, 735, 4800), outline="black", fill="black"
            )  # fill_option_emport
            if dict_create_boxes["type_ulm"] == "Paramoteur":
                image_editable.rectangle(
                    (1495, 5010, 1565, 5090), outline="black", fill="black"
                )  # fill_paramoteur_emport
            elif dict_create_boxes["type_ulm"] == "Multiaxe":
                image_editable.rectangle(
                    (450, 5010, 520, 5090), outline="black", fill="black"
                )  # fill_multiaxe_emport
        else:
            image_editable.rectangle(
                (650, 4240, 735, 4340), outline="black", fill="black"
            )  # fill_option_ajout_classe
            if dict_create_boxes["type_ulm"] == "Paramoteur":
                image_editable.rectangle(
                    (1495, 4500, 1565, 4580), outline="black", fill="black"
                )  # fill_paramoteur_brevet
            elif dict_create_boxes["type_ulm"] == "Multiaxe":
                image_editable.rectangle(
                    (450, 4500, 520, 4580), outline="black", fill="black"
                )  # fill_multiaxe_brevet

    return img


# %%% Ajout des boxes sur le formualaire épreuve vol
def add_annotations_boxes_ep_sol(
    dict_create_boxes: dict, image_to_annot: Image
) -> Image:
    img = image_to_annot
    image_editable = ImageDraw.Draw(img)

    image_editable.rectangle(
        (2305, 2350, 2385, 2460), outline="white", fill="white"
    )  # @courriel_instructeur
    image_editable.rectangle(
        (2305, 3220, 2385, 3310), outline="white", fill="white"
    )  # @courriel_candidat

    if dict_create_boxes["options_apte_checklist"] == "Apte":
        image_editable.rectangle(
            (2850, 3850, 2920, 3930), outline="black", fill="black"
        )  # fill_APTE
    elif dict_create_boxes["options_apte_checklist"] == "Ajourne":
        image_editable.rectangle(
            (1708, 3850, 1778, 3930), outline="black", fill="black"
        )  # fill_ajourne

    if dict_create_boxes["brevet_init_or_not"] == "Premier brevet":
        image_editable.rectangle(
            (410, 4030, 500, 4130), outline="black", fill="black"
        )  # fill_premier_brevet
        if dict_create_boxes["type_ulm"] == "Paramoteur":
            image_editable.rectangle(
                (1495, 4490, 1565, 4575), outline="black", fill="black"
            )  # fill_paramoteur_brevet
        elif dict_create_boxes["type_ulm"] == "Multiaxe":
            image_editable.rectangle(
                (450, 4490, 520, 4575), outline="black", fill="black"
            )  # fill_multiaxe_brevet
    elif dict_create_boxes["brevet_init_or_not"] == "Ajout classe":
        image_editable.rectangle(
            (410, 4130, 500, 4230), outline="black", fill="black"
        )  # fill_ajout_classe
        if (
            len(dict_create_boxes["emport_pass_or_not"]) > 0
            and dict_create_boxes["emport_pass_or_not"][0] == "Emport de passager"
        ):
            image_editable.rectangle(
                (650, 4690, 735, 4795), outline="black", fill="black"
            )  # fill_option_emport
            if dict_create_boxes["type_ulm"] == "Paramoteur":
                image_editable.rectangle(
                    (1495, 5050, 1565, 5130), outline="black", fill="black"
                )  # fill_paramoteur_emport
            elif dict_create_boxes["type_ulm"] == "Multiaxe":
                image_editable.rectangle(
                    (450, 5050, 520, 5130), outline="black", fill="black"
                )  # fill_multiaxe_emport
        else:
            image_editable.rectangle(
                (650, 4230, 735, 4330), outline="black", fill="black"
            )  # fill_option_ajout_classe
            if dict_create_boxes["type_ulm"] == "Paramoteur":
                image_editable.rectangle(
                    (1495, 4490, 1565, 4575), outline="black", fill="black"
                )  # fill_paramoteur_brevet
            elif dict_create_boxes["type_ulm"] == "Multiaxe":
                image_editable.rectangle(
                    (450, 4490, 520, 4575), outline="black", fill="black"
                )  # fill_multiaxe_brevet

    return img


# %%% Annoter les pdfs unitaires
def annotate_single_pdf(utils_to_annotate_pdf: dict, original_values: dict) -> None:
    # Ajout des annotations sur le pdf original
    doc_provisoire = add_annotations_general(utils_annotate=utils_to_annotate_pdf)

    if utils_to_annotate_pdf["filename_original"] == FILE_NAME_EPREUVE_SOL:
        doc_provisoire = add_annotations_boxes_ep_sol(
            dict_create_boxes=original_values, image_to_annot=doc_provisoire
        )
    elif utils_to_annotate_pdf["filename_original"] == FILE_NAME_EPREUVE_VOL:
        doc_provisoire = add_annotations_boxes_ep_vol(
            dict_create_boxes=original_values, image_to_annot=doc_provisoire
        )

    # Sauvegarde du jpg temporaire
    save_temp_image(
        image_to_save=doc_provisoire,
        filename_temp_jpg=utils_to_annotate_pdf["filename_jpg_temp"],
    )

    # Sauvegarde finale du pdf annoté
    save_final_pdf(
        filename_temp_jpg=utils_to_annotate_pdf["filename_jpg_temp"],
        final_filename_pdf=utils_to_annotate_pdf["filename_final"],
    )


# %%% Merge final de tous es pdfs
def merge_pdfs(list_filename: list, original_values: dict) -> None:
    final_filename_dossier_complet = f"{ROOT_DOWNLOADS_DIR}dossier_complet_{original_values['nom_candidat']}_{original_values['prenom_candidat']}.pdf"
    merger = PdfMerger()

    for pdf in list_filename:
        merger.append(pdf)

    merger.write(final_filename_dossier_complet)
    merger.close()
    for name in list_filename:
        os.remove(name)
    return final_filename_dossier_complet


# %%%
def annotate_all_pdfs(dict_text: dict) -> None:
    """
    Fonction dont l'objectif est de créer tous les fichiers nécessaires.
    """
    (
        utils_attest_provisoire,
        utils_debut_formation,
        utils_epreuve_sol,
        utils_epreuve_vol,
    ) = create_utils(dict_create_utils=dict_text)

    final_filled_filenames = [
        utils_debut_formation["filename_final"],
        utils_epreuve_sol["filename_final"],
        utils_epreuve_vol["filename_final"],
        utils_attest_provisoire["filename_final"],
    ]

    if "debut_formation" not in dict_text["docs_to_fill"]:
        final_filled_filenames.remove(utils_debut_formation["filename_final"])
    if "ep_sol" not in dict_text["docs_to_fill"]:
        final_filled_filenames.remove(utils_epreuve_sol["filename_final"])
    if "ep_vol" not in dict_text["docs_to_fill"]:
        final_filled_filenames.remove(utils_epreuve_vol["filename_final"])
    if "attest_provisoire" not in dict_text["docs_to_fill"]:
        final_filled_filenames.remove(utils_attest_provisoire["filename_final"])

    #delete_old_files()

    if "debut_formation" in dict_text["docs_to_fill"]:
        annotate_single_pdf(
            utils_to_annotate_pdf=utils_debut_formation,
            original_values=dict_text,
        )

    if "ep_sol" in dict_text["docs_to_fill"]:
        annotate_single_pdf(
            utils_to_annotate_pdf=utils_epreuve_sol,
            original_values=dict_text,
        )

    if "ep_vol" in dict_text["docs_to_fill"]:
        annotate_single_pdf(
            utils_to_annotate_pdf=utils_epreuve_vol,
            original_values=dict_text,
        )

    if "attest_provisoire" in dict_text["docs_to_fill"]:
        annotate_single_pdf(
            utils_to_annotate_pdf=utils_attest_provisoire,
            original_values=dict_text,
        )

    if len(final_filled_filenames) > 0:
        filename_to_download = merge_pdfs(
            list_filename=final_filled_filenames, original_values=dict_text
        )

    return filename_to_download
