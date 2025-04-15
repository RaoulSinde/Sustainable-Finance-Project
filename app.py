import streamlit as st
import data_finance_verte as dfv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Page d'accueil : Vue Globale
# ------------------------------
def show_home():
    st.title("Green Asset Management - Portefeuille Vert")
    
    tickers = dfv.tickers  
    start_date = "2019-01-01"
    end_date = "2024-12-31"
    wallet_stats = dfv.get_wallet_statistics(tickers, start=start_date, end=end_date)
    
    
    st.markdown("""
    ### ♻️ Bienvenue sur notre application de suivi du **Portefeuille Vert**

    Notre **Portefeuille Vert** est une solution d’investissement durable, conçue pour allier **performance financière** et **impact environnemental et sociétal positif**.  
    Il intègre une large gamme d’instruments sélectionnés selon des critères rigoureux d’investissement responsable :

    ✅ **Actions** d’entreprises engagées dans la transition écologique  
    ✅ **Fonds durables** (ETF thématiques ESG)  
    ✅ **Obligations vertes** finançant des projets environnementaux  
    ✅ **SCPI responsables** axées sur l’immobilier durable et la rénovation énergétique

    ---

    ### 🌿 Une approche globale de l’investissement responsable

    Ce portefeuille vise à représenter une **allocation diversifiée** sur des actifs verts et éthiques, à travers différents secteurs et classes d’actifs, tout en suivant une stratégie d’analyse rigoureuse et quantitative :

    📌 **Sélection basée sur des critères ESG** : gouvernance, politique climatique, impact social  
    📌 **Exclusion des secteurs polluants** : charbon, hydrocarbures non conventionnels, armement  
    📌 **Poids équilibrés et transparents** pour limiter les risques et suivre la performance réelle

    ---

    ### 📊 Que propose cette application ?

    Cette plateforme vous permet de :

    - Explorer la **composition détaillée du portefeuille** : titres, fonds, obligations, SCPI  
    - Suivre les **performances financières** : rendement annuel, volatilité, corrélations  
    - Visualiser les **statistiques dynamiques** et graphiques interactifs  
    - Comprendre les choix d’investissement et les enjeux sous-jacents à chaque actif

    ---

    **Notre ambition :** démontrer qu’un investissement responsable peut être à la fois **éthique, rentable et résilient**.

    Utilisez le menu de navigation à gauche pour découvrir nos **critères de sélection**, les **détails du portefeuille**, ainsi que ses **performances**.
    """)
    
