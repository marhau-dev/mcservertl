import subprocess
import os

pat = os.path.dirname(os.path.realpath(__file__))
ld = "servers"
try:
    folder_path = os.path.join(pat,ld )
    os.makedirs(folder_path)
except:
     nothing = "nothing"
print(pat)
def setup(path_of_server, name, ip, port, ram , crossplay, chunkgen, craked, hardcore, difficulty, gamemode,core ):
    elua = """

    eula=TRUE
    """
    import shutil
    core = str(core)
    path = str(path_of_server)
    port = str(port)
    ip = str(ip)
    name = str(name)
    ram = str(ram)
    crossplay = str(crossplay)
    chunkgen = str(chunkgen)
    craked = str(craked)
    hardcore = str(hardcore)
    difficulty = str(difficulty)
    gamemode = str(gamemode)


    if craked == "yes":
        craked = "false"
    else:
        craked = "true"
    if hardcore == "yes":
        hardcore = "true"
    else:
        hardcore = "false"

    temple = f"""    
#Minecraft server properties
#Thu Apr 25 20:28:37 CDT 2024
allow-flight=false
allow-nether=true
broadcast-console-to-ops=true
broadcast-rcon-to-ops=true
difficulty=normal
enable-command-block=false
enable-jmx-monitoring=false
enable-query=false
enable-rcon=false
enable-status=true
enforce-secure-profile=true
enforce-whitelist=false
entity-broadcast-range-percentage=100
force-gamemode=false
function-permission-level=2
gamemode={gamemode}
generate-structures=true
generator-settings=
hardcore={hardcore}
hide-online-players=false
initial-disabled-packs=
initial-enabled-packs=vanilla
level-name=world
level-seed=
level-type=minecraft\:normal
max-chained-neighbor-updates=1000000
max-players=20
max-tick-time=600000
max-world-size=29999984
motd={name}
network-compression-threshold=256
online-mode={craked}
op-permission-level=4
player-idle-timeout=0
prevent-proxy-connections=false
pvp=true
query.port=25565
rate-limit=0
rcon.password=
rcon.port=25575
require-resource-pack=false
resource-pack=
resource-pack-prompt=
resource-pack-sha1=
server-ip={ip}
server-port={port}
simulation-distance=10
spawn-animals=true
spawn-monsters=true
spawn-npcs=true
spawn-protection={chunkgen}
sync-chunk-writes=true
text-filtering-config=
use-native-transport=true
view-distance={chunkgen}
white-list=false

"""
   
    bat = f"""
java -Xmx{ram}G -jar server.jar%*
pause
"""
    try:
        pathds = path + "\\server.properties"
        file = open(pathds, 'w')
        file.write(temple)
        pathds = path + "\\start.bat"
        file = open(pathds, 'w')
        file.write(bat)
        pathds = path + "\\eula.txt"
        file = open(pathds, 'w')
        file.write(elua)
        
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    if crossplay == "yes":    
        import requests
        rq = requests
        urls = f"https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot"
        dw = requests.get(urls)
        if dw.status_code == 200:
            import os
            path =  path_of_server 
            os.makedirs(path, exist_ok=True)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            folder_name = "plugins"
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path)
            print(path)
            path = path + "\\plugins"
            with open(os.path.join(path, f"geyser.jar"), 'wb') as f:
                f.write(dw.content)

servp = "nothing"



def download(core,version):
    import requests
    import os
    rq = requests
    core = str(core)
    version = str(version)
    corename = core
    urls = f"https://mcutils.com/api/server-jars/{core}/{version}/download"
    dw = rq.get(urls)
    if dw.status_code == 200:
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, "servers")
        os.makedirs(path, exist_ok=True)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        core = f"{core}{version}.jar"
        core = str(core)

        base_name = f"server_{corename}_{version}"
        folder_name = base_name
        count = 0
        folder_name = base_name
        while os.path.exists(os.path.join(path, folder_name)):
            count += 1
            folder_name = f"{base_name}_{count}"
        
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path)
        
        path = folder_path

        with open(os.path.join(path, f"server.jar"), 'wb') as f:
            f.write(dw.content)
            if "fabric" in core or "Fabric" in core:
                print("PLS wait fabric need to be extracted")
                subprocess.run(["java", "-jar", "server.jar", "server", "-downloadMinecraft", f"-mcversion={version}"], cwd=path)
            elif "forge" in core or "Forge" in core:   
                print("PLS wait fabric need to be extracted")
                subprocess.run(["java", "-jar", "server.jar", "--installServer"], cwd=path) 
            return path
    elif dw.status_code == 404:
            return f"false maybe your name of core or version was wrong.  {dw.status_code},{urls}"

print(""" server creation tool by marhau
      if you need help send me help
      """) 
while True:
    
    answ = input("You: ")
    if answ == "help" or answ == "Help":
                print(""" 
            create --- create server fabric, forge, paper, spigot, purpur
            exit --- close app
        """)
    elif answ == "create" or answ == "Create":
                
                
                print("""Good pls send waht core do you want
                            cores:
                Paper -- lowest version is 1.8.8 | type plugins
                Spigot -- lowest version is 1.4.6 | type  plugins 
                Purpur -- lowest version is 1.14.1 | type mods or plugins
                Forge -- lowest version is 1.5.2 | type mods
                Fabric -- lowest version is 1.14 | type mods


                
                """)
                cores = input("core : ")
                versions = input("version:")
                os.system('cls')
                print("pls wait we downloading right now")
                pathserv = download(cores,versions)
                print(pathserv)
                os.system('cls')
                print("we need setup server pls fill this forms")

                servername = input("your server name: ")
                import socket
                name = socket.gethostname()
                ips = socket.gethostbyname(name)
                print("type your server port ")
                ports = input("port: ")
                os.system('cls')
                print("type how many ram did you want give to a server")
                ram = input("ram in GB: ")
                os.system('cls')
                if cores == "forge" or cores == "Forge" or cores == "fabric" or cores == "Fabric":
                     crossplay = "no"
                else:
                     print("did you want on crossplay on your server ")
                     crossplay = input("yes/no: ")
                     os.system('cls')
                print("chunk view default is 10")
                chnk = input("chunks: ")
                os.system('cls')
                print("license ?")
                lcs = input("yes/no: ")
                os.system('cls')
                print("hardcore ?")
                hd = input("yes/no: ")
                os.system('cls')
                print("dificalty:  peaceful easy normal hard")
                df = input("dificalty: ")
                os.system('cls')
                print("gamemode:  survival, creative, spectator")
                gm = input("gamemode: ")
                os.system('cls')
                
                setup(pathserv,servername,ips,ports,ram,crossplay,chnk,lcs,hd,df,gm,cores)
                print("""
                      config file was saved. 
                  run start.bat for start server!!
                      
                      
                      """)
    elif answ == "exit" or answ == "Exit":
         break