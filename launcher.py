import os as OS;
import json as JSON;
import subprocess as Subprocess;

OS.system('mode con: cols=64 lines=17');
OS.system("TITLE lethal's totally radical unn2 launcher");

ef_to_launch:str = ".exe";

cmds:dict = {
    "INFO  (version id)": "Prints info about the selected version.",
    "START (version id)": "Opens the selected version.",
    "QUIT": "Exits this program."
};

while True:
    OS.system("CLS");
    print("lethal's totally radical unn2 version launcher 3.0");
    print("~" * 64);
    
    for cmd in cmds:
        print(f'{cmd:18s} : {cmds[cmd]}');

    print("~" * 64);
    
    cwd:str = OS.getcwd();
    mods:list = OS.listdir(f'{cwd}\\mods\\');
    
    m_id:int = 0;
    for mod_f in mods:
        mod_f_length:int = len(mod_f);
        
        if mod_f[mod_f_length-4:mod_f_length] == ef_to_launch:
            print(f'[{m_id}] {mod_f[0:mod_f_length-4]}');
            m_id += 1;
        
    print("~" * 64);

    m_input:str = input('DO? ').split(' ');
    OS.system('CLS');

    if(m_input[0].upper() == "INFO"):
        if(int(m_input[1])*2+1 > len(mods)):
            print(f'Provided m_id too high ({int(m_input[1])*2+1} < {len(mods)}). Lowering to last valid m_id.\n');
            m_input[1] = str((len(mods) - 1) / 2);

        with open(f'{cwd}\\mods\\{mods[int(m_input[1])*2+1]}', 'r') as mod_info:
            mod_info_data: dict = JSON.loads(mod_info.read());
            print(f'{mod_info_data['name']} by {mod_info_data['developer']}\n{mod_info_data['description']}\n');
            print(f'save: {mod_info_data['save_location']}->{mod_info_data['save_identifier']}\n');
            OS.system('PAUSE');
    
    if(m_input[0].upper() == "START"):
        with open(f'{cwd}\\mods\\{mods[int(m_input[1])*2+1]}', 'r') as mod_info:
            mod_info_data: dict = JSON.loads(mod_info.read());
            print(f'Opening {mods[int(m_input[1])*2]} and spoofing save for {mod_info_data['save_identifier']}');
            
            save_path: str = mod_info_data['save_location'];
            if save_path.split('\\')[0] == "%%mmf":
                save_path = f'{OS.getenv('APPDATA')}\\MMFApplications\\{save_path.split('\\')[1]}';
            
            with open(f'{cwd}\\svs\\{mod_info_data['save_identifier']}', 'r') as sv_f:
                with open(save_path, 'w') as w_f:
                    w_f.write(sv_f.read());
            
        Subprocess.call([f'{cwd}\\mods\\{mods[int(m_input[1])*2]}']);
        
        with open(f'{cwd}\\mods\\{mods[int(m_input[1])*2+1]}', 'r') as mod_info:
            mod_info_data: dict = JSON.loads(mod_info.read());
            print(f'Saving spoofed save from {mod_info_data['save_location']} as {mod_info_data['save_identifier']}');
            
            save_path: str = mod_info_data['save_location'];
            if save_path.split('\\')[0] == "%%mmf":
                save_path = f'{OS.getenv('APPDATA')}\\MMFApplications\\{save_path.split('\\')[1]}';
                
            with open(save_path, 'r') as sv_f:
                with open(f'{cwd}\\svs\\{mod_info_data['save_identifier']}', 'w') as w_f:
                    w_f.write(sv_f.read());
    
    if(m_input[0].upper() == "QUIT"):
        quit();
    
