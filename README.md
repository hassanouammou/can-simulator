# CAN Simulator

Simulateur de réseau CAN automobile avec une interface graphique PyQt5. Le projet permet d'observer les trames échangées entre plusieurs nœuds virtuels et d'envoyer des trames manuellement.

## Fonctionnalités

- Diffusion des trames sur un bus CAN simulé.
- Nœud ABS avec émission périodique de données de vitesse et de glissement.
- Nœud moteur avec évolution du régime moteur.
- Nœud porte avec changement périodique d'état.
- Tableau de bord avec décodage des principaux identifiants.
- CanDump pour visualiser les trames reçues.
- Interface graphique affichant l'heure, l'identifiant, les données, le DLC, l'ACK, les erreurs et la source.
- Envoi manuel de trames au format `cansend`.

## Prérequis

- Python 3.
- PyQt5 installé dans l'environnement Python utilisé.

Le projet contient un environnement virtuel local `.venv` lorsqu'il a été créé sur la machine de développement.

## Lancement

Depuis le dossier racine du projet sous PowerShell :

```powershell
.\.venv\Scripts\python.exe main.py
```

Si l'environnement virtuel est déjà activé :

```powershell
python main.py
```

## Utilisation

Dans le champ de commande de l'interface, saisir par exemple :

```text
cansend 0x123 [1,2,3]
```

La trame est diffusée à tous les nœuds connectés au bus et apparaît dans le tableau de supervision.

## Identifiants simulés

| Identifiant | Données | Description |
| --- | --- | --- |
| `0x100` | `[vitesse, slip]` | Données ABS |
| `0x200` | `[octet haut, octet bas]` | Régime moteur en tr/min |
| `0x350` | `[0]` ou `[1]` | Porte fermée ou ouverte |

Les trames envoyées manuellement avec d'autres identifiants sont affichées comme données brutes par le tableau de bord.

## Architecture

```text
CAN-Simulator/
├── main.py                 # Point d'entrée de l'application
├── can_gui.py              # Interface graphique PyQt5
├── engine/
│   ├── can_bus.py          # Bus et diffusion des trames
│   ├── can_frame.py        # Modèle de trame CAN
│   └── can_errors.py       # Réservé à la gestion des erreurs
├── nodes/
│   ├── node_abs.py         # Nœud ABS
│   ├── node_engine.py      # Nœud moteur
│   ├── node_dashboard.py   # Décodage pour le tableau de bord
│   ├── node_door.py        # Nœud porte
│   ├── node_cansend.py     # Émission manuelle
│   └── node_candump.py     # Journalisation des trames
├── cli/                    # Prévu pour une interface terminal
└── gui/                    # Prévu pour une organisation GUI complémentaire
```

## État du projet

Le projet est un prototype fonctionnel. Les prochaines évolutions prévues sont notamment :

- ajouter une validation stricte des identifiants, données et DLC ;
- implémenter la gestion des erreurs CAN ;
- ajouter des tests automatisés ;
- compléter ou retirer les modules CLI et GUI encore vides ;
- améliorer la gestion des messages d'erreur dans l'interface.
