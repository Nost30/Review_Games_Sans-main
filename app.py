from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}

# Datos iniciales de ejemplo
videojuegos = [
    {
        'id': 1,
        'nombre': 'The Legend of Zelda: Breath of the Wild',
        'genero': 'Aventura',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Nintendo',
        'puntaje_metacritic': 97,
        'puntaje_usuarios': 8.5
    },
    {
        'id': 2,
        'nombre': 'God of War',
        'genero': 'Acción',
        'plataforma': 'PlayStation 4',
        'desarrolladora': 'Santa Monica Studio',
        'puntaje_metacritic': 94,
        'puntaje_usuarios': 9.1
    },
    {
        'id': 3,
        'nombre': 'Red Dead Redemption 2',
        'genero': 'Acción-aventura',
        'plataforma': 'PlayStation 4, Xbox One, PC',
        'desarrolladora': 'Rockstar Games',
        'puntaje_metacritic': 96,
        'puntaje_usuarios': 9.0
    },
    {
        'id': 4,
        'nombre': 'The Witcher 3: Wild Hunt',
        'genero': 'RPG',
        'plataforma': 'PlayStation 4, Xbox One, PC, Nintendo Switch',
        'desarrolladora': 'CD Projekt Red',
        'puntaje_metacritic': 93,
        'puntaje_usuarios': 9.4
    },
    {
        'id': 5,
        'nombre': 'Super Mario Odyssey',
        'genero': 'Plataformas',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Nintendo',
        'puntaje_metacritic': 97,
        'puntaje_usuarios': 8.9
    },
    {
        'id': 6,
        'nombre': 'Minecraft',
        'genero': 'Sandbox',
        'plataforma': 'Multiplataforma',
        'desarrolladora': 'Mojang',
        'puntaje_metacritic': 93,
        'puntaje_usuarios': 8.7
    },
    {
        'id': 7,
        'nombre': 'Persona 5',
        'genero': 'JRPG',
        'plataforma': 'PlayStation 4',
        'desarrolladora': 'Atlus',
        'puntaje_metacritic': 93,
        'puntaje_usuarios': 9.1
    },
    {
        'id': 8,
        'nombre': 'Sekiro: Shadows Die Twice',
        'genero': 'Acción-aventura',
        'plataforma': 'PlayStation 4, Xbox One, PC',
        'desarrolladora': 'FromSoftware',
        'puntaje_metacritic': 91,
        'puntaje_usuarios': 8.2
    },
    {
        'id': 9,
        'nombre': 'Dark Souls III',
        'genero': 'RPG',
        'plataforma': 'PlayStation 4, Xbox One, PC',
        'desarrolladora': 'FromSoftware',
        'puntaje_metacritic': 89,
        'puntaje_usuarios': 8.9
    },
    {
        'id': 10,
        'nombre': 'Hades',
        'genero': 'Roguelike',
        'plataforma': 'PC, Nintendo Switch',
        'desarrolladora': 'Supergiant Games',
        'puntaje_metacritic': 93,
        'puntaje_usuarios': 8.8
    },
    {
    'id': 11,
    'nombre': 'Cyberpunk 2077',
    'genero': 'RPG',
    'plataforma': 'PlayStation 4, Xbox One, PC',
    'desarrolladora': 'CD Projekt Red',
    'puntaje_metacritic': 86,
    'puntaje_usuarios': 7.0
 },
 {
        'id': 12,
        'nombre': 'Animal Crossing: New Horizons',
        'genero': 'Simulación',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Nintendo',
        'puntaje_metacritic': 90,
        'puntaje_usuarios': 8.1
    },
    {
        'id': 13,
        'nombre': 'Doom Eternal',
        'genero': 'Shooter',
        'plataforma': 'PlayStation 4, Xbox One, PC, Stadia',
        'desarrolladora': 'id Software',
        'puntaje_metacritic': 88,
        'puntaje_usuarios': 8.6
    },
    {
        'id': 14,
        'nombre': 'Ghost of Tsushima',
        'genero': 'Acción-aventura',
        'plataforma': 'PlayStation 4',
        'desarrolladora': 'Sucker Punch Productions',
        'puntaje_metacritic': 83,
        'puntaje_usuarios': 8.1
    },
    {
        'id': 15,
        'nombre': 'Among Us',
        'genero': 'Partido en línea',
        'plataforma': 'iOS, Android, PC',
        'desarrolladora': 'InnerSloth',
        'puntaje_metacritic': 83,
        'puntaje_usuarios': 6.4
    },
    {
        'id': 16,
        'nombre': 'The Last of Us Part II',
        'genero': 'Acción-aventura',
        'plataforma': 'PlayStation 4',
        'desarrolladora': 'Naughty Dog',
        'puntaje_metacritic': 93,
        'puntaje_usuarios': 5.7
    },
    {
        'id': 17,
        'nombre': 'Hollow Knight',
        'genero': 'Metroidvania',
        'plataforma': 'PC, Nintendo Switch, PlayStation 4, Xbox One',
        'desarrolladora': 'Team Cherry',
        'puntaje_metacritic': 90,
        'puntaje_usuarios': 8.7
    },
    {
        'id': 18,
        'nombre': 'Celeste',
        'genero': 'Plataformas',
        'plataforma': 'PC, Nintendo Switch, PlayStation 4, Xbox One',
        'desarrolladora': 'Maddy Makes Games',
        'puntaje_metacritic': 92,
        'puntaje_usuarios': 8.8
    },{
        'id': 19,
        'nombre': 'Stardew Valley',
        'genero': 'Simulación',
        'plataforma': 'PC, PlayStation 4, Xbox One, Nintendo Switch, iOS, Android',
        'desarrolladora': 'ConcernedApe',
        'puntaje_metacritic': 89,
        'puntaje_usuarios': 9.0
    },
    {
        'id': 20,
        'nombre': 'Ori and the Will of the Wisps',
        'genero': 'Metroidvania',
        'plataforma': 'PC, Xbox One, Nintendo Switch',
        'desarrolladora': 'Moon Studios',
        'puntaje_metacritic': 88,
        'puntaje_usuarios': 8.7
    },
    {
        'id': 21,
        'nombre': 'Pokémon Sword',
        'genero': 'RPG',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': 80,
        'puntaje_usuarios': 7.6
    },
    {
        'id': 22,
        'nombre': 'Pokémon Shield',
        'genero': 'RPG',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': 80,
        'puntaje_usuarios': 7.6
    },
    {
        'id': 23,
        'nombre': 'Pokémon Legends: Arceus',
        'genero': 'RPG de acción',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 24,
        'nombre': 'Crash Bandicoot N. Sane Trilogy',
        'genero': 'Plataformas',
        'plataforma': 'PlayStation 4, Xbox One, Nintendo Switch, PC',
        'desarrolladora': 'Vicarious Visions',
        'puntaje_metacritic': 80,
        'puntaje_usuarios': 8.0
    },
    {
        'id': 25,
        'nombre': 'Crash Bandicoot 4: It’s About Time',
        'genero': 'Plataformas',
        'plataforma': 'PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Nintendo Switch, PC',
        'desarrolladora': 'Toys for Bob',
        'puntaje_metacritic': 85,
        'puntaje_usuarios': 8.3
    },
    {
        'id': 26,
        'nombre': 'Assassin\'s Creed Odyssey',
        'genero': 'Acción-Aventura, RPG',
        'plataforma': 'PlayStation 4, Xbox One, PC, Nintendo Switch (cloud)',
        'desarrolladora': 'Ubisoft Quebec',
        'puntaje_metacritic': 86,
        'puntaje_usuarios': 7.6
    },
    {
        'id': 27,
        'nombre': 'Assassin\'s Creed Valhalla',
        'genero': 'Acción-Aventura, RPG',
        'plataforma': 'PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, PC, Google Stadia',
        'desarrolladora': 'Ubisoft Montreal',
        'puntaje_metacritic': 82,
        'puntaje_usuarios': 7.5
    },
    {
        'id': 28,
        'nombre': 'The Elder Scrolls V: Skyrim',
        'genero': 'RPG',
        'plataforma': 'PlayStation 3, PlayStation 4, Xbox 360, Xbox One, PC, Nintendo Switch',
        'desarrolladora': 'Bethesda Game Studios',
        'puntaje_metacritic': 94,
        'puntaje_usuarios': 8.0
    },
    {
        'id': 29,
        'nombre': 'Genshin Impact',
        'genero': 'Acción-RPG, Mundo abierto',
        'plataforma': 'PlayStation 4, PlayStation 5, PC, iOS, Android',
        'desarrolladora': 'miHoYo',
        'puntaje_metacritic': 81,
        'puntaje_usuarios': 8.0
    },
    {
        'id': 30,
        'nombre': 'Final Fantasy VII Remake',
        'genero': 'RPG de acción',
        'plataforma': 'PlayStation 4',
        'desarrolladora': 'Square Enix',
        'puntaje_metacritic': 87,
        'puntaje_usuarios': 8.4
    },{
        'id': 31,
        'nombre': 'Tomb Raider',
        'genero': 'Acción-aventura',
        'plataforma': 'Multiplataforma',
        'desarrolladora': 'Crystal Dynamics',
        'puntaje_metacritic': 86,
        'puntaje_usuarios': 8.3
    },
    {
        'id': 32,
        'nombre': 'Rise of the Tomb Raider',
        'genero': 'Acción-aventura',
        'plataforma': 'Multiplataforma',
        'desarrolladora': 'Crystal Dynamics',
        'puntaje_metacritic': 88,
        'puntaje_usuarios': 8.1
    },
    {
        'id': 33,
        'nombre': 'Shadow of the Tomb Raider',
        'genero': 'Acción-aventura',
        'plataforma': 'Multiplataforma',
        'desarrolladora': 'Eidos-Montréal',
        'puntaje_metacritic': 77,
        'puntaje_usuarios': 7.5
    },
    {
        'id': 34,
        'nombre': 'Tomb Raider (2013)',
        'genero': 'Acción-aventura',
        'plataforma': 'Multiplataforma',
        'desarrolladora': 'Crystal Dynamics',
        'puntaje_metacritic': 86,
        'puntaje_usuarios': 8.3
    },
    {
        'id': 35,
        'nombre': 'Pokémon Rojo y Azul',
        'genero': 'RPG',
        'plataforma': 'Game Boy',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 36,
        'nombre': 'Pokémon Oro y Plata',
        'genero': 'RPG',
        'plataforma': 'Game Boy Color',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 37,
        'nombre': 'Pokémon Rubí y Zafiro',
        'genero': 'RPG',
        'plataforma': 'Game Boy Advance',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 38,
        'nombre': 'Pokémon Esmeralda',
        'genero': 'RPG',
        'plataforma': 'Game Boy Advance',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 39,
        'nombre': 'Pokémon Diamante y Perla',
        'genero': 'RPG',
        'plataforma': 'Nintendo DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 40,
        'nombre': 'Pokémon Platino',
        'genero': 'RPG',
        'plataforma': 'Nintendo DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 41,
        'nombre': 'Pokémon Blanco y Negro',
        'genero': 'RPG',
        'plataforma': 'Nintendo DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 42,
        'nombre': 'Pokémon Blanco y Negro 2',
        'genero': 'RPG',
        'plataforma': 'Nintendo DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 43,
        'nombre': 'Pokémon X e Y',
        'genero': 'RPG',
        'plataforma': 'Nintendo 3DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 44,
        'nombre': 'Pokémon Rubí Omega y Zafiro Alfa',
        'genero': 'RPG',
        'plataforma': 'Nintendo 3DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 45,
        'nombre': 'Pokémon Sol y Luna',
        'genero': 'RPG',
        'plataforma': 'Nintendo 3DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 46,
        'nombre': 'Pokémon Ultrasol y Ultraluna',
        'genero': 'RPG',
        'plataforma': 'Nintendo 3DS',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 47,
        'nombre': 'Pokémon Espada y Escudo',
        'genero': 'RPG',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': 80,
        'puntaje_usuarios': 5.6
    },
    {
        'id': 48,
        'nombre': 'Pokémon Brillante Diamante y Reluciente Perla',
        'genero': 'RPG',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 49,
        'nombre': 'Pokémon Leyendas: Arceus',
        'genero': 'RPG de acción',
        'plataforma': 'Nintendo Switch',
        'desarrolladora': 'Game Freak',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },{
        'id': 51,
        'nombre': 'Sonic the Hedgehog',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Sonic Team',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 52,
        'nombre': 'Sonic the Hedgehog 2',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Sonic Team',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 53,
        'nombre': 'Sonic the Hedgehog 3',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Sonic Team',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 54,
        'nombre': 'Super Mario Bros.',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Nintendo',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 55,
        'nombre': 'Super Mario Bros. 2',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Nintendo',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 56,
        'nombre': 'Super Mario Bros. 3',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Nintendo',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 57,
        'nombre': 'Crash Bandicoot',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Naughty Dog',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 58,
        'nombre': 'Crash Bandicoot 2: Cortex Strikes Back',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Naughty Dog',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 59,
        'nombre': 'Crash Bandicoot: Warped',
        'genero': 'Plataformas',
        'plataforma': 'Varios',
        'desarrolladora': 'Naughty Dog',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 60,
        'nombre': 'Halo: Combat Evolved',
        'genero': 'Shooter en primera persona',
        'plataforma': 'Xbox, Microsoft Windows, Mac OS X',
        'desarrolladora': 'Bungie',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 61,
        'nombre': 'Halo 2',
        'genero': 'Shooter en primera persona',
        'plataforma': 'Xbox, Microsoft Windows',
        'desarrolladora': 'Bungie',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 62,
        'nombre': 'Halo 3',
        'genero': 'Shooter en primera persona',
        'plataforma': 'Xbox 360, Xbox One, Microsoft Windows',
        'desarrolladora': 'Bungie',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 63,
        'nombre': 'Monster Hunter',
        'genero': 'Acción-RPG',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 64,
        'nombre': 'Monster Hunter Freedom',
        'genero': 'Acción-RPG',
        'plataforma': 'PlayStation Portable',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 65,
        'nombre': 'Monster Hunter Freedom 2',
        'genero': 'Acción-RPG',
        'plataforma': 'PlayStation Portable',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 66,
        'nombre': 'Monster Hunter Tri',
        'genero': 'Acción-RPG',
        'plataforma': 'Wii',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 67,
        'nombre': 'Monster Hunter: World',
        'genero': 'Acción-RPG',
        'plataforma': 'PlayStation 4, Xbox One, Microsoft Windows',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 68,
        'nombre': 'Monster Hunter Rise',
        'genero': 'Acción-RPG',
        'plataforma': 'Nintendo Switch, Microsoft Windows',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },{
        'id': 69,
        'nombre': 'Forza Motorsport',
        'genero': 'Carreras',
        'plataforma': 'Xbox',
        'desarrolladora': 'Turn 10 Studios',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 70,
        'nombre': 'Forza Motorsport 2',
        'genero': 'Carreras',
        'plataforma': 'Xbox 360',
        'desarrolladora': 'Turn 10 Studios',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 71,
        'nombre': 'Forza Motorsport 3',
        'genero': 'Carreras',
        'plataforma': 'Xbox 360',
        'desarrolladora': 'Turn 10 Studios',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 72,
        'nombre': 'Forza Motorsport 4',
        'genero': 'Carreras',
        'plataforma': 'Xbox 360',
        'desarrolladora': 'Turn 10 Studios',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 73,
        'nombre': 'Forza Horizon',
        'genero': 'Carreras de mundo abierto',
        'plataforma': 'Xbox 360',
        'desarrolladora': 'Playground Games',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 74,
        'nombre': 'Forza Horizon 2',
        'genero': 'Carreras de mundo abierto',
        'plataforma': 'Xbox 360, Xbox One',
        'desarrolladora': 'Playground Games',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 75,
        'nombre': 'Forza Horizon 3',
        'genero': 'Carreras de mundo abierto',
        'plataforma': 'Xbox One, Microsoft Windows',
        'desarrolladora': 'Playground Games',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 76,
        'nombre': 'Forza Horizon 4',
        'genero': 'Carreras de mundo abierto',
        'plataforma': 'Xbox One, Microsoft Windows',
        'desarrolladora': 'Playground Games',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 77,
        'nombre': 'Borderlands',
        'genero': 'Acción-RPG, Shooter en primera persona',
        'plataforma': 'PlayStation 3, Xbox 360, Microsoft Windows',
        'desarrolladora': 'Gearbox Software',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 78,
        'nombre': 'Borderlands 2',
        'genero': 'Acción-RPG, Shooter en primera persona',
        'plataforma': 'PlayStation 3, Xbox 360, Microsoft Windows',
        'desarrolladora': 'Gearbox Software',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 79,
        'nombre': 'Borderlands: The Pre-Sequel!',
        'genero': 'Acción-RPG, Shooter en primera persona',
        'plataforma': 'PlayStation 3, Xbox 360, Microsoft Windows',
        'desarrolladora': '2K Australia',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 80,
        'nombre': 'Borderlands 3',
        'genero': 'Acción-RPG, Shooter en primera persona',
        'plataforma': 'PlayStation 4, Xbox One, Microsoft Windows',
        'desarrolladora': 'Gearbox Software',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 81,
        'nombre': 'Mega Man',
        'genero': 'Plataformas, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 82,
        'nombre': 'Mega Man 2',
        'genero': 'Plataformas, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 83,
        'nombre': 'Mega Man 3',
        'genero': 'Plataformas, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 84,
        'nombre': 'Mega Man X',
        'genero': 'Plataformas, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 85,
        'nombre': 'Mega Man X2',
        'genero': 'Plataformas, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 86,
        'nombre': 'Mega Man X3',
        'genero': 'Plataformas, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Capcom',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },{
        'id': 88,
        'nombre': 'LEGO Batman: The Videogame',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 89,
        'nombre': 'LEGO Indiana Jones: The Original Adventures',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 90,
        'nombre': 'LEGO Harry Potter: Years 1–4',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 91,
        'nombre': 'LEGO Star Wars II: The Original Trilogy',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 92,
        'nombre': 'LEGO Pirates of the Caribbean: The Video Game',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 93,
        'nombre': 'LEGO Marvel Super Heroes',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 94,
        'nombre': 'LEGO The Lord of the Rings',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 95,
        'nombre': 'LEGO Jurassic World',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 96,
        'nombre': 'LEGO DC Super-Villains',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    },
    {
        'id': 97,
        'nombre': 'LEGO Movie Videogame',
        'genero': 'Aventura, Acción',
        'plataforma': 'Varios',
        'desarrolladora': 'Traveller\'s Tales',
        'puntaje_metacritic': None,
        'puntaje_usuarios': None
    }

 
]


@app.route('/')
def index():
    return render_template('index.html', juegos=videojuegos)

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        new_game = {
            'id': len(videojuegos) + 1,
            'nombre': request.form['nombre'],
            'genero': request.form['genero'],
            'plataforma': request.form['plataforma'],
            'desarrolladora': request.form['desarrolladora'],
            'puntaje_metacritic': request.form['puntaje_metacritic'],
            'puntaje_usuarios': request.form['puntaje_usuarios']
        }
        videojuegos.append(new_game)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    juego = next((juego for juego in videojuegos if juego['id'] == id), None)
    if request.method == 'POST':
        if juego:
            juego['nombre'] = request.form['nombre']
            juego['genero'] = request.form['genero']
            juego['plataforma'] = request.form['plataforma']
            juego['desarrolladora'] = request.form['desarrolladora']
            juego['puntaje_metacritic'] = request.form['puntaje_metacritic']
            juego['puntaje_usuarios'] = request.form['puntaje_usuarios']
        return redirect(url_for('index'))
    return render_template('edit.html', juego=juego)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_game(id):
    global videojuegos
    videojuegos = [juego for juego in videojuegos if juego['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
