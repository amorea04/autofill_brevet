"""
Module aimed to build the GUI
for autofill brevet project
"""

# %% Imports
import os
import datetime
import tkinter
import customtkinter
from PIL import Image
import pandas as pd


import autofill_functions_tk


# %% GUI
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
customtkinter.set_appearance_mode("Dark")

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
customtkinter.set_default_color_theme("dark-blue")


# Create App class
class App(customtkinter.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Création des documents")
        self.geometry(f"{1300}x{850}")
        customtkinter.set_widget_scaling(1.2)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0), weight=1)

        # %%% Création du logo
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "logo0.jpg")),
            size=(26, 26),
        )

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((5, 7), weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            image=self.logo_image,
            compound="left",
            text="Paramètres",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=(10, 10), pady=(20, 10))

        # %%% Création d'une premiere frame pour radiobutton --> Apte
        self.radiobutton_frame_sbar_apte = customtkinter.CTkFrame(self.sidebar_frame)
        self.radiobutton_frame_sbar_apte.grid(
            row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )

        self.radio_var_apte = tkinter.IntVar(value=0)
        self.label_radio_group_apte = customtkinter.CTkLabel(
            master=self.radiobutton_frame_sbar_apte, text="Apte ?", anchor="nw"
        )
        self.label_radio_group_apte.grid(
            row=0, column=2, columnspan=1, padx=10, pady=(10, 0), sticky="nw"
        )
        self.radio_button_apte_1 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame_sbar_apte,
            variable=self.radio_var_apte,
            value=0,
            text="Apte",
        )
        self.radio_button_apte_1.grid(
            row=1, column=2, pady=(5, 5), padx=10, sticky="nw"
        )
        self.radio_button_apte_2 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame_sbar_apte,
            variable=self.radio_var_apte,
            value=1,
            text="Ajourné",
        )
        self.radio_button_apte_2.grid(row=2, column=2, pady=5, padx=10, sticky="w")

        # %%% Création d'une seconde frame pour radiobutton --> premier brevet ?
        self.radiobutton_frame_sbar_pb = customtkinter.CTkFrame(self.sidebar_frame)
        self.radiobutton_frame_sbar_pb.grid(
            row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.radio_var_pb = tkinter.IntVar(value=0)
        self.label_radio_group_pb = customtkinter.CTkLabel(
            master=self.radiobutton_frame_sbar_pb,
            text="Premier brevet ?",
            anchor="nw",
        )
        self.label_radio_group_pb.grid(
            row=0, column=2, columnspan=1, padx=10, pady=(10, 0), sticky="nw"
        )
        self.radio_button_1_pb = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame_sbar_pb,
            variable=self.radio_var_pb,
            value=0,
            text="Premier brevet",
        )
        self.radio_button_1_pb.grid(row=1, column=2, pady=(5, 5), padx=10, sticky="nw")
        self.radio_button_2_pb = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame_sbar_pb,
            variable=self.radio_var_pb,
            value=1,
            text="Ajout d'une classe",
        )
        self.radio_button_2_pb.grid(row=2, column=2, pady=5, padx=10, sticky="nw")

        # %%% Création d'une troisième frame pour radiobutton --> type ULM ?
        self.radiobutton_frame_sbar_type_ulm = customtkinter.CTkFrame(
            self.sidebar_frame
        )
        self.radiobutton_frame_sbar_type_ulm.grid(
            row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.radio_var_type_ulm = tkinter.IntVar(value=0)
        self.label_radio_group_type_ulm = customtkinter.CTkLabel(
            master=self.radiobutton_frame_sbar_type_ulm,
            text="Type ULM ?",
            anchor="nw",
        )
        self.label_radio_group_type_ulm.grid(
            row=0, column=2, columnspan=1, padx=10, pady=(10, 0), sticky="nw"
        )
        self.radio_button_1_type_ulm = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame_sbar_type_ulm,
            variable=self.radio_var_type_ulm,
            value=0,
            text="Paramoteur",
        )
        self.radio_button_1_type_ulm.grid(
            row=1, column=2, pady=(5, 5), padx=10, sticky="nw"
        )
        self.radio_button_2_type_ulm = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame_sbar_type_ulm,
            variable=self.radio_var_type_ulm,
            value=1,
            text="Multiaxe",
        )
        self.radio_button_2_type_ulm.grid(row=2, column=2, pady=5, padx=10, sticky="nw")

        # %%% Création d'une quatrième frame pour checkbox --> emport passager?
        self.checkbox_frame_sbar_ep = customtkinter.CTkFrame(self.sidebar_frame)
        self.checkbox_frame_sbar_ep.grid(
            row=4, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )

        self.checkbox_1_ep = customtkinter.CTkCheckBox(
            master=self.checkbox_frame_sbar_ep,
            text="Emport passager",
            command=self.get_check_box_status,
        )
        self.checkbox_1_ep.grid(row=1, column=0, pady=(10, 10), padx=10, sticky="nw")

        # %%% Création d'une Sixième frame pour checkbox --> type documents à créer ?
        self.docs_to_fill = {"debut_formation", "ep_sol", "ep_vol", "attest_provisoire"}
        self.checkbox_frame_sbar_type_docs = customtkinter.CTkFrame(self.sidebar_frame)
        self.checkbox_frame_sbar_type_docs.grid(
            row=6, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )

        self.var_checkbox_deb_formation = tkinter.IntVar(value=1)
        self.checkbox_deb_formation = customtkinter.CTkCheckBox(
            master=self.checkbox_frame_sbar_type_docs,
            text="Début formation",
            variable=self.var_checkbox_deb_formation,
            command=self.get_docs_to_fill,
        )
        self.checkbox_deb_formation.grid(
            row=1, column=0, pady=(5, 2), padx=10, sticky="w"
        )

        self.var_checkbox_ep_sol = tkinter.IntVar(value=1)
        self.checkbox_ep_sol = customtkinter.CTkCheckBox(
            master=self.checkbox_frame_sbar_type_docs,
            text="Epreuve sol",
            variable=self.var_checkbox_ep_sol,
            command=self.get_docs_to_fill,
        )
        self.checkbox_ep_sol.grid(row=2, column=0, pady=(2, 2), padx=10, sticky="w")

        self.var_checkbox_ep_vol = tkinter.IntVar(value=1)
        self.checkbox_ep_vol = customtkinter.CTkCheckBox(
            master=self.checkbox_frame_sbar_type_docs,
            text="Epreuve vol",
            variable=self.var_checkbox_ep_vol,
            command=self.get_docs_to_fill,
        )
        self.checkbox_ep_vol.grid(row=3, column=0, pady=(2, 2), padx=10, sticky="w")

        self.var_checkbox_attest_provisoire = tkinter.IntVar(value=1)
        self.checkbox_attest_provisoire = customtkinter.CTkCheckBox(
            master=self.checkbox_frame_sbar_type_docs,
            text="Attest. provisoire",
            variable=self.var_checkbox_attest_provisoire,
            command=self.get_docs_to_fill,
        )
        self.checkbox_attest_provisoire.grid(
            row=4, column=0, pady=(2, 5), padx=10, sticky="w"
        )

        # %%% sélection des paramètres de la fenetre.
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Apparence:", anchor="w"
        )
        self.appearance_mode_label.grid(row=8, column=0, padx=10, pady=(2, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=10, pady=(0, 2))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Echelle:", anchor="w"
        )
        self.scaling_label.grid(row=10, column=0, padx=10, pady=(2, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=11, column=0, padx=10, pady=(0, 10))

        # %%% création du bouton sauvegarder le document
        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text="Remplir les documents",
            text_color=("gray10", "#DCE4EE"),
            command=self.try_annotate,
        )
        self.main_button_1.grid(
            row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # %%% Informations à remplir
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            master=self,
            label_text="Informations",
            label_font=(None, 22),
        )
        self.scrollable_frame.grid(
            row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure((0, 1, 2), weight=1)
        # %%%% Les dates
        self.frame_dates = customtkinter.CTkFrame(
            master=self.scrollable_frame, border_color="grey", border_width=3
        )
        self.frame_dates.grid(
            row=1, column=0, padx=(10, 10), pady=(0, 5), sticky="nsew"
        )
        self.frame_dates.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.label_frame_dates = customtkinter.CTkLabel(
            master=self.frame_dates,
            text="Les Dates (format: JJ/MM/AAAA) :",
            font=(None, 18),
            text_color="orange",
            anchor="w",
        )
        self.label_frame_dates.grid(
            row=0, column=0, columnspan=3, padx=10, pady=(5, 0), sticky="w"
        )
        self.label_date_deb_formation = customtkinter.CTkLabel(
            master=self.frame_dates,
            text="Date début formation:",
            anchor="sw",
        )
        self.label_date_deb_formation.grid(
            row=1, column=0, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_date_deb_formation = customtkinter.CTkEntry(
            self.frame_dates, placeholder_text=""
        )
        self.entry_date_deb_formation.grid(
            row=2, column=0, padx=(10, 0), pady=(0, 0), sticky="nsew"
        )
        self.label_date_deb_attest_provisoire = customtkinter.CTkLabel(
            master=self.frame_dates,
            text="Date début attestation:",
            anchor="sw",
        )
        self.label_date_deb_attest_provisoire.grid(
            row=3, column=0, padx=10, pady=(5, 0), sticky="w"
        )
        self.var_date_deb_attest_provisoire = tkinter.StringVar(
            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}"
        )
        self.entry_date_deb_attest_provisoire = customtkinter.CTkEntry(
            self.frame_dates,
            textvariable=self.var_date_deb_attest_provisoire,
        )
        self.entry_date_deb_attest_provisoire.grid(
            row=4, column=0, padx=(10, 0), pady=(0, 0), sticky="nsew"
        )
        self.label_date_ep_sol = customtkinter.CTkLabel(
            master=self.frame_dates,
            text="Date épreuve sol:",
            anchor="sw",
        )
        self.label_date_ep_sol.grid(row=1, column=2, padx=10, pady=(0, 0), sticky="w")
        self.var_date_ep_sol = tkinter.StringVar(
            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}"
        )
        self.entry_date_ep_sol = customtkinter.CTkEntry(
            self.frame_dates,
            textvariable=self.var_date_ep_sol,
        )
        self.entry_date_ep_sol.grid(
            row=2, column=2, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_date_ep_vol = customtkinter.CTkLabel(
            master=self.frame_dates,
            text="Date épreuve vol :",
            anchor="sw",
        )
        self.label_date_ep_vol.grid(row=3, column=2, padx=10, pady=(0, 0), sticky="w")
        self.var_date_ep_vol = tkinter.StringVar(
            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}"
        )
        self.entry_date_ep_vol = customtkinter.CTkEntry(
            self.frame_dates,
            textvariable=self.var_date_ep_vol,
        )
        self.entry_date_ep_vol.grid(
            row=4, column=2, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_fait_le = customtkinter.CTkLabel(
            master=self.frame_dates,
            text="Fait le :",
            anchor="sw",
        )
        self.label_fait_le.grid(row=5, column=0, padx=10, pady=(5, 0), sticky="w")
        self.var_fait_le = tkinter.StringVar(
            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}"
        )
        self.entry_fait_le = customtkinter.CTkEntry(
            self.frame_dates,
            textvariable=self.var_fait_le,
        )
        self.entry_fait_le.grid(
            row=6, column=0, padx=(10, 0), pady=(0, 10), sticky="nsew"
        )

        # %%%% Le candidat
        self.frame_candidat = customtkinter.CTkFrame(
            master=self.scrollable_frame, border_color="grey", border_width=3
        )
        self.frame_candidat.grid(
            row=2, column=0, padx=(10, 10), pady=(0, 5), sticky="nsew"
        )
        self.frame_candidat.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.label_frame_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Le candidat :",
            font=(None, 18),
            text_color="orange",
            anchor="w",
        )
        self.label_frame_candidat.grid(
            row=0, column=0, columnspan=3, padx=10, pady=(5, 0), sticky="w"
        )
        self.label_nom_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Nom :",
            anchor="sw",
        )
        self.label_nom_candidat.grid(row=1, column=0, padx=10, pady=(0, 0), sticky="w")
        self.entry_nom_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_nom_candidat.grid(
            row=2, column=0, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_prenom_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Prénom :",
            anchor="sw",
        )
        self.label_prenom_candidat.grid(
            row=1, column=1, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_prenom_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_prenom_candidat.grid(
            row=2, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_nom_usage_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Nom d'usage si différent:",
            anchor="sw",
        )
        self.label_nom_usage_candidat.grid(
            row=1, column=2, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_nom_usage_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_nom_usage_candidat.grid(
            row=2, column=2, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_date_naissance_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Date naissance :",
            anchor="sw",
        )
        self.label_date_naissance_candidat.grid(
            row=1, column=3, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_date_naissance_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_date_naissance_candidat.grid(
            row=2, column=3, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_lieu_naissance_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Lieu naissance :",
            anchor="sw",
        )
        self.label_lieu_naissance_candidat.grid(
            row=1, column=4, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_lieu_naissance_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_lieu_naissance_candidat.grid(
            row=2, column=4, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )

        self.label_adresse_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Adresse :",
            anchor="sw",
        )
        self.label_adresse_candidat.grid(
            row=3, column=0, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_adresse_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_adresse_candidat.grid(
            row=4, column=0, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_commune_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Commune :",
            anchor="sw",
        )
        self.label_commune_candidat.grid(
            row=3, column=1, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_commune_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_commune_candidat.grid(
            row=4, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_code_postal_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Code postal :",
            anchor="sw",
        )
        self.label_code_postal_candidat.grid(
            row=3, column=2, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_code_postal_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_code_postal_candidat.grid(
            row=4, column=2, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_pays_residence_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Pays résidence :",
            anchor="sw",
        )
        self.label_pays_residence_candidat.grid(
            row=3, column=3, padx=10, pady=(0, 0), sticky="w"
        )
        self.var_pays_residence_candidat = tkinter.StringVar(value="France")
        self.entry_pays_residence_candidat = customtkinter.CTkEntry(
            self.frame_candidat,
            textvariable=self.var_pays_residence_candidat,
        )
        self.entry_pays_residence_candidat.grid(
            row=4, column=3, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )

        self.label_numero_telephone_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="N° téléphone :",
            anchor="sw",
        )
        self.label_numero_telephone_candidat.grid(
            row=5, column=0, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_numero_telephone_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_numero_telephone_candidat.grid(
            row=6, column=0, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.label_mail_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="E-mail :",
            anchor="sw",
        )
        self.label_mail_candidat.grid(row=5, column=1, padx=10, pady=(0, 0), sticky="w")
        self.entry_mail_candidat = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_mail_candidat.grid(
            row=6, column=1, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.label_num_licence_candidat = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="N° Licence (si applicable) :",
            anchor="sw",
        )
        self.label_num_licence_candidat.grid(
            row=5, column=2, padx=10, pady=(0, 0), sticky="w"
        )
        self.var_num_licence_candidat = tkinter.StringVar(value="----------")
        self.entry_num_licence_candidat = customtkinter.CTkEntry(
            self.frame_candidat,
            textvariable=self.var_num_licence_candidat,
        )
        self.entry_num_licence_candidat.grid(
            row=6, column=2, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.label_num_ident_ulm = customtkinter.CTkLabel(
            master=self.frame_candidat,
            text="Identification ULM :",
            anchor="sw",
        )
        self.label_num_ident_ulm.grid(row=5, column=3, padx=10, pady=(0, 0), sticky="w")
        self.entry_num_ident_ulm = customtkinter.CTkEntry(
            self.frame_candidat, placeholder_text=""
        )
        self.entry_num_ident_ulm.grid(
            row=6, column=3, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )

        # %%%% L'instructeur'
        self.frame_instructeur = customtkinter.CTkFrame(
            master=self.scrollable_frame, border_color="grey", border_width=3
        )
        self.frame_instructeur.grid(
            row=3, column=0, padx=(10, 10), pady=(0, 5), sticky="nsew"
        )
        self.frame_instructeur.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.label_frame_instructeur = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="L'instructeur :",
            font=(None, 18),
            text_color="orange",
            anchor="w",
        )
        self.label_frame_instructeur.grid(
            row=0, column=0, columnspan=3, padx=10, pady=(5, 0), sticky="w"
        )

        self.var_nom_instructeur = tkinter.StringVar(value="CHIRON")
        self.var_prenom_instructeur = tkinter.StringVar(value="Christophe")
        self.var_telephone_instructeur = tkinter.StringVar(value="06.61.19.53.82")
        self.var_mail_instructeur = tkinter.StringVar(value="ckchiron@yahoo.fr")
        self.var_numero_licence = tkinter.StringVar(value="0305004006")
        self.var_numero_qualification = tkinter.StringVar(value="ULM 0300004006")
        self.var_date_val_qualification = tkinter.StringVar(value="31/07/2023")
        self.var_date_val_licence = tkinter.StringVar(value="-----------")
        self.var_aeorclub_assos = tkinter.StringVar(value="Air Race Pro")
        self.var_lieu_redaction = tkinter.StringVar(value="Voeuil-et-Giget")

        self.label_nom_instructeur = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="Nom :",
            anchor="sw",
        )
        self.label_nom_instructeur.grid(
            row=1, column=0, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_nom_instructeur = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_nom_instructeur,
        )
        self.entry_nom_instructeur.grid(
            row=2, column=0, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_prenom_instructeur = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="Prénom :",
            anchor="sw",
        )
        self.label_prenom_instructeur.grid(
            row=1, column=1, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_prenom_instructeur = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_prenom_instructeur,
        )
        self.entry_prenom_instructeur.grid(
            row=2, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_telephone_instructeur = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="N° téléphone :",
            anchor="sw",
        )
        self.label_telephone_instructeur.grid(
            row=1, column=2, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_telephone_instructeur = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_telephone_instructeur,
        )
        self.entry_telephone_instructeur.grid(
            row=2, column=2, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_mail_instructeur = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="e-mail :",
            anchor="sw",
        )
        self.label_mail_instructeur.grid(
            row=1, column=3, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_mail_instructeur = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_mail_instructeur,
        )
        self.entry_mail_instructeur.grid(
            row=2, column=3, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_numero_licence = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="N° licence :",
            anchor="sw",
        )
        self.label_numero_licence.grid(
            row=3, column=0, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_numero_licence = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_numero_licence,
        )
        self.entry_numero_licence.grid(
            row=4, column=0, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_numero_qualification = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="N° qualification :",
            anchor="sw",
        )
        self.label_numero_qualification.grid(
            row=3, column=1, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_numero_qualification = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_numero_qualification,
        )
        self.entry_numero_qualification.grid(
            row=4, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_date_val_qualification = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="Date val qualif :",
            anchor="sw",
        )
        self.label_date_val_qualification.grid(
            row=3, column=2, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_date_val_qualification = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_date_val_qualification,
        )
        self.entry_date_val_qualification.grid(
            row=4, column=2, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_date_val_licence = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="Date val licence :",
            anchor="sw",
        )
        self.label_date_val_licence.grid(
            row=3, column=3, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_date_val_licence = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_date_val_licence,
        )
        self.entry_date_val_licence.grid(
            row=4, column=3, padx=(10, 10), pady=(0, 0), sticky="nsew"
        )
        self.label_aeorclub_assos = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="Aéroclub/Association :",
            anchor="sw",
        )
        self.label_aeorclub_assos.grid(
            row=5, column=0, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_aeorclub_assos = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_aeorclub_assos,
        )
        self.entry_aeorclub_assos.grid(
            row=6, column=0, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.label_lieu_redaction = customtkinter.CTkLabel(
            master=self.frame_instructeur,
            text="Aéroclub/Association :",
            anchor="sw",
        )
        self.label_lieu_redaction.grid(
            row=5, column=1, padx=10, pady=(0, 0), sticky="w"
        )
        self.entry_lieu_redaction = customtkinter.CTkEntry(
            self.frame_instructeur,
            textvariable=self.var_lieu_redaction,
        )
        self.entry_lieu_redaction.grid(
            row=6, column=1, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )

    # ----------------------------------------------------------------
    # %%% Interactions avec la GUI
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def get_check_box_status(self):
        if self.checkbox_1_ep.get() == 1:
            # value_ep = "Emport_passager"
            self.radio_var_pb.set(1)
        elif self.checkbox_1_ep.get() == 0:
            # value_ep = "Brevet"
            self.radio_var_pb.set(0)
        # print(value_ep)

    def get_docs_to_fill(self):
        if self.var_checkbox_deb_formation.get() == 1:
            self.docs_to_fill.add("debut_formation")

        if self.var_checkbox_ep_sol.get() == 1:
            self.docs_to_fill.add("ep_sol")

        if self.var_checkbox_ep_vol.get() == 1:
            self.docs_to_fill.add("ep_vol")

        if self.var_checkbox_attest_provisoire.get() == 1:
            self.docs_to_fill.add("attest_provisoire")

        if self.var_checkbox_deb_formation.get() == 0:
            self.docs_to_fill.discard("debut_formation")

        if self.var_checkbox_ep_sol.get() == 0:
            self.docs_to_fill.discard("ep_sol")

        if self.var_checkbox_ep_vol.get() == 0:
            self.docs_to_fill.discard("ep_vol")

        if self.var_checkbox_attest_provisoire.get() == 0:
            self.docs_to_fill.discard("attest_provisoire")

        # print(self.docs_to_fill)

        return self.docs_to_fill

    def try_annotate(self):
        values_to_fill = {}
        if self.radio_var_apte.get() == 0:
            values_to_fill["options_apte_checklist"] = "Apte"
        elif self.radio_var_apte.get() == 1:
            values_to_fill["options_apte_checklist"] = "Ajourne"
        if self.radio_var_pb.get() == 0:
            values_to_fill["brevet_init_or_not"] = "Premier brevet"
        elif self.radio_var_pb.get() == 1:
            values_to_fill["brevet_init_or_not"] = "Ajout classe"
        if self.radio_var_type_ulm.get() == 0:
            values_to_fill["type_ulm"] = "Paramoteur"
        elif self.radio_var_type_ulm.get() == 1:
            values_to_fill["type_ulm"] = "Multiaxe"
        if values_to_fill["type_ulm"] == "Paramoteur":
            values_to_fill["classe_ulm"] = "1 (Paramoteur)"
        elif values_to_fill["type_ulm"] == "Multiaxe":
            values_to_fill["classe_ulm"] = "3 (Multiaxe)"
        else:
            values_to_fill["classe_ulm"] = ""
        if self.checkbox_1_ep.get() == 1:
            values_to_fill["emport_pass_or_not"] = ["Emport de passager"]
        else:
            values_to_fill["emport_pass_or_not"] = []
        values_to_fill["date_deb_formation"] = self.entry_date_deb_formation.get()
        values_to_fill["date_ep_sol"] = self.entry_date_ep_sol.get()
        values_to_fill["date_ep_vol"] = self.entry_date_ep_vol.get()
        values_to_fill[
            "date_deb_attest_provisoire"
        ] = self.entry_date_deb_attest_provisoire.get()
        values_to_fill["date_fin_attest_provisoire"] = (
            pd.to_datetime(values_to_fill["date_deb_attest_provisoire"], dayfirst=True)
            + datetime.timedelta(days=56)
        ).strftime("%d/%m/%Y")
        values_to_fill["fait_le"] = self.entry_fait_le.get()
        values_to_fill["nom_candidat"] = self.entry_nom_candidat.get()
        values_to_fill["prenom_candidat"] = self.entry_prenom_candidat.get()
        values_to_fill["nom_usage_candidat"] = self.entry_nom_usage_candidat.get()
        values_to_fill[
            "date_naissance_candidat"
        ] = self.entry_date_naissance_candidat.get()
        values_to_fill[
            "lieu_naissance_candidat"
        ] = self.entry_lieu_naissance_candidat.get()
        values_to_fill["adresse_candidat"] = self.entry_adresse_candidat.get()
        values_to_fill["commune_candidat"] = self.entry_commune_candidat.get()
        values_to_fill["code_postal_candidat"] = self.entry_code_postal_candidat.get()
        values_to_fill[
            "pays_residence_candidat"
        ] = self.entry_pays_residence_candidat.get()
        values_to_fill[
            "numero_telephone_candidat"
        ] = self.entry_numero_telephone_candidat.get()
        values_to_fill["mail_candidat"] = self.entry_mail_candidat.get()
        values_to_fill["num_licence_candidat"] = self.entry_num_licence_candidat.get()
        values_to_fill["num_ident_ulm"] = self.entry_num_ident_ulm.get()
        values_to_fill["nom_instructeur"] = self.entry_nom_instructeur.get()
        values_to_fill["prenom_instructeur"] = self.entry_prenom_instructeur.get()
        values_to_fill["telephone_instructeur"] = self.entry_telephone_instructeur.get()
        values_to_fill["mail_instructeur"] = self.entry_mail_instructeur.get()
        values_to_fill["numero_licence"] = self.entry_numero_licence.get()
        values_to_fill["date_val_licence"] = self.var_date_val_licence.get()
        values_to_fill["numero_qualification"] = self.entry_numero_qualification.get()
        values_to_fill[
            "date_val_qualification"
        ] = self.entry_date_val_qualification.get()
        values_to_fill["aeorclub_assos"] = self.entry_aeorclub_assos.get()
        values_to_fill["lieu_redaction"] = self.entry_lieu_redaction.get()
        values_to_fill["docs_to_fill"] = self.docs_to_fill

        # print(values_to_fill)
        _ = autofill_functions_tk.annotate_all_pdfs(dict_text=values_to_fill)


if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()
