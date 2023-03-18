"""
Fichier principal de l'app dash
"""
# %% Imports
import datetime
import pandas as pd
from dash import Dash, html, dcc, Input, Output, State

import autofill_functions

# %% Init app
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# create the app
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)

colors = {"background": "#111111", "text": "orange"}

options_brevet_initial = [
    "Premier brevet",
    "Ajout classe",
]
options_apte = [
    "Apte",
    "Ajourne",
]
options_type_ulm = ["Paramoteur", "Multiaxe"]
options_emport = ["Emport de passager"]
# %% Page_1-Layout

app.layout = html.Div(
    # style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            "Informations à renseigner",
            style={"textAlign": "center", "color": "#2c75ff"},
        ),
        html.Br(),
        html.Div(
            children=html.H2(
                "Généralités :",
                style={"textAlign": "left", "color": colors["text"]},
            )
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.RadioItems(
                            options=options_apte,
                            value="Apte",
                            id="options_apte_checklist",
                            inline=True,
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        dcc.RadioItems(
                            options=options_brevet_initial,
                            value="Premier brevet",
                            id="options_brevet_initial_checklist",
                            inline=True,
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        dcc.RadioItems(
                            options=options_type_ulm,
                            value="Paramoteur",
                            id="options_type_ulm_checklist",
                            inline=True,
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        dcc.Checklist(
                            options=options_emport,
                            value=[],
                            id="options_emport_checklist",
                            inline=True,
                        ),
                    ]
                ),
            ],
            # style={"display": "flex", "flex-direction": "row"},
        ),
        html.Br(),
        html.Div(
            children=html.H2(
                "Les dates (format = JJ/MM/AAAA) :",
                style={"textAlign": "left", "color": colors["text"]},
            )
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label("Date début de formation"),
                        dcc.Input(
                            id="date_deb_formation",
                            value="",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Date épreuve sol"),
                        dcc.Input(
                            id="date_ep_sol",
                            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Date épreuve vol"),
                        dcc.Input(
                            id="date_ep_vol",
                            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Date d'effet attestation provisoire"),
                        dcc.Input(
                            id="date_deb_attest_provisoire",
                            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Fait le :"),
                        dcc.Input(
                            id="fait_le",
                            value=f"{datetime.datetime.now().strftime('%d/%m/%Y')}",
                            type="text",
                        ),
                    ]
                ),
            ],
            # style={"display": "flex", "flex-direction": "row"},
        ),
        html.Br(),
        html.Div(
            children=html.H2(
                "Le candidat :",
                style={"textAlign": "left", "color": colors["text"]},
            )
        ),
        html.Div(
            children=[
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.Label("Nom"),
                                dcc.Input(
                                    id="nom_candidat",
                                    value="",
                                    type="text",
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Prénom"),
                                dcc.Input(
                                    id="prenom_candidat",
                                    value="",
                                    type="text",
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Nom d'usage si différent"),
                                dcc.Input(
                                    id="nom_usage_candidat", value="", type="text"
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Date de naissance"),
                                dcc.Input(
                                    id="date_naissance_candidat", value="", type="text"
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Lieu de naissance"),
                                dcc.Input(
                                    id="lieu_naissance_candidat", value="", type="text"
                                ),
                            ]
                        ),
                    ],
                    style={"display": "flex"},
                ),
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.Label("Adresse"),
                                dcc.Input(id="adresse_candidat", value="", type="text"),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Commune"),
                                dcc.Input(id="commune_candidat", value="", type="text"),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Code postal"),
                                dcc.Input(
                                    id="code_postal_candidat", value="", type="text"
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Pays de résidence"),
                                dcc.Input(
                                    id="pays_residence_candidat",
                                    value="France",
                                    type="text",
                                ),
                            ]
                        ),
                    ],
                    style={"display": "flex"},
                ),
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.Label("Numéro de téléphone"),
                                dcc.Input(
                                    id="numero_telephone_candidat",
                                    value="",
                                    type="text",
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("Adresse e-mail"),
                                dcc.Input(id="mail_candidat", value="", type="text"),
                            ]
                        ),
                    ],
                    style={"display": "flex"},
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Label("N° de licence (si applicable)"),
                                dcc.Input(
                                    id="num_licence_candidat",
                                    value="----------",
                                    type="text",
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Label("N° identification ULM"),
                                dcc.Input(id="num_ident_ulm", value="", type="text"),
                            ]
                        ),
                    ],
                    style={"display": "flex"},
                ),
            ],
            # style={"display": "flex"},
        ),
        html.Br(),
        html.H2(
            "L'instructeur :",
            style={"textAlign": "left", "color": colors["text"]},
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label("Nom"),
                        dcc.Input(
                            id="nom_instructeur",
                            value="CHIRON",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Prénom"),
                        dcc.Input(
                            id="prenom_instructeur",
                            value="Christophe",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("N° téléphone"),
                        dcc.Input(
                            id="telephone_instructeur",
                            value="06.61.19.53.82",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Adresse e-mail"),
                        dcc.Input(
                            id="mail_instructeur",
                            value="ckchiron@yahoo.fr",
                            type="text",
                        ),
                    ]
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label("N° de licence"),
                        dcc.Input(id="numero_licence", value="0305004006", type="text"),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("N° qualif instructeur"),
                        dcc.Input(
                            id="numero_qualification",
                            value="ULM 0300004006",
                            type="text",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Date fin validité n° qualif"),
                        dcc.Input(
                            id="date_val_qualification",
                            value="31/07/2023",
                            type="text",
                        ),
                    ]
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label("Aéroclub/Association"),
                        dcc.Input(
                            id="aeorclub_assos", value="Air Race Pro", type="text"
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Fait à"),
                        dcc.Input(
                            id="lieu_redaction", value="Voeuil-et-Giget", type="text"
                        ),
                    ]
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        html.Br(),
        # html.H2(
        #     "Autres informations :",
        #     style={"textAlign": "left", "color": colors["text"]},
        # ),
        # html.Div(
        #     children=[
        #         html.Label("Type d'activité"),
        #         dcc.Input(id="type_activite", value="PARAMOTEUR", type="text"),
        #     ]
        # ),
        # html.Br(),
        html.Div(
            children=[
                html.Button(
                    children="Télécharger les pdf", id="generate_pdf", n_clicks=0
                )
            ]
        ),
        html.Div(
            children=[dcc.Download(id="test_generate")]
        ),  # html.Label(id="test_generate", children="PDF générés !")]),
    ],
)

values_to_fill = {}

# options_apte_checklist
# options_brevet_initial_checklist
# options_type_ulm_checklist
# options_emport_checklist
# date_deb_formation
# date_ep_sol
# date_ep_vol
# date_deb_attest_provisoire
# fait_le
# nom_candidat
# prenom_candidat
# nom_usage_candidat
# date_naissance_candidat
# lieu_naissance_candidat
# adresse_candidat
# commune_candidat
# code_postal_candidat
# pays_residence_candidat
# numero_telephone_candidat
# mail_candidat
# num_licence_candidat
# num_ident_ulm
# nom_instructeur
# prenom_instructeur
# telephone_instructeur
# mail_instructeur
# numero_licence
# numero_qualification
# date_val_qualification
# aeorclub_assos
# lieu_redaction


@app.callback(
    Output("test_generate", "data"),
    Input("generate_pdf", "n_clicks"),
    [
        State("options_apte_checklist", "value"),
        State("options_brevet_initial_checklist", "value"),
        State("options_type_ulm_checklist", "value"),
        State("options_emport_checklist", "value"),
        State("date_deb_formation", "value"),
        State("date_ep_sol", "value"),
        State("date_ep_vol", "value"),
        State("date_deb_attest_provisoire", "value"),
        State("fait_le", "value"),
        State("nom_candidat", "value"),
        State("prenom_candidat", "value"),
        State("nom_usage_candidat", "value"),
        State("date_naissance_candidat", "value"),
        State("lieu_naissance_candidat", "value"),
        State("adresse_candidat", "value"),
        State("commune_candidat", "value"),
        State("code_postal_candidat", "value"),
        State("pays_residence_candidat", "value"),
        State("numero_telephone_candidat", "value"),
        State("mail_candidat", "value"),
        State("num_licence_candidat", "value"),
        State("num_ident_ulm", "value"),
        State("nom_instructeur", "value"),
        State("prenom_instructeur", "value"),
        State("telephone_instructeur", "value"),
        State("mail_instructeur", "value"),
        State("numero_licence", "value"),
        State("numero_qualification", "value"),
        State("date_val_qualification", "value"),
        State("aeorclub_assos", "value"),
        State("lieu_redaction", "value"),
    ],
    prevent_initial_call=True,
)
def update_output(
    n_clicks,
    options_apte_checklist,
    brevet_init_or_not,
    type_ulm,
    emport_pass_or_not,
    date_deb_formation,
    date_ep_sol,
    date_ep_vol,
    date_deb_attest_provisoire,
    fait_le,
    nom_candidat,
    prenom_candidat,
    nom_usage_candidat,
    date_naissance_candidat,
    lieu_naissance_candidat,
    adresse_candidat,
    commune_candidat,
    code_postal_candidat,
    pays_residence_candidat,
    numero_telephone_candidat,
    mail_candidat,
    num_licence_candidat,
    num_ident_ulm,
    nom_instructeur,
    prenom_instructeur,
    telephone_instructeur,
    mail_instructeur,
    numero_licence,
    numero_qualification,
    date_val_qualification,
    aeorclub_assos,
    lieu_redaction,
):
    """
    Fonction assurant la création des valeurs à partir
    du formulaire et l'appel des fonctions assurant l'annotation
    des pdfs.
    """
    if n_clicks > 0:
        values_to_fill["options_apte_checklist"] = options_apte_checklist
        values_to_fill["brevet_init_or_not"] = brevet_init_or_not
        values_to_fill["type_ulm"] = type_ulm
        if type_ulm == "Paramoteur":
            values_to_fill["classe_ulm"] = "1 (Paramoteur)"
        elif type_ulm == "Multiaxe":
            values_to_fill["classe_ulm"] = "3 (Multiaxe)"
        else:
            values_to_fill["classe_ulm"] = ""
        values_to_fill["emport_pass_or_not"] = emport_pass_or_not
        values_to_fill["date_deb_formation"] = date_deb_formation
        values_to_fill["date_ep_sol"] = date_ep_sol
        values_to_fill["date_ep_vol"] = date_ep_vol
        values_to_fill["date_deb_attest_provisoire"] = date_deb_attest_provisoire
        values_to_fill["date_fin_attest_provisoire"] = (
            pd.to_datetime(values_to_fill["date_deb_attest_provisoire"], dayfirst=True)
            + datetime.timedelta(days=56)
        ).strftime("%d/%m/%Y")
        values_to_fill["fait_le"] = fait_le
        values_to_fill["nom_candidat"] = nom_candidat
        values_to_fill["prenom_candidat"] = prenom_candidat
        values_to_fill["nom_usage_candidat"] = nom_usage_candidat
        values_to_fill["date_naissance_candidat"] = date_naissance_candidat
        values_to_fill["lieu_naissance_candidat"] = lieu_naissance_candidat
        values_to_fill["adresse_candidat"] = adresse_candidat
        values_to_fill["commune_candidat"] = commune_candidat
        values_to_fill["code_postal_candidat"] = code_postal_candidat
        values_to_fill["pays_residence_candidat"] = pays_residence_candidat
        values_to_fill["numero_telephone_candidat"] = numero_telephone_candidat
        values_to_fill["mail_candidat"] = mail_candidat
        values_to_fill["num_licence_candidat"] = num_licence_candidat
        values_to_fill["num_ident_ulm"] = num_ident_ulm
        values_to_fill["nom_instructeur"] = nom_instructeur
        values_to_fill["prenom_instructeur"] = prenom_instructeur
        values_to_fill["telephone_instructeur"] = telephone_instructeur
        values_to_fill["mail_instructeur"] = mail_instructeur
        values_to_fill["numero_licence"] = numero_licence
        values_to_fill["date_val_licence"] = "-----------"
        values_to_fill["numero_qualification"] = numero_qualification
        values_to_fill["date_val_qualification"] = date_val_qualification
        values_to_fill["aeorclub_assos"] = aeorclub_assos
        values_to_fill["lieu_redaction"] = lieu_redaction
        # print(values_to_fill)
        file_to_save = autofill_functions.annotate_all_pdfs(dict_text=values_to_fill)
        return dcc.send_file(path=str(file_to_save))


@app.callback(
    Output("generate_pdf", "style"),
    [Input("generate_pdf", "n_clicks")],
)
def update_button_color(n_clicks):
    """
    Fonction permettant de changer la couleur du bouton une fois qu'on a cliqué dessus.
    """
    if n_clicks:
        return {"backgroundColor": "green"}
    else:
        return {}


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8110)