# ------------------------------
# Page Critères de Sélection
# ------------------------------
def show_criterias():
    st.title("Nos critères de sélection")

    st.markdown("""
    ### 1) Critères de sélection des actions

    Pour la sélection des actions composant notre portefeuille, nous nous appuyons principalement sur les **données ESG fournies par MSCI**, en appliquant une grille de critères exigeante et cohérente avec notre stratégie d'investissement responsable.
    #### Engagement de l’entreprise à réduire ses émissions de carbone
    Nous sélectionnons uniquement des entreprises qui :
    - Se sont engagées à réduire durablement leurs émissions de gaz à effet de serre ;
    - Présentent des engagements jugés **crédibles, précis et suffisamment transparents** ;
    - Ont des objectifs de réduction couvrant **100 % de leur empreinte carbone**, incluant :
    - **Scope 1** : émissions directes de l’entreprise  
    - **Scope 2** : émissions indirectes liées à la consommation d’énergie  
    - **Scope 3** : autres émissions indirectes (amont et aval de la chaîne de valeur)
    - Dont les engagements climatiques sont **compatibles avec une trajectoire de réchauffement < 1,5°C**, conformément à l’Accord de Paris.

    #### Notation ESG MSCI
    Nous excluons les entreprises ayant une **note ESG inférieure à AA** :
    - **A ou moins** : l’entreprise ne gère que partiellement, ou de manière insuffisante, ses risques ESG  
    - **AA** : entreprise leader dans la gestion de ses enjeux ESG  
    - **AAA** : meilleure note possible, gestion exemplaire


    #### Controverses ESG
    Nous ne sélectionnons pas les entreprises confrontées à des **controverses ESG majeures**. Pour chaque pilier (Environnement, Social, Gouvernance), nous exigeons une **note de controverse** inférieure ou égale à O (modéré à élevé) et au moins une note égale à G (très bien)".

    #### Implication dans des secteurs controversés
    Nous excluons les entreprises impliquées dans des **secteurs controversés**, à l’exception de celles actives dans le **tabac** ou l’**alcool**, pour lesquelles une **note ESG minimale de AA** est exigée.

    ---
    ### 2) Critères de sélection pour les fonds et ETF
    Nous ne sélections que des fodns et ETF qui suivent l'article 9 du réglement SFDR.
    
    Pourquoi l’article 9 ?
    Les fonds article 9 sont ceux qui ont un objectif d’investissement durable explicite. Contrairement aux fonds article 8 (qui « promeuvent » des caractéristiques ESG), les article 9 doivent démontrer que leur stratégie vise réellement un impact positif mesurable (ex. : réduction des émissions, inclusion sociale, etc.).
    Ils offrent ainsi une transparence renforcée et permettent aux investisseurs de s’assurer que leur capital finance des projets alignés avec des objectifs concrets de durabilité, tels que ceux définis par les Objectifs de Développement Durable (ODD) ou l’Accord de Paris.

    ---
    ### 3) Critères de sélection pour les obligations
    Nous ne sélectionnons que des obligations vertes qui ont le label Greenfin. Ce label est attribué par le Ministère de la Transition Écologique et Solidaire en France, garantissant que les fonds levés par l’émission d’obligations vertes sont utilisés pour financer des projets ayant un impact environnemental positif.
    Les obligations vertes labellisées Greenfin doivent répondre à des critères stricts, notamment :
    - Utilisation des fonds exclusivement pour des projets verts (énergies renouvelables, efficacité énergétique, gestion durable de l’eau, etc.)
    - Transparence sur l’utilisation des fonds et le suivi des projets financés
    - Engagement à respecter des normes environnementales élevées
    
    

    ---
    ### 4) Critères de sélection pour les SCPI
    Concernant les SCPI, nous ne sélectionnons que celles qui sont labellisées ISR (Investissement Socialement Responsable) et qui visent notamment à améliorer la performance énergétique de leurs actifs immobiliers.
    
    Le label ISR est un label français qui garantit que la SCPI respecte des critères environnementaux, sociaux et de gouvernance (ESG) dans sa gestion. Les SCPI labellisées ISR doivent démontrer :
    - Un engagement à améliorer la performance énergétique de leurs actifs immobiliers
    - Une stratégie d’investissement responsable intégrant des critères ESG
    - Une transparence sur les impacts environnementaux et sociaux de leurs investissements
    - Un suivi régulier des performances ESG de leur portefeuille immobilier
    

   
    ---
    """)
    

