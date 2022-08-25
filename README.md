# SUBTITLER
Subtitler est un programme minimaliste vous permettant de générer des sous-titres pour vos vidéos.
## Installation
1. Pour commencer, obtenez le code via la commande

`git clone https://github.com/ParfaitD9/subtitler.git`

2. Rendez vous dans le dossier subtitler

`cd subtitler`

3. Créez un environnement virtuel pour les paquets nécéssairees

`python -m venv venv`

4. Activez votre environnement virtuel

**Linux**
`source venv/bin/activate`

**Windows**
`.\venv\Scripts\activate`

5. Installez les paquets

`pip install -r requirements.txt`

Vous êtes maintenant prêt à sous titrer vos vidéos 👍

## Utilisation
### Commandes
La commande pour sous-titrer une vidéo est aussi simple que:

`python main.py subtitle -f <nom_de_la_video.mp4>`

Cette commande vous génère un fichier `<nom_de_la_video.srt>` dans le dossier de la vidéo qui contient les sous-titres de votre vidéo.
|Long|Description|
|----|-----------|
|`subtitle`|Sous titrer une vidéo|
## Arguments
|Long|Court|Description|Défaut|
|----|-----|-----------|------|
|--file|-f|Chemin de la vidéo à sous-titrer|Non défini|
|{--audio, --no-audio}|-a|Conserver ou pas le fichier audio de la vidéo|--no-audio|
|--outdir|-o|Chemin du dossier où générer les sous-titre|Dossier contenant la vidéo|
|--lang|-l|Code de la langue de la vidéo|en-US|