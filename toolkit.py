import dns.name
import dns.resolver
import socket
import requests
from nested_lookup import nested_lookup
from Naked.toolshed.shell import execute_js, muterun_js
import server
from rich.console import Console

def amplified(h):
    console = Console()
    myResolver = dns.resolver.Resolver() #La création d'un résolveur personnalisé permet d'utiliser l'adresse de notre cible comme résolveur
    myResolver.timeout = 5
    myResolver.lifetime = 5
    myResolver.nameservers = h
    try:
        answer = myResolver.query('version.bind','TXT','CH') #Le troisième paramètre "CH" permet d'utiliser la classe CHAOS
    except:
        console.print("\nImpossible de récupérer la version du serveur",style='bold red')
    else:
        print("Réponse du serveur :")
        for rdata in answer:
            print(rdata.to_text())

def dns_zone(h):
    console = Console()
    try:
        z = dns.zone.from_xfr(dns.query.xfr('nsztm2.digi.ninja',h))
    except:
        console.print("\nEchec du tranfert : Serveur non vulnérable au transfert de zone\n",style='bold red')
    else:
        print("\nSuccès du transfert : Serveur vulnerable au transfert de zone\n")
        names = z.nodes.keys()
        for n in names:
            print(z[n].to_text(n))

def main(h):
    global s
    console = Console()
    s = dict()
    n = dns.name.from_text(h)
    try:
        while True:
            try:
                #On envoie une requête de type NS :
                answer = dns.resolver.query(n,'NS')
            except dns.resolver.NoAnswer:
                #On a pas trouvé d'enregistrement, on ignore l'exception et on continue
                console.print("\nAucun enregistrement NS trouvé pour "+n.to_text()+", tentative avec le parent.", style="bold yellow")
            else:
                #Aucune exception levée, on a trouvé un enregistrement NS
                console.print("\nEnregistrement NS trouvé pour le domaine "+n.to_text(),style="bold green")
                for rdata in answer:
                    s = socket.gethostbyname(rdata.to_text())
                    r = requests.get("http://ip-api.com/json/{}".format(h))
                    a = r.json()
                    #print(a)
                    #print(type(a))
                    lat = nested_lookup('lat', a)
                    lon = nested_lookup('lon',a)
                    console.print(rdata.to_text()+f'     {s}      {lat}:{lon}'.format(s,lat,lon))
                break;
            #Si on arrive ici, c'est qu'on a pas trouvé, on réessaie avec le parent:
            n = n.parent()
    except dns.name.NoParent:
        #Cette exception est levée si le domaine n'a plus de parent, on a atteint la racine du DNS
        console.print("Aucun serveur NS trouvé",style='bold red')
    amplified(h)
    dns_zone(h)
    #server.run()

if __name__ == '__main__':
    main()