# ------------------------------
# Page Détails du Portefeuille
# ------------------------------
def show_details():
    st.title("Détails du Portefeuille depuis 2019")

    st.subheader("Un portefeuille aligné avec les objectifs de l'accord de Paris")
    temperatures = [1.4, 1.3, 1.5, 1.4, 1.5, 1.3, 1.5, 1.5]
    st.markdown(f"Température implicite de la partie Actions du portefeuille : {np.mean(temperatures):.2f}°C ✅")
    st.markdown("Nous pondérons la température implicite de chaque actif en fonction de sa part dans le portefeuille. (notre portefeuille est équipondéré)")

    st.subheader("Composition actuelle du portefeuille vert")
    
    st.markdown("Le portefeuille est construit selon une répartition équipondérée entre l’ensemble des valeurs qu’il contient.")
    
    st.markdown("""
    #### 🏢 **Actions durables**
    - **MICROSOFT CORPORATION (MSFT)** 
    - **L’OREAL SA (OR)** 
    - **BOUYGUES SA (EN)** 
    - **CARREFOUR SA (CA)**
    - **UNILEVER PLC (ULVR)** 
    - **SCHNEIDER ELECTRIC SE (SU)** 
    - **SAP SE (SAP)** 
    - **ALLIANZ SE (ALV.DE)** 

    #### 🌍 **Fonds & ETF ESG**
    - **AMUNDI EURO GOVERNMENT GREEN BOND UCITS ETF ACC (EART.L)** 
    - **Invesco MSCI World ESG Climate Paris Aligned UCITS ETF Acc (PAWD.L)** 

    #### 💸 **Obligations vertes**
    - **Obligations Assimilables au Trésor (OAT) vertes France**

    #### 🏠 **SCPI responsables**
    - **SCPI Accimmo Pierre, BNP Paribas REIM** 

    ---

    Pour en savoir plus sur chaque actif, sélectionnez un titre dans le menu déroulant ci-dessous.

    """)
    
    # Liste des tickers 
    tickers = ["MSFT", "OR", "EN.PA", "CA", "UL", "SU", "SAP", "ALV.DE", "EART.L", "PAWD.L", "SCPI Accimmo Pierre"]

    # Sélection d'un titre parmi ceux composant le portefeuille
    selected_ticker = st.selectbox("Sélectionnez un titre", tickers)

    # Dictionnaire associant une description spécifique à chaque titre
    ticker_descriptions = {
        "MSFT": """Nom : Microsoft Corporation  
- Objectif de décarbonation : Oui, objectif fixé à 2045, couvrant l’intégralité des émissions (Scopes 1, 2 et 3), avec un engagement clair, crédible et transparent  
- Température implicite : 1,4°C — indique une trajectoire alignée avec les objectifs climatiques internationaux de 1,5°C
- Note ESG MSCI : A. Microsoft se situe dans la moyenne parmi 460 entreprises du secteur des logiciels et des services.  
- Controverses ESG : Environnement: G (green, très bien), Social : Y (yellow : modéré), Gouvernance : Y (yellow : modéré)
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "OR": """Nom : L’Oréal SA  
- Objectif de décarbonation : Oui, objectif fixé à 2050, couvrant 100 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,3°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AA. L’Oréal est reconnue comme un leader dans la gestion de ses enjeux ESG  
- Controverses ESG : Environnement : G (green, très bien), Social : O (orange, modéré à élevé), Gouvernance : G (green, très bien)  
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "EN.PA": """Nom : Bouygues SA  
- Objectif de décarbonation : Oui, objectif fixé à 2050, couvrant 97 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,5°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AA. Bouygues est reconnue comme un leader dans la gestion de ses enjeux ESG  
- Controverses ESG : Environnement : G (green, très bien), Social : O (orange, modéré à élevé), Gouvernance : G (green, très bien)  
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "CA": """Nom : Carrefour SA  
- Objectif de décarbonation : Oui, objectif fixé à 2040, couvrant 100 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,4°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AA. Carrefour est reconnu comme un leader dans la gestion de ses enjeux ESG  
- Controverses ESG : Environnement : Y (yellow, modéré), Social : O (orange, modéré à élevé), Gouvernance : G (green, très bien)  
- Activités controversées : Implication dans les secteurs du tabac et de l’alcool. Maintenu dans le portefeuille car sa note ESG est supérieure ou égale à AA, conformément à notre politique de sélection
""",
        "UL": """Nom : Unilever PLC  
- Objectif de décarbonation : Oui, objectif fixé à 2040, couvrant 100 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,5°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AAA. Unilever est considéré comme un exemple en matière de gestion des enjeux ESG  
- Controverses ESG : Environnement : O (orange, modéré à élevé), Social : Y (yellow, modéré), Gouvernance : G (green, très bien)  
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "SU": """Nom : Schneider Electric SE  
- Objectif de décarbonation : Oui, objectif fixé à 2040, couvrant 100 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,3°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AAA. Schneider Electric est un leader mondial reconnu pour la qualité de sa gestion ESG  
- Controverses ESG : Environnement : G (green, très bien), Social : O (orange, modéré à élevé), Gouvernance : G (green, très bien)  
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "SAP": """Nom : SAP SE  
- Objectif de décarbonation : Oui, objectif fixé à 2030, couvrant 100 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,5°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AA. SAP est reconnu comme un leader dans la gestion de ses enjeux ESG  
- Controverses ESG : Environnement : G (green, très bien), Social : O (orange, modéré à élevé), Gouvernance : G (green, très bien)  
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "ALV.DE": """Nom : ALLIANZ SE
- Objectif de décarbonation : Oui, objectif fixé à 2050, couvrant 100 % des émissions (Scopes 1, 2 et 3), avec un plan compréhensible  
- Température implicite : 1,5°C — trajectoire alignée avec les objectifs climatiques internationaux  
- Note ESG MSCI : AA. Allianz est reconnu comme un leader dans la gestion de ses enjeux ESG   
- Controverses ESG : Environnement : G (green, très bien), Social : Y (yellow, modéré), Gouvernance : Y (yellow, modéré)  
- Activités controversées : Aucune implication dans des activités controversées selon MSCI
""",
        "EART.L": """- Nom : AMUNDI EURO GOVERNMENT GREEN BOND UCITS ETF ACC  
- Émetteur : Amundi   
- ISIN : LU2356220926  
- Label : Article 9 SFDR   
- Objectif d'investissement : Ce fond a pour objectif de répliquer l’indice Solactive Euro Government Green Bond Index. Cet indice représente la performance des obligations vertes de qualité “investment grade“ émises par des pays européens et libellées en EUR. Les obligations vertes sont émises à des fins de financement de projets avec un impact positif sur l’environnement. Pour être éligible à l’indice, une obligation doit être considérée comme ‘obligation verte’ par la Climate Bonds Initiative et répondre à certains critères spécifiques.""",
        
        "PAWD.L": """- Nom : Invesco MSCI World ESG Climate Paris Aligned UCITS ETF Acc    
- Émetteur : Invesco     
- ISIN : IE000V93BNU0  
- Label : Article 9 SFDR   
- Objectf d'investissement : Cet ETF vise à fournir la performance de rendement total net de l'indice MSCI World ESG Climate Paris Aligned Benchmark Select (l'" indice de référence "). L'indice de référence suit la performance des entreprises de moyenne et grande capitalisation des marchés développés du monde entier et vise à réduire l'exposition aux risques climatiques physiques et transitoires, tout en poursuivant les opportunités découlant de la transition vers une économie à faible émission de carbone, conformément aux exigences de l'Accord de Paris. En outre, l'indice de référence offre une exposition aux entreprises présentant des métriques ESG élevées, intègre les recommandations de la Task Force on Climate Related Financial Disclosures (TCFD) et est conçu pour dépasser les normes minimales de l'indice de référence aligné sur Paris de l'UE, telles que définies dans le règlement délégué (UE) 2020/1818 de la Commission.""",
       
       "SCPI Accimmo Pierre": """- Nom : SCPI Accimmo Pierre   
- Émetteur : BNP Paribas REIM    
- Label : ISR
- Objectf d'investissement : Accimmo Pierre adopte une approche “best-in-progress”, visant à améliorer la performance ESG de ses actifs existants. Elle investit notamment dans des immeubles récents de haute qualité, dont certains sont certifiés HQE. Par exemple, son acquisition du siège du Conseil Régional d’Île-de-France, livré début 2020, bénéficie de la certification HQE Conception “Excellent”.""",
       
    }

    # Affichage de l'analyse détaillée du titre sélectionné
    st.markdown(f"### Analyse détaillée du titre : {selected_ticker}")
    if selected_ticker in ticker_descriptions:
        st.write(ticker_descriptions[selected_ticker])
    else:
        st.write("Aucune description disponible pour ce titre actuellement.")

   

