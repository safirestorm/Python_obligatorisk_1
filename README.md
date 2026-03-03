Valuta CLI Program

Et simpelt Python CLI-program, der henter aktuelle valutakurser fra ExchangeRate API.

 1. Hent projektet fra GitHub
git clone https://github.com/DIT-BRUGERNAVN/DIT-REPO-NAVN.git
cd DIT-REPO-NAVN

2. Opret og aktiver virtuelt miljø

Projektet skal køres i et virtual environment.
 Opret miljø:
  python -m venv .venv
 Aktiver miljø:
 Mac/Linux:
  source .venv/bin/activate
 Windows:
  .venv\Scripts\activate

 Når det er aktiveret, vises (.venv) i terminalen.

 3. Installer dependencies
pip install requests python-dotenv

 4. Tilføj API-nøgle (kun første gang)
python valuta.py -key DIN_API_NØGLE

 Programmet opretter automatisk en .env fil og gemmer nøglen.

 5. Kør programmet
python valuta.py

Indtast derefter en valuta, fx:
USD

Programmet viser herefter den aktuelle valutakurs.
