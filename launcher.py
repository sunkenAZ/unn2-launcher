import subprocess as Subprocess;
import json as JSON;
import math as Math;
import os as OS;

OS.system("TITLE lsl for unn2 v4");

ef_to_launch: str = 'exe';

cmds: dict = {
    'INFO  (version id)': 'Prints info about the selected version.',
    'START (version id)': 'Opens the selected version.',
    'SETTINGS': 'Modify launcher settings.',
    'QUIT': 'Exits this program.'
};

s_cmds: dict = {
    'BACK': ['Go back to main launcher.', '--'],
    'COLOR': ['Modify color. Identical to CMD COLOR.', '07']
};

in_settings: bool = False;

while True:
    cwd: str = OS.getcwd();
    games: list = OS.listdir(f'{cwd}\\games\\');
    
    OS.system(f'mode con: cols=64 lines={6 + len(games) + len(cmds)}');
    OS.system('CLS');
    print(f'lethal\'s simple unn2 launcher {"<2025/03/07 - version 4>":>34}');
    print('~' * 64);
    
    if in_settings:
        for cmd in s_cmds:
            print(f'{cmd:18s} : {s_cmds[cmd][1]} : {s_cmds[cmd][0]}');
    else:
        for cmd in cmds:
            print(f'{cmd:18s} : {cmds[cmd]}');
        
        print('~' * 64);
    
        g_id: int = 0;
        for game_f in games:
            game_name_length: int = len(game_f);
        
            if game_f[game_name_length - len(ef_to_launch) - 1:game_name_length] == f'.{ef_to_launch}':
                print(f'[{g_id}] > {game_f[0:game_name_length - len(ef_to_launch) - 1]}');
                g_id += 1;
        
    print("~" * 64);

    m_input: str = input('DO? ').split(' ');
    OS.system('CLS');

    # :: INFO ::
    if(m_input[0].upper() == 'INFO'):
        if int(m_input[1]) > len(games) or int(m_input[1]) < 0:
            print(f'Provided g_id out of range (-1 < {int(m_input[1])} < {len(games)}). Clamping to last valid m_id. ({min(len(games)-1, max(int(m_input[1]), 0))})\n');
            m_input[1] = str(min(len(games)-1, max(int(m_input[1]), 0)));

        with open(f'{cwd}\\infos\\{games[int(m_input[1])][0:len(games[int(m_input[1])])-len(ef_to_launch)-1]}.json', 'r') as ver_info:
            ver_info_data: dict = JSON.loads(ver_info.read());
            print(f'{ver_info_data['name']} by {ver_info_data['developer']}\n{ver_info_data['description']}\n');
            print(f'[save file: {ver_info_data['save_location']} -> (cloned to){ver_info_data['save_identifier']}]\n');
            OS.system('PAUSE');
    
    # :: START ::
    if(m_input[0].upper() == 'START'):
        with open(f'{cwd}\\infos\\{games[int(m_input[1])][0:len(games[int(m_input[1])])-len(ef_to_launch)-1]}.json', 'r') as game_info:
            game_info_data: dict = JSON.loads(game_info.read());
            print(f'Opening {games[int(m_input[1])]}\n& spoofing save -> {game_info_data['save_identifier']}');
            
            save_path: str = game_info_data['save_location'];
            if save_path.split('\\')[0] == "%%mmf":
                save_path = f'{OS.getenv('APPDATA')}\\MMFApplications\\{save_path.split('\\')[1]}';
            
            with open(f'{cwd}\\save_clones\\{game_info_data['save_identifier']}', 'r') as sv_f:
                with open(save_path, 'w') as w_f:
                    w_f.write(sv_f.read());
        
        Subprocess.call([f'{cwd}\\games\\{games[int(m_input[1])]}']);
        
        with open(f'{cwd}\\infos\\{games[int(m_input[1])][0:len(games[int(m_input[1])])-len(ef_to_launch)-1]}.json', 'r') as game_info:
            game_info_data: dict = JSON.loads(game_info.read());
            print(f'Saving spoofed save from {game_info_data['save_location']} as {game_info_data['save_identifier']}');
            
            save_path: str = game_info_data['save_location'];
            if save_path.split('\\')[0] == "%%mmf":
                save_path = f'{OS.getenv('APPDATA')}\\MMFApplications\\{save_path.split('\\')[1]}';
                
            with open(save_path, 'r') as sv_f:
                with open(f'{cwd}\\save_clones\\{game_info_data['save_identifier']}', 'w') as w_f:
                    w_f.write(sv_f.read());
    
    # :: BACK ::
    if(m_input[0].upper() == 'BACK'):
        in_settings = False;
    
    # :: SETTINGS ::
    if(m_input[0].upper() == 'SETTINGS'):
        in_settings = True;
    
    # :: COLOR ::
    if(m_input[0].upper() == 'COLOR'):
        OS.system(f'COLOR {m_input[1]}');
        s_cmds['COLOR'][1] = m_input[1];
        OS.system('CLS');
    
    # :: QUIT ::
    if(m_input[0].upper() == 'QUIT'):
        quit();
    