# ------------------------------
# Page Performances
# ------------------------------
def show_performances():
    st.title("Performances du Portefeuille")
    
    st.markdown("Le portefeuille présente de très bonnes performances. Il est bien diversifié comme le montre la matrice de corrélation présentée ci-dessous, permettant ainsi de réduire le risque. De plus, ses rendements cumulés sont comparables, quoique légèrement inférieurs, à ceux du S&P 500 sur la période étudiée. Cela témoigne de la solidité de notre stratégie d’investissement responsable.")

    # Définition de la période d'analyse
    start_date = "2019-01-01"
    end_date = "2024-12-31"
    tickers = dfv.tickers  # La liste des actifs du portefeuille
    
    # Récupération des statistiques du portefeuille
    wallet_stats = dfv.get_wallet_statistics(tickers, start=start_date, end=end_date)

    # Récupération des données du S&P 500 et calcul de ses rendements
    spx_data = dfv.get_stock_statistics("^SPX", start=start_date, end=end_date)["returns"]
    
    # Affichage des indicateurs clés via des "metrics"
    st.subheader("Statistiques Clés")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rendement annuel", f"{wallet_stats['portfolio_annual_return']:.2f}")
    col2.metric("Volatilité annuelle", f"{wallet_stats['portfolio_annual_volatility']:.2f}")
    col3.metric("Ratio de Sharpe", f"{wallet_stats['portfolio_sharpe_ratio']:.2f}")

    st.subheader("Performances de la SCPI")    
    # Affichage des performances de la SCPI   
    st.markdown("Rendements annuels")
    st.markdown("2019 : 4,01%  \n  2020 : 3,81%  \n  2021 : 4,61%  \n  2022 : 3,80%  \n  2023 : 3,51%")
    
    # Section graphique
    st.subheader("Graphiques")
    
    # Graphique 1 : Histogramme des rendements annuels moyens par actif
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    mean_returns = wallet_stats["mean_annual_returns"]
    ax1.bar(mean_returns.index, mean_returns.values)
    ax1.set_title("Rendements annuels moyens par Actif")
    ax1.set_ylabel("Rendement annuel (%)")
    ax1.set_xlabel("Actif")
    st.pyplot(fig1)
    
    # Graphique 2 : Heatmap de la matrice de corrélation
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    corr_matrix = wallet_stats["correlation_matrix"]
    cax = ax2.imshow(corr_matrix, interpolation='nearest', cmap='coolwarm')
    fig2.colorbar(cax)
    ax2.set_xticks(np.arange(len(corr_matrix.columns)))
    ax2.set_yticks(np.arange(len(corr_matrix.index)))
    ax2.set_xticklabels(corr_matrix.columns, rotation=90)
    ax2.set_yticklabels(corr_matrix.index)
    ax2.set_title("Matrice de Corrélation", pad=20)
    st.pyplot(fig2)
    
    # Calcul de la performance du portefeuille équipondéré
    daily_returns = wallet_stats["daily_returns"]

    # Moyenne simple des rendements disponibles chaque jour
    portfolio_daily_returns = daily_returns.mean(axis=1, skipna=True)

    # Performance cumulée du portefeuille
    portfolio_cumulative_returns = (1 + portfolio_daily_returns).cumprod()

    # Calcul de la performance cumulée du S&P 500
    spx_cumulative_returns = (1 + spx_data).cumprod()

    # Création du graphique
    fig3, ax3 = plt.subplots(figsize=(10, 5))

    # Tracer la performance cumulée du portefeuille
    portfolio_cumulative_returns.plot(ax=ax3, label="Portefeuille", color="blue")

    # Tracer la performance cumulée du S&P 500
    spx_cumulative_returns.plot(ax=ax3, label="S&P 500", color="red")

    # Ajouter un titre, un label et une légende
    ax3.set_title("Performance du Portefeuille Équipondéré vs S&P 500")
    ax3.set_ylabel("Valeur du Portefeuille")
    ax3.set_xlabel("Date")
    ax3.legend()

    # Affichage du graphique dans Streamlit
    st.pyplot(fig3)

# ------------------------------
# Navigation via la barre latérale
# ------------------------------
page = st.sidebar.radio("Navigation", ["Accueil 🏡", "Critères de sélection ✔️", "Détails du portefeuille 📋", "Performances 📈"])

if page == "Accueil 🏡":
    show_home()
elif page == "Critères de sélection ✔️":
    show_criterias()
elif page == "Détails du portefeuille 📋":
    show_details()
elif page == "Performances 📈":
    show_performances()
