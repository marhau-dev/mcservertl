import subprocess
import os
pat = os.path.dirname(os.path.realpath(__file__))
ld = "servers"
##check avalible of servers folder if not. create it.
try:
    folder_path = os.path.join(pat,ld )
    os.makedirs(folder_path)
except:
     nothing = "nothing"

#animation of downloading
def animate(text):
    import sys
    import time
    spinner_chars = "|/-\\|/-\\ "
    for char in spinner_chars:
        sys.stdout.write(f"\r{text} {char}")
        sys.stdout.flush()
        time.sleep(0.6)

#part for create server.properties
def setup(path_of_server, name,players, ip, port, ram , crossplay, chunkgen, craked, hardcore, difficulty, gamemode,core,versionn ):
    bat = "1"
    elua = """

    eula=TRUE
    """
    import shutil
    #convert all info to str value type.
    versionn = str(versionn)
    players = str(players)
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

# protection from empty values
    if players == null or players == " ":
         players = "20"
    if name == null or name == " ":
         name = "Server of Minecaft"
    if ram == null or ram == " ":
         ram = "8"
    if chunkgen == null or chunkgen == "":
         chunkgen = "10"
    if gamemode == null or gamemode == " ":
         gamemode = "survival"
    if difficulty == null or difficulty == " ":
         difficulty = "easy"
    if hardcore == null or hardcore == " ":
         hardcore = "no"
    if crossplay == null or crossplay == " ":
         crossplay = "no"
    if craked == null or craked == " ":
         craked = "yes"
    if ip == null or ip == " ":
         ip = "localhost"


    if craked == "yes":
        craked = "false"
    else:
        craked = "true"
    if hardcore == "yes":
        hardcore = "true"
    else:
        hardcore = "false"
#temple of server.properties 
    temple = f"""    
#Minecraft server properties
allow-flight=false
allow-nether=true
broadcast-console-to-ops=true
broadcast-rcon-to-ops=true
difficulty={difficulty}
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
max-players={players}
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
    #some version of forge have different start file name. And we make diferrent .bat file for this version of forge
    if core == "forge":
        dfn = ["1.1","1.2.3","1.2.4","1.2.5","1.3.2","1.4.0","1.4.1","1.4.2","1.4.3","1.4.4","1.4.5","1.4.6","1.4.7","1.5","1.5.1","1.5.2","1.6.1","1.6.2","1.6.3","1.6.4","1.7.2","1.7.10","1.8","1.8.8","1.8.9","1.9","1.9.4","1.10","1.10.2","1.11","1.11.2","1.12","1.12.1","1.12.2","1.15","1.15.1","1.15.2","1.16.1","1.16.2","1.16.3","1.16.4","1.16.5"]
        if versionn in dfn:
            bat = f"""
java -Xmx{ram}G -jar minecraft_server.{versions}.jar%*
pause
""" 
 
        elif versionn != dfn:  
            bat = f"""
java -Xmx{ram}G -jar server.jar%*
pause
"""   
    elif core == "fabric":
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


#part of download core
def download(core,version):
    import requests
    import os
    rq = requests
    core = str(core)
    version = str(version)
    corename = core
    #api link to download core
    urls = f"https://mcutils.com/api/server-jars/{core}/{version}/download"
    dw = rq.get(urls)
    if dw.status_code == 200:
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, "servers")
        os.makedirs(path, exist_ok=True)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        core = f"{core}{version}.jar"
        core = str(core)
        #create folder
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
        #download core to created folder
        with open(os.path.join(path, f"server.jar"), 'wb') as f:
            f.write(dw.content)
            #fabric and forge needs an instalation before starting 
            if "fabric" in core or "Fabric" in core:
                print("""
                 PLS wait Fabric need to be extracted""")
                subprocess.run(["java", "-jar", "server.jar", "server", "-downloadMinecraft", f"-mcversion={version}"], cwd=path)
            elif "forge" in core or "Forge" in core:   

                print("""
                 PLS wait Forge need to be extracted""")
                subprocess.run(["java", "-jar", "server.jar", "--installServer"], cwd=path) 
           #return result of complete downloader file
            return path
    #if information was wrong we return info
    elif dw.status_code == 404:
            return f"false maybe your name of core or version was wrong.  {dw.status_code},{urls}"

print(""" server creation tool by marhau.
 
 If you need help write help in console
      """) 
while True:
    #take your answer
    answ = input("You: ")
    if answ == "help" or answ == "Help":
                print(""" 
            create --- create server fabric, forge, paper, spigot, purpur
            exit --- close app
        """)
    elif answ == "create" or answ == "Create":
                
                
                print("""Pls write what core and version do you want.
                            cores:
                Paper -- lowest version is 1.8.8 | type plugins
                Spigot -- lowest version is 1.4.6 | type  plugins 
                Purpur -- lowest version is 1.14.1 | type mods or plugins
                Forge -- lowest version is 1.5.2 | type mods
                Fabric -- lowest version is 1.14 | type mods


                
                """)
                # Collect info for download server core 
                cores = input("Core : ")
                versions = input("Version: ")
                os.system('cls')
                
                animate("Pls wait we downloading right now")
                pathserv = download(cores,versions)
                print(pathserv)
                os.system('cls')
                print("We need setup server pls fill this forms")

                servername = input("Your server name: ")
                os.system('cls')
                print("Players limit, default is 20")

                playerscount = input("Players: ")
               #check your local ip for server
                try:
                    import socket
                    name = socket.gethostname()
                    ips = socket.gethostbyname(name)
                except:
                    
                     print("app can't take your ip check your internet connection")
                
                print("type your server port ")
                ports = input("port: ")
                os.system('cls')
                print("type how many ram did you want give to a server")
                ram = input("ram in GB: ")
                os.system('cls')
                if cores == "forge" or cores == "Forge" or cores == "fabric" or cores == "Fabric":
                     crossplay = "no"
                else:
                     #crossplay means download Geyser or not (Geyser allow players from bedrock connect to java)
                     print("Did you want crossplay on your server ")
                     crossplay = input("yes/no: ")
                     os.system('cls')
                print("Chunk view default is 10")
                chnk = input("Chunks: ")
                os.system('cls')
                print("License ?")
                lcs = input("yes/no: ")
                os.system('cls')
                print("Hardcore ?")
                hd = input("yes/no: ")
                os.system('cls')
                print("Dificalty:  peaceful easy normal hard")
                df = input("Fificalty:  ")
                os.system('cls')
                print("Gamemode:  survival, creative, spectator")
                gm = input("Gamemode: ")
                os.system('cls')




                #after collecting info we use function to create server.properties
                setup(pathserv,servername,playerscount,ips,ports,ram,crossplay,chnk,lcs,hd,df,gm,cores,versions)
                print("""
                      config file was saved. 
                  run start.bat for start server!!
                        write exit to close app
                      
                      """)
    elif answ == "exit" or answ == "Exit":
         break