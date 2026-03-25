from random import randint
import pyxel as p,pyxel




class Jeu:
    def __init__(self) :
        self.pause_time=0
        self.rng_factor=900 #plus c'est bas  plus il y a de mobs, on peut le baisser a chaque roun pour rajouter des mobs éventuellement
        self.taille_map=1
        p.init(250*self.taille_map,250*self.taille_map)
        self.konami_code = [pyxel.KEY_UP, pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_DOWN,pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_RIGHT,pyxel.KEY_B, pyxel.KEY_A]
        self.code=[]
        p.load("images.pyxres")
        self.fin = 0
        self.ind = 0
        self.manche = 1
        self.accumul = 0
        self.taille_shop=5
        self.liste_powerups=["   ATK","    HP","   tir"," sangsue","   Spd","  luck","   def","  crit","   1UP"," SPD proj"]
        self.liste_shop=[self.liste_powerups[randint(0,len(self.liste_powerups)-1)]for _ in range(self.taille_shop) ]

        self.is_running = 200 #1= manche classique, 2=pause, 3=manche boss
        self.game_status=0
        p.run(self.update,self.draw)



    def frames_checker(self) :

        if (seed>0 and seed<9) :
            return 1
        if (seed>9 and seed<14) :
            return 2
        if (seed>14 and seed<18) :
            return 3
        else:
            return -1



    def creation_monstre(self,type) :
        if joueur1.PV > 0 and self.is_running!=2:

            for pos in spawnlist.spawnlist:
                if type == 1:
                    liste_monstres.liste_monstres1.append(Monstre(1,pos.x,pos.y))

                if type == 2:
                    liste_monstres.liste_monstres2.append(Monstre(2,pos.x,pos.y))

                if type == 3:
                    liste_monstres.liste_monstres3.append(Monstre(3,pos.x,pos.y))

                if type == 4:
                    taille = len(liste_monstres.liste_monstres4)
                    if taille < 1:
                        liste_monstres.liste_monstres4.append(Monstre(4,0,0))

                if type == 5:
                    taille = len(liste_monstres.liste_monstres5)
                    if taille < 1:
                        liste_monstres.liste_monstres5.append(Monstre(5,110,110))
                if type == 6:
                    taille = len(liste_monstres.liste_monstres6)
                    if taille < 21:
                        for i in range(7):
                            liste_monstres.liste_monstres6.append(Monstre(6,240 + i*100,45))
                            liste_monstres.liste_monstres6.append(Monstre(6,280 + i*100,105))
                            liste_monstres.liste_monstres6.append(Monstre(6,240 + i*100,180))
                        
                if type == 7:
                    taille = len(liste_monstres.liste_monstres7)
                    if taille < 130:
                        for i in range(130):
                            liste_monstres.liste_monstres7.append(Monstre(7,240 + i*6,randint(0,245)))
                           
            try:
                if seed<17:
                    spawnlist.update()
            except UnboundLocalError:
                pass


    def creation_projectiles(self,type,target):
        if type == 1:
            liste_projectiles.list_projectiles1.append(Projectiles(1,joueur1,target))
        if type == 2:
            for monstre in liste_monstres.liste_monstres2:
                liste_projectiles.list_projectiles2.append(Projectiles(2,monstre,target))
        if type == 3:
            for monstre in liste_monstres.liste_monstres4:
                    liste_projectiles.list_projectiles3.append(Projectiles(3,monstre,target))
        if type == 4:
            for monstre in liste_monstres.liste_monstres5:
                    liste_projectiles.list_projectiles4.append(Projectiles(4,monstre,target))

    def update(self) :
        if self.is_running == 201:
            if p.mouse_x > 99 and p.mouse_x < 159 and p.mouse_y > 114 and p.mouse_y < 132 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.accumul = p.frame_count
                self.is_running = 1
            if p.mouse_x > 99 and p.mouse_x < 159 and p.mouse_y > 139 and p.mouse_y < 151 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.is_running = 202
        if self.is_running == 202:
            if p.mouse_x > 9 and p.mouse_x < 27 and p.mouse_y > 225 and p.mouse_y < 242 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.is_running = 201
        if self.is_running == 200:
            if p.mouse_x > 199 and p.mouse_x < 240 and p.mouse_y > 229 and p.mouse_y < 242 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.is_running = 201
            if p.frame_count % 1 == 0 :
                if self.ind < 235:
                    self.ind += 1
            if self.fin == 1:
                if p.frame_count % 1 == 0:
                    if self.ind < 475:
                        self.ind += 1
                    else:
                        self.is_running = 201
        if joueur1.PV<1 and joueur1.vie_bonus>0:
            joueur1.PV_max=joueur1.PV_max//2
            joueur1.PV=joueur1.PV_max
            
            joueur1.vie_bonus-=1
        global seed


        seed=randint(0,self.rng_factor)

        if self.is_running==2:
            if p.mouse_x < 158 and p.mouse_x > 97 and p.mouse_y < 142 and p.mouse_y > 127 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.accumul = p.frame_count
                self.manche += 1
                self.liste_shop=[self.liste_powerups[randint(0,len(self.liste_powerups)-1)]for _ in range(self.taille_shop) ]
                if self.manche < 10 and self.manche != 5:
                    self.is_running = 1
                elif self.manche == 5:
                    self.is_running = 3
                elif self.manche == 10:
                    self.is_running = 4
            self.pause_time+=1
            p.cls(0)
        if self.is_running==1:
            if p.frame_count>(self.accumul + 900) and p.frame_count<(self.accumul + 950):
                self.accumul = p.frame_count
                self.is_running+=1


        if self.is_running == 3:
            self.rng_factor = 1800
            for monstre in liste_monstres.liste_monstres4:
                if monstre.PV < 1:
                    self.is_running = 2
        if self.is_running == 4:
            self.rng_factor = 1800
            for monstre in liste_monstres.liste_monstres5:
                if monstre.PV < 1:
                    self.is_running = 0#signifie la fin du jeu manche 10 environ 12 minutes de gameplay si victoire


        joueur1.levelHandler()
        joueur1.deplacement()
        joueur1.buffer()
        if pyxel.btnp(pyxel.KEY_UP):
            self.code.append(pyxel.KEY_UP)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.code.append(pyxel.KEY_DOWN)
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.code.append(pyxel.KEY_LEFT)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.code.append(pyxel.KEY_RIGHT)
        if pyxel.btnp(pyxel.KEY_B):
            self.code.append(pyxel.KEY_B)
        if pyxel.btnp(pyxel.KEY_A):
            self.code.append(pyxel.KEY_A)
        if len(self.code)>10:
            self.code=[]
        if self.code == self.konami_code:
                self.is_running-=50
                self.code=[]
        if self.code==[pyxel.KEY_A]:
            self.code==[]
            
        if p.btnp(p.KEY_I):
            print(p.mouse_x,p.mouse_y)
            print(joueur1.xp,joueur1.lvl)
        if p.btnp(p.KEY_P):
                p.quit()
        if p.btnp(p.KEY_V):
            print(liste_projectiles.list_projectiles1[0].xy)
        if (p.frame_count %15 == 0): 
            for _ in range(joueur1.tir_bonus):
                x1=joueur1.x
                x2=pyxel.mouse_x+randint(-20,20)
                y1=joueur1.y
                y2=pyxel.mouse_y+randint(-20,20)
                try:
                    coef=(y2-y1)/(x2-x1)
                except ZeroDivisionError:
                        coef= None
                if x2>x1 and coef!=None:
                    origine=y1-coef*x1
                    x2,y2=x2*50, coef*x2*50+origine
                elif x2<x1 and coef!=None:
                    origine=y1-coef*x1
                    x2,y2= (-1*x2)*50, coef*(x2*-1)*50+origine
                if coef is None and y2<y1:
                    y2/=100
                if coef is None and y2>y1:
                    y2*=50
                
                
                self.creation_projectiles(1,((int(x2)+randint(-20,20)),(int(y2)+randint(-20,20))))
        if self.is_running == 1:
            self.rng_factor = 900 - (self.manche * 20)
            self.creation_monstre(self.frames_checker())
            if joueur1.escadrille == 1:
                self.creation_monstre(6)
                self.creation_monstre(7)
                for monstre in liste_monstres.liste_monstres1:
                    liste_monstres.liste_monstres1.remove(monstre)
                for monstre in liste_monstres.liste_monstres2:
                    liste_monstres.liste_monstres2.remove(monstre)
                for monstre in liste_monstres.liste_monstres3:
                    liste_monstres.liste_monstres3.remove(monstre)
                for projectiles in liste_projectiles.list_projectiles1:
                    liste_projectiles.list_projectiles1.remove(projectiles)
                joueur1.escadrille = 3
            liste_monstres.mouvement_liste_monstre()
            if (p.frame_count % 6 == 0): #vitesse tir
                x1=joueur1.x
                x2=pyxel.mouse_x
                y1=joueur1.y
                y2=pyxel.mouse_y
                try:
                    coef=(y2-y1)/(x2-x1)
                except ZeroDivisionError:
                        coef= None
                if x2>x1 and coef!=None:
                    origine=y1-coef*x1
                    x2,y2=x2*50, coef*x2*50+origine
                elif x2<x1 and coef!=None:
                    origine=y1-coef*x1
                    x2,y2= (-1*x2)*50, coef*(x2*-1)*50+origine
                if coef is None and y2<y1:
                    y2/=100
                if coef is None and y2>y1:
                    y2*=50
                self.creation_projectiles(1,(x2,y2))
            if (p.frame_count % 25 == 0):
                self.creation_projectiles(2,joueur1.xy)
            liste_projectiles.mouvement_liste_projectiles()


        #tue les mobs lors de la pause
        if self.is_running == 2:
            for monstre in liste_monstres.liste_monstres1:
                liste_monstres.liste_monstres1.remove(monstre)
            for monstre in liste_monstres.liste_monstres2:
                liste_monstres.liste_monstres2.remove(monstre)
            for monstre in liste_monstres.liste_monstres3:
                liste_monstres.liste_monstres3.remove(monstre)
            for monstre in liste_monstres.liste_monstres4:
                liste_monstres.liste_monstres4.remove(monstre)
            for monstre in liste_monstres.liste_monstres6:
                liste_monstres.liste_monstres6.remove(monstre)
            for monstre in liste_monstres.liste_monstres7:
                liste_monstres.liste_monstres7.remove(monstre)
            for projectiles in liste_projectiles.list_projectiles1:
                liste_projectiles.list_projectiles1.remove(projectiles)
            for projectiles in liste_projectiles.list_projectiles2:
                liste_projectiles.list_projectiles2.remove(projectiles)
            for projectiles in liste_projectiles.list_projectiles3:
                liste_projectiles.list_projectiles3.remove(projectiles)
            for projectiles in liste_projectiles.list_projectiles4:
                liste_projectiles.list_projectiles4.remove(projectiles)




        if self.is_running == 3:
            self.creation_monstre(4)
            self.creation_monstre(self.frames_checker())
            liste_monstres.mouvement_liste_monstre()
            if (p.frame_count % 5 == 0):
                self.creation_projectiles(1,(pyxel.mouse_x,pyxel.mouse_y))
            if (p.frame_count % 5 == 0):
                self.creation_projectiles(3,joueur1.xy)
            if (p.frame_count % 20 == 0):
                self.creation_projectiles(2,joueur1.xy)
            liste_projectiles.mouvement_liste_projectiles()

        if self.is_running == 4:
            self.creation_monstre(5)
            self.creation_monstre(self.frames_checker())
            liste_monstres.mouvement_liste_monstre()
            if (p.frame_count % 5 == 0):
                self.creation_projectiles(1,(pyxel.mouse_x,pyxel.mouse_y))
            if (p.frame_count % 10 == 0):
                self.creation_projectiles(4,joueur1.xy)
            if (p.frame_count % 20 == 0):
                self.creation_projectiles(2,joueur1.xy)
            liste_projectiles.mouvement_liste_projectiles()


        if self.is_running == 0:
            for monstre in liste_monstres.liste_monstres1:
                liste_monstres.liste_monstres1.remove(monstre)
            for monstre in liste_monstres.liste_monstres2:
                liste_monstres.liste_monstres2.remove(monstre)
            for monstre in liste_monstres.liste_monstres3:
                liste_monstres.liste_monstres3.remove(monstre)
            for monstre in liste_monstres.liste_monstres4:
                liste_monstres.liste_monstres4.remove(monstre)
            for monstre in liste_monstres.liste_monstres5:
                liste_monstres.liste_monstres5.remove(monstre)
            for projectiles in liste_projectiles.list_projectiles1:
                liste_projectiles.list_projectiles1.remove(projectiles)
            for projectiles in liste_projectiles.list_projectiles2:
                liste_projectiles.list_projectiles2.remove(projectiles)
            for projectiles in liste_projectiles.list_projectiles3:
                liste_projectiles.list_projectiles3.remove(projectiles)
            for projectiles in liste_projectiles.list_projectiles4:
                liste_projectiles.list_projectiles4.remove(projectiles)

        for loot in listeloot.liste_loot:
            if pyxel.frame_count-loot.spawntime>150:

                listeloot.liste_loot.remove(loot)

            if loot.pos[0] <= joueur1.x + 15 and loot.pos[0] > joueur1.x -15 and loot.pos[1] <= joueur1.y + 15 and loot.pos[1] > joueur1.y - 15:#TODO : AFFINER LA COLLISION
                
                joueur1.powerup_check(loot.type)
                
                joueur1.buffer()
                try:
                    listeloot.liste_loot.remove(loot)
                except ValueError:
                    pass
                
                
        #MODE CREATIF
        if self.is_running<-2:
            self.pause_time+=1
            if p.btnp(p.KEY_R):
                self.accumul = p.frame_count
                self.is_running+=50
            self.rng_factor=0
            if (p.frame_count % 15 == 0): #vitesse tir
                x1=joueur1.x
                x2=pyxel.mouse_x
                y1=joueur1.y
                y2=pyxel.mouse_y
                try:
                    coef=(y2-y1)/(x2-x1)
                except ZeroDivisionError:
                        coef= None
                if x2>x1 and coef!=None:
                    origine=y1-coef*x1
                    x2,y2=x2*50, coef*x2*50+origine
                elif x2<x1 and coef!=None:
                    origine=y1-coef*x1
                    x2,y2= (-1*x2)*50, coef*(x2*-1)*50+origine
                if coef is None and y2<y1:
                    y2/=100
                if coef is None and y2>y1:
                    y2*=50
                self.creation_projectiles(1,(x2,y2))
            if (p.frame_count % 25 == 0):
                self.creation_projectiles(2,joueur1.xy)
            liste_projectiles.mouvement_liste_projectiles()
            if (p.frame_count %15 == 0): 
                for _ in range(joueur1.tir_bonus):
                    x1=joueur1.x
                    x2=pyxel.mouse_x+randint(-20,20)
                    y1=joueur1.y
                    y2=pyxel.mouse_y+randint(-20,20)
                    try:
                        coef=(y2-y1)/(x2-x1)
                    except ZeroDivisionError:
                            coef= None
                    if x2>x1 and coef!=None:
                        origine=y1-coef*x1
                        x2,y2=x2*50, coef*x2*50+origine
                    elif x2<x1 and coef!=None:
                        origine=y1-coef*x1
                        x2,y2= (-1*x2)*50, coef*(x2*-1)*50+origine
                    if coef is None and y2<y1:
                        y2/=100
                    if coef is None and y2>y1:
                        y2*=50
                    
                    
                    self.creation_projectiles(1,((int(x2)+randint(-20,20)),(int(y2)+randint(-20,20))))
            if self.game_status<=10:
                self.game_status+=1
                for monstre in liste_monstres.liste_monstres1:
                    liste_monstres.liste_monstres1.remove(monstre)
                for monstre in liste_monstres.liste_monstres2:
                    liste_monstres.liste_monstres2.remove(monstre)
                for monstre in liste_monstres.liste_monstres3:
                    liste_monstres.liste_monstres3.remove(monstre)
                for monstre in liste_monstres.liste_monstres4:
                    liste_monstres.liste_monstres4.remove(monstre)
                for monstre in liste_monstres.liste_monstres6:
                    liste_monstres.liste_monstres6.remove(monstre)
                for monstre in liste_monstres.liste_monstres7:
                    liste_monstres.liste_monstres7.remove(monstre)
                for projectiles in liste_projectiles.list_projectiles1:
                    liste_projectiles.list_projectiles1.remove(projectiles)
                for projectiles in liste_projectiles.list_projectiles2:
                    liste_projectiles.list_projectiles2.remove(projectiles)
                for projectiles in liste_projectiles.list_projectiles3:
                    liste_projectiles.list_projectiles3.remove(projectiles)
                for projectiles in liste_projectiles.list_projectiles4:
                    liste_projectiles.list_projectiles4.remove(projectiles)
                for spawn in spawnlist.spawnlist:
                    spawnlist.spawnlist.remove(spawn)
            liste_monstres.mouvement_liste_monstre()
            if  p.btnr(p.KEY_KP_1):
                self.creation_monstre(1)
            if  p.btnr(p.KEY_KP_2):
                self.creation_monstre(2)
            if  p.btnr(p.KEY_KP_3):
                self.creation_monstre(3)
            if  p.btnr(p.KEY_KP_4):
                self.creation_monstre(4)
            if  p.btnr(p.KEY_KP_5):
                self.creation_monstre(5)
            
            if p.btnr(p.KEY_1):
                listeloot.liste_loot.append(Loot(5,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_2):
                listeloot.liste_loot.append(Loot(15,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_3):
                listeloot.liste_loot.append(Loot(25,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_4):
                listeloot.liste_loot.append(Loot(35,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_5):
                listeloot.liste_loot.append(Loot(45,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_6):
                listeloot.liste_loot.append(Loot(56,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_7):
                listeloot.liste_loot.append(Loot(68,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_8):
                listeloot.liste_loot.append(Loot(80,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_9):
                listeloot.liste_loot.append(Loot(89,(50,50),pyxel.frame_count))
            if p.btnr(p.KEY_0):
                listeloot.liste_loot.append(Loot(99,(50,50),pyxel.frame_count))
                
                
            
            
            #si on appuie sur une touche, ca fait spawn un monstre de type 1 si on appuie sur 1 etc
            #si on appuie sur une autre touche (h?) ca fait spawn un powerup (hp?) etc
            #numpad pour les mobs et f key pour les powerups?
            #faut voir si la logique des boss est link au is running, si oui c'est mort pour les boss :/
       

    def draw(self) :
        p.cls(0)
        pyxel.blt(pyxel.mouse_x,pyxel.mouse_y,0,42,18,4,4,0)
        if self.is_running == 201:
            p.bltm(0,0,0,249-p.frame_count % 249,240,250,230,0)
            p.blt(100,115,0,118,200,58,16,0)
            p.blt(100,140,0,152,1,58,11,0)
        if self.is_running == 202:
            p.blt(10,225,0,216,0,16,16,0)
            p.text(10,20,"Deplacements du vaisseau :    Z / Q / S / D",10)
            p.text(10,50,"Le tir est automatique, pour viser : Direction de la souris",10)
            p.text(10,70,"Vous devez detruire des ennemis, pour acquerir de l'xp ",10)
            p.text(10,80,"qui vous permettra d'acheter des ameliorations dans le shop",10)
            p.text(10,100,"Une fois dans la partie, vous pourrez faire appel ",10)
            p.text(10,110,"a l'escadrille (en appuyant sur b)",10)
            p.blt(100,175,0,72,186,33,31,0)
        if self.is_running == 200:
            p.blt(200,230,1,0,46,39,12,0)
            
            timer2 =(p.frame_count-self.pause_time )//30
            if timer2 > 18:
                self.fin = 1
           
            p.text(109,250 - self.ind,"STAR WARS",10)
            p.text(38,300-self.ind,"L'EMPIRE REPEND LA TERREUR DANS LA GALAXIE, ",10)
            p.text(30,310-self.ind,"ET IL EST SUR LE POINT DE DECOUVRIR L'EMPLACEMENT",10)
            p.text(38,320-self.ind,"DE LA BASE DE LA RESISTANCE. VOUS INCARNEZ LE",10)
            p.text(28,330-self.ind,"MEILLEUR PILOTE D'UN ESCADRON POUR TENTER DE DETRUIRE ",10)
            p.text(17,340-self.ind,"LA TERRIBLE ETOILE DE LA MORT A BORD DU FAUCON MILLENIUM ",10)
            p.text(24,370-self.ind,"ALERTE PAR VOTRE ARRIVEE, L'EMPIRE DEPLOIE SA FLOTTE",10)
            p.text(24,380-self.ind,"DE CHASSEUR TIE ET ENGAGE DES CHASSEURS DE PRIME POUR",10)
            p.text(26,390-self.ind,"VOUS EXTERMINER. VOTRE ESCADRON EST EN ROUTE, MAIS IL ",10)
            p.text(55,400-self.ind,"FAUT FAIRE FACE SEUL POUR LE MOMENT",10)
           
            p.text(70,440-self.ind,"QUE LA FORCE SOIT AVEC VOUS",10)
        if joueur1.PV>0 and self.manche < 11 and self.is_running != 200 and self.is_running != 202:
            if self.is_running == 0:
                pyxel.text(110,110,'VICTOIRE', 15)
            


            if self.is_running == 3:
                p.blt(74,29,0,0,88,102,8,0)
                for monstre in liste_monstres.liste_monstres4:
                    
                    for k in range(int((monstre.PV/monstre.PV_max)*100)): #on prend le pourcentage de pv restant qu'on divise par deux pour avoir le nombre de pixel a dessiné (chaque pixel =2% de vie), on peut augmenter ce nombre si jamais ca rend pas bien, par exemple prendre 3% au lieu de 2%
                        p.pset(75+k,30,9) #on vas colorier les k pourcent de vie restant, cad si on est full vie on colorie toute la barre mais si on a que 50% de vie alors on colorie que la moitié
                        p.pset(75+k,31,9)
                        p.pset(75+k,32,9)
                        p.pset(75+k,33,9)
                        # on fais pareil a la ligne y+1 pour que la barre de vie fasse 2 pixel d'épaisseur
                    #ici 191 correspond a l'extrémité gauche de la barre de vie, si on veut que la barre de vie fasse tout l'écran il faut mettre cette a valeur a environ 5/10
                    #ici 3=236 correspond au plafond de la barre de vie, si on veut qu'elle soit en haut il faut mettre cette valeur a environ 5/10
                    #if monstre.PV >= 4500 : p.blt(74,20,0,1,81,100,4)
                    #if monstre.PV < 4500 and monstre.PV >= 4000: p.blt(74,20,0,1,80,90,4)
                    #if monstre.PV < 4000 and monstre.PV >= 3500: p.blt(74,20,0,1,80,80,4)
                    #if monstre.PV < 3500 and monstre.PV >= 3000: p.blt(74,20,0,1,80,70,4)
                    #if monstre.PV < 3000 and monstre.PV >= 2500: p.blt(74,20,0,1,80,60,4)
                    #if monstre.PV < 2500 and monstre.PV >= 2000: p.blt(74,20,0,1,80,50,4)
                    #if monstre.PV < 2000 and monstre.PV >= 1500: p.blt(74,20,0,1,80,40,4)
                    #if monstre.PV < 1500 and monstre.PV >= 1000: p.blt(74,20,0,1,80,30,4)
                    #if monstre.PV < 1000 and monstre.PV >= 500: p.blt(74,20,0,1,80,20,4)
                    #if monstre.PV < 500 and monstre.PV > 0: p.blt(74,20,0,1,80,10,4)
            if self.is_running == 4:
                p.blt(74,29,0,0,88,102,8,0)
                for monstre in liste_monstres.liste_monstres5:
                    for k in range(int((monstre.PV/monstre.PV_max)*100)): #on prend le pourcentage de pv restant qu'on divise par deux pour avoir le nombre de pixel a dessiné (chaque pixel =2% de vie), on peut augmenter ce nombre si jamais ca rend pas bien, par exemple prendre 3% au lieu de 2%
                        p.pset(75+k,30,9) #on vas colorier les k pourcent de vie restant, cad si on est full vie on colorie toute la barre mais si on a que 50% de vie alors on colorie que la moitié
                        p.pset(75+k,31,9)
                        p.pset(75+k,32,9)
                        p.pset(75+k,33,9)# on fais pareil a la ligne y+1 pour que la barre de vie fasse 2 pixel d'épaisseur
                    #ici 191 correspond a l'extrémité gauche de la barre de vie, si on veut que la barre de vie fasse tout l'écran il faut mettre cette a valeur a environ 5/10
                    #ici 3=236 correspond au plafond de la barre de vie, si on veut qu'elle soit en haut il faut mettre cette valeur a environ 5/10
                    #if monstre.PV >= 1800 : p.blt(74,20,0,1,81,100,4)
                    #if monstre.PV < 1800 and monstre.PV >= 1600: p.blt(74,20,0,1,80,90,4)
                    #if monstre.PV < 1600 and monstre.PV >= 1400: p.blt(74,20,0,1,80,80,4)
                    #if monstre.PV < 1400 and monstre.PV >= 1200: p.blt(74,20,0,1,80,70,4)
                    #if monstre.PV < 1200 and monstre.PV >= 1000: p.blt(74,20,0,1,80,60,4)
                    #if monstre.PV < 1000 and monstre.PV >= 800: p.blt(74,20,0,1,80,50,4)
                    #if monstre.PV < 800 and monstre.PV >= 600: p.blt(74,20,0,1,80,40,4)
                    #if monstre.PV < 600 and monstre.PV >= 400: p.blt(74,20,0,1,80,30,4)
                    #if monstre.PV < 400 and monstre.PV >= 200: p.blt(74,20,0,1,80,20,4)
                    #if monstre.PV < 200 and monstre.PV > 0: p.blt(74,20,0,1,80,10,4)

            if self.is_running != 2 and self.is_running != 0 and self.is_running != 201:
                p.bltm(0,0,0,0,276,250,230,0)
            if self.is_running !=2:
                if joueur1.touch == True:
                    p.blt(joueur1.x,joueur1.y,0,40,216,16,16,0)
                    joueur1.touch = False
                else:
                    p.blt(joueur1.x,joueur1.y,0,16,200,16,16,0)
            p.text(5,240,"score : " + str(joueur1.score),10)
            p.text(5,230,"xp : " + str(joueur1.xp)+"/"+str(int(joueur1.lvl*1.4+10)),10)
            p.text(5,220,"Points : " + str(joueur1.points),10)
            pyxel.text(110,5,"Manche :" + str(self.manche),10)
            timer =(p.frame_count-self.pause_time )//30
            if self.is_running != 201:
                p.text(0,0,str(timer),8)
            p.text(190,240,str(joueur1.PV)+"/"+str(joueur1.PV_max),10)
            
            
            if self.is_running!=2 and self.is_running != 0:
                for loot in listeloot.liste_loot:
                    if loot.type == "   Spd":
                        p.blt(loot.pos[0],loot.pos[1],0,129,236,12,12,0)
                    if loot.type == "   ATK":
                        p.blt(loot.pos[0],loot.pos[1],0,99,236,12,12,0)
                    if loot.type == "   def":
                        p.blt(loot.pos[0],loot.pos[1],0,114,236,12,12,0)
                    if loot.type == "   tir":
                        p.blt(loot.pos[0],loot.pos[1],0,146,236,12,12,0)
                    if loot.type == "  crit":
                        p.blt(loot.pos[0],loot.pos[1],0,90,52,12,12,0)
                    if loot.type == "    HP":
                        p.blt(loot.pos[0],loot.pos[1],0,178,236,12,12,0)
                    if loot.type == " sangsue":
                        p.blt(loot.pos[0],loot.pos[1],0,162,236,12,12,0)
                    if loot.type == "  luck":
                        p.blt(loot.pos[0],loot.pos[1],0,130,114,12,12,0)
                    if loot.type == " SPD proj":
                        p.blt(loot.pos[0],loot.pos[1],0,95,220,12,12,0)
                    if loot.type == "   1UP":
                        p.blt(loot.pos[0],loot.pos[1],0,154,180,12,12,0)
                    
                for el in spawnlist.spawnlist:
                    if self.is_running != 201:
                        p.blt(el.x,el.y,0,0,48,8,8,0) #indicateur de spawn, A MODIFIER PAR UN SPRITE!!
            for monstre in liste_monstres.liste_monstres1 :
                if monstre.PV <1 or monstre.touch == 1:
                    p.blt(monstre.x,monstre.y,0,24,64,16,16,0)
                    p.circb(monstre.x+8,monstre.y+8,9,3)
                    p.circb(monstre.x+8,monstre.y+8,10,3)
                    p.circb(monstre.x+8,monstre.y+8,11,10)
                    p.circb(monstre.x+8,monstre.y+8,12,10)
                    
                p.blt(monstre.x,monstre.y,0,56,184,16,16,0)
            for monstre in liste_monstres.liste_monstres2 :
                if monstre.PV < 1:
                    p.blt(monstre.x,monstre.y,0,24,64,16,16,0)
                    p.circb(monstre.x+8,monstre.y+8,9,3)
                    p.circb(monstre.x+8,monstre.y+8,10,3)
                    p.circb(monstre.x+8,monstre.y+8,11,10)
                    p.circb(monstre.x+8,monstre.y+8,12,10)
                if monstre.touch == 1:
                    p.blt(monstre.x,monstre.y,0,86,0,24,18,0)
                  
                p.blt(monstre.x,monstre.y,0,112,26,20,14,0)
            for monstre in liste_monstres.liste_monstres3 :
                if monstre.PV < 1:
                    p.blt(monstre.x,monstre.y,0,24,64,16,16,0)
                    p.circb(monstre.x+8,monstre.y+8,9,3)
                    p.circb(monstre.x+8,monstre.y+8,10,3)
                    p.circb(monstre.x+8,monstre.y+8,11,10)
                    p.circb(monstre.x+8,monstre.y+8,12,10)
                    
                p.blt(monstre.x,monstre.y,0,16,184,16,16,0)
            for monstre in liste_monstres.liste_monstres4 :
                if monstre.touch == 1:

                    p.blt(monstre.x-1,monstre.y,0,7,224,24,25)
                    monstre.touch = 0
                else:
                    p.blt(monstre.x,monstre.y,0,33,184,22,23,0)
            for monstre in liste_monstres.liste_monstres5 :
                if monstre.touch == 1:
                    p.blt(monstre.x-1,monstre.y,0,7,224,24,25)
                    monstre.touch = 0
                else:
                    p.blt(monstre.x,monstre.y,0,9,152,22,23,0)
            for monstre in liste_monstres.liste_monstres6:
                p.blt(monstre.x,monstre.y,0,72,186,33,31,0)
            for monstre in liste_monstres.liste_monstres7:
                p.blt(monstre.x,monstre.y,0,0,104,32,1,0)
            
            for projectile in liste_projectiles.list_projectiles1 : p.blt(projectile.x,projectile.y,0,57,117,4,3,0)
            for projectile in liste_projectiles.list_projectiles2 : p.blt(projectile.x,projectile.y,0,57,105,4,3,0)
            for projectile in liste_projectiles.list_projectiles3 : p.blt(projectile.x,projectile.y,0,57,105,4,3,0)
            for projectile in liste_projectiles.list_projectiles4 : p.blt(projectile.x,projectile.y,0,57,105,4,3,0)
            p.blt(190,235,0,32,34,52,4,0)
            for k in range(int(((joueur1.PV/joueur1.PV_max)*100)/2)): #on prend le pourcentage de pv restant qu'on divise par deux pour avoir le nombre de pixel a dessiné (chaque pixel =2% de vie), on peut augmenter ce nombre si jamais ca rend pas bien, par exemple prendre 3% au lieu de 2%
                p.pset(191+k,236,8) #on vas colorier les k pourcent de vie restant, cad si on est full vie on colorie toute la barre mais si on a que 50% de vie alors on colorie que la moitié
                p.pset(191+k,237,8)# on fais pareil a la ligne y+1 pour que la barre de vie fasse 2 pixel d'épaisseur
                #ici 191 correspond a l'extrémité gauche de la barre de vie, si on veut que la barre de vie fasse tout l'écran il faut mettre cette a valeur a environ 5/10
                #ici 3=236 correspond au plafond de la barre de vie, si on veut qu'elle soit en haut il faut mettre cette valeur a environ 5/10
            if joueur1.escadrille != 3:
                p.text(60,230,"Escadrille",15)
                p.blt(60,237,0,0,120,42,10,0)
                if joueur1.score < 1200:
                    for i in range(joueur1.score // 30):
                        p.pset(61+i,238,4)
                        p.pset(61+i,239,4)
                        p.pset(61+i,240,4)
                        p.pset(61+i,241,4)
                        p.pset(61+i,242,4)
                        p.pset(61+i,243,4)
                        p.pset(61+i,244,4)
                        p.pset(61+i,245,4)
                else:
               
            
                    p.blt(61,238,0,0,133,40,8,0)
                    if p.btnp(p.KEY_B):
                        joueur1.escadrille = 1
            if self.is_running==2:
                p.bltm(0,0,0,0,0,250,125,0)
                p.bltm(0,125,0,249-p.frame_count % 249,240,250,126,0)

                p.blt(175,160,0,72,186,33,31,0)
                p.blt(145,210,0,72,186,33,31,0)
                p.blt(85,180,0,72,186,33,31,0)
                p.blt(98,128,0,1,1,59,13,0)
                for i in range(3):
                    p.text(60+i*50,60,self.liste_shop[i],8)
                    if self.liste_shop[i] == "   Spd":
                        p.blt(70+i*50+1,71,0,129,236,12,12,0)
                    if self.liste_shop[i] == "   ATK":
                        p.blt(70+i*50+1,71,0,99,236,12,12,0)
                    if self.liste_shop[i] == "   def":
                        p.blt(70+i*50+1,71,0,114,236,12,12,0)
                    if self.liste_shop[i] == "   tir":
                        p.blt(70+i*50+1,71,0,146,236,12,12,0)
                    if self.liste_shop[i] == "  crit":
                        p.blt(70+i*50+1,71,0,90,52,12,12,0)
                    if self.liste_shop[i] == "    HP":
                        p.blt(70+i*50+1,71,0,178,236,12,12,0)
                    if self.liste_shop[i] == " sangsue":
                        p.blt(70+i*50+1,71,0,162,236,12,12,0)
                    if self.liste_shop[i] == "  luck":
                        p.blt(70+i*50+1,71,0,130,114,12,12,0)
                    if self.liste_shop[i] == " SPD proj":
                        p.blt(70+i*50+1,71,0,95,220,12,12,0)
                    if self.liste_shop[i] == "   1UP":
                        p.blt(70+i*50+1,71,0,154,180,12,12,0)

                    p.rectb(70+i*50,70,14,14,6)
                    if p.mouse_x>=(69+50*i) and p.mouse_x<=(83+50*i) and p.mouse_y>=69 and p.mouse_y<=83:
                        p.rect(70+50*i,70,14,14,6)
                        if p.btnp(p.MOUSE_BUTTON_LEFT):
                            if joueur1.points>0 and self.liste_shop[i]!="   1UP":
                                p.rect(70+50*i,70,14,14,15)
                                joueur1.points-=1
                                joueur1.powerup_check(self.liste_shop[i]) #TODO retirer le fait de pouvoir acheter le power up si il a deja été acheté une fois
                            elif joueur1.points>3:
                                p.rect(70+50*i,70,14,14,15)
                                joueur1.points-=3
                                joueur1.powerup_check(self.liste_shop[i])
                            else:
                                p.rect(70+50*i,70,14,14,4)
                for k in range(2):
                    p.text(85+k*50,90,self.liste_shop[k+3],8)

                    if self.liste_shop[k+3] == "   Spd":
                        p.blt(95+k*50+1,101,0,129,236,12,12,0)
                    if self.liste_shop[k+3] == "   ATK":
                        p.blt(95+k*50+1,101,0,99,236,12,12,0)
                    if self.liste_shop[k+3] == "   def":
                        p.blt(95+k*50+1,101,0,114,236,12,12,0)
                    if self.liste_shop[k+3] == "   tir":
                        p.blt(95+k*50+1,101,0,146,236,12,12,0)
                    if self.liste_shop[k+3] == "  crit":
                        p.blt(95+k*50+1,101,0,90,52,12,12,0)
                    if self.liste_shop[k+3] == "    HP":
                        p.blt(95+k*50+1,101,0,178,236,12,12,0)
                    if self.liste_shop[k+3] == " sangsue":
                        p.blt(95+k*50+1,101,0,162,236,12,12,0)
                    if self.liste_shop[k+3] == "  luck":
                        p.blt(95+k*50+1,101,0,130,114,12,12,0)
                    if self.liste_shop[k+3] == " SPD proj":
                        p.blt(95+k*50+1,101,0,95,220,12,12,0)
                    if self.liste_shop[k+3] == "   1UP":
                        p.blt(95+k*50+1,101,0,154,180,12,12,0)
                    p.rectb(95+k*50,100,14,14,6)
                    if p.mouse_x>=(94+50*k) and p.mouse_x<=(108+50*k) and p.mouse_y>=99 and p.mouse_y<=113:
                        p.rect(95+50*k,100,14,14,6)
                        if p.btnp(p.MOUSE_BUTTON_LEFT):
                            if joueur1.points>0 and self.liste_shop[k+3]!="   1UP":
                                p.rect(95+50*k,100,14,14,15)
                                joueur1.points-=1
                                joueur1.powerup_check(self.liste_shop[k+3]) #TODO retirer le fait de pouvoir acheter le power up si il a deja été acheté une fois
                            elif joueur1.points>3:
                                p.rect(95+50*k,100,14,14,15)
                                joueur1.points-=3
                                joueur1.powerup_check(self.liste_shop[k+3])
                            else:
                                p.rect(95+50*k,100,14,14,4)#faut faire rester les couleurs plus longtemps ca reste qu'une frame la

                        # on ajoute le power up cliqué cad:
        elif self.is_running == 0:
                pyxel.text(110,110,'VICTOIRE', 15)                #joueur1.nompowerup+=1
                        #on enleve la ressource d'amélioration
        else:
            if self.is_running != 200 and self.is_running != 202:
                pyxel.text(75,98,'GAME OVER', 15)
                pyxel.text(75,120,"SCORE : " + str(joueur1.score) + " points",15)
                       #joueur1.ressource-=1



            
        
class Joueur :
    def __init__(self,PV,ATK) :

        #début d'idée de powerups
        self.ATK_bonus=0
        self.HP_bonus=0
        self.tir_bonus=0
        self.lifesteal_bonus=0
        self.SPD_bonus=0
        #self.range_bonus=0
        self.aimbot=False
        self.luck_bonus=0
        self.rebonds=False
        self.gun_type="standard"
        self.reduction_degats=0
        self.taux_crit=0
        self.vie_bonus=0
        self.vitesse_tir_bonus=0

        self.x = 150
        self.y = 150
        self.xy = [self.x,self.y]
        self.PV = PV
        self.PV_max=PV
        self.ATK = ATK
        self.score = 0
        self.xp=0
        self.lvl=1
        self.luck=0
        self.range=60
        self.points=0
        self.lifesteal=0
        self.SPD=0.9
        self.touch = False
        self.escadrille = 0

    def buffer(self):
        self.PV_max+=self.HP_bonus
        self.HP_bonus=0
        self.ATK+=self.ATK_bonus
        self.ATK_bonus=0
        for _ in range(self.SPD_bonus):
            self.SPD*=1.20
        self.SPD_bonus=0
        self.luck+=self.luck_bonus
        self.luck=0
        #for _ in range(self.range_bonus):
            #self.range_bonus*=1.5
        #self.range_bonus=0
        self.lifesteal+=self.lifesteal_bonus
        self.lifesteal_bonus=0
    def levelHandler(self):
        if self.xp>=int((self.lvl*1.4+10)):
            self.xp-=int(self.lvl*1.4+10)
            self.lvl+=1
            self.points+=1
        
    def powerup_check(self,str):
        
        if str=="   ATK":
            self.ATK_bonus+=1
        if str=="    HP":
            self.HP_bonus+=1
        if str=="   tir":
            self.tir_bonus+=1
        if str=="   Spd":
            self.SPD_bonus+=1
        #if str=="range":
            #self.range_bonus+=1
        if str=="  luck":
            self.luck_bonus+=1
        if str==" sangsue":
            self.lifesteal_bonus+=3
        if str=="   def":
            self.reduction_degats+=5
        if str=="  crit":
            self.taux_crit+=5
        if str=="   1UP":
            self.vie_bonus+=1
        if str==" SPD proj":
            self.vitesse_tir_bonus+=1


    def deplacement(self) :
        if pyxel.btn(pyxel.KEY_S) and self.y +15 <= 250:
            self.y += self.SPD

        if pyxel.btn(pyxel.KEY_Z) and self.y >= 0:
            self.y -= self.SPD

        if pyxel.btn(pyxel.KEY_D) and self.x +13<= 250:
            self.x += self.SPD

        if pyxel.btn(pyxel.KEY_Q) and self.x >= 0:
            self.x -= self.SPD

        self.xy = [self.x,self.y]


class Monstre :
    def __init__(self,type,x,y) :
        self.touch = 0
        self.type=type
        self.x = x
        self.y = y
        self.xy = [x,y]
        self.el = 0
        self.el_bis = 0
        if type == 1 :
            self.PV = 10
            self.ATK = 2
            self.PV_max= 10
        if type == 2:
            self.PV = 20
            self.ATK = 5
            self.PV_max=20
        if type == 3:
            self.PV = 30
            self.ATK = 5
            self.PV_max=30
        if type == 4:
            self.PV = 3500
            self.PV_max = 3500
            self.ATK = 10
        if type == 5:
            self.PV = 2000
            self.ATK = 10
            self.zone = 1
            self.PV_max = 2000
    
    def limite_zone(self):
        if self.x < 5:
            self.x += 20
        if self.x > 220:
            self.x-= 15
        if self.y < 5:
            self.y += 20
        if self.y > 220:
            self.y-= 15
    
    def aleatoire(self):
        self.el = randint(0,1)
        self.el_bis = randint(0,1)
    
    def mouv_mons_1(self):
        chemin = ligne(self.xy,joueur1.xy)
        self.x = chemin[2][0]
        self.y = chemin[2][1]
        
   
    def mouv_mons_2(self):
        self.aleatoire()
        if self.el == 0:
            if self.el_bis == 0:
                self.x -= 1
            else:
                self.x += 1
        else:
            if self.el_bis == 0:
                    self.y -= 1
            else:
                self.y += 1
        
    def attaque_mons_3(self):
        if self.x < joueur1.x + 4 and self.x > joueur1.x -4:
            self.y = joueur1.y-16
        elif self.y < joueur1.y + 4 and self.y > joueur1.y -4:
            self.x = joueur1.x -24
        
    def mouv_mons_3(self):
        self.attaque_mons_3()
        self.limite_zone()
        if self.x > 125 and self.x < 240:
            self.x += 1
        elif self.x < 125 and self.x > 2:
            self.x -= 1
        if self.y > 125 and self.y < 240:
            self.y += 1
        elif self.y < 125 and self.y > 2:
            self.y -= 1
           
        
    def mouvement_monstre(self,type) : #location= endroit vers lequel on veut se diriger
        if type == 1 :
            self.mouv_mons_1()
        if type == 2:
           self.mouv_mons_2()
        if type == 3:
           self.mouv_mons_3()
  

        if type == 4:
            chemin = ligne(self.xy,joueur1.xy)
            self.x = chemin[5][0]
            self.y = chemin[5][1]
            


        if type == 5:
            if self.x < 225 and self.y == 0:
                self.x += 5
            if self.x == 225 and self.y < 225:
                self.y += 5
            if self.y == 225 and self.x >= 5:
                self.x -= 5
            if self.x == 0 and self.y >= 5:
                self.y -= 5
            

        if type == 6:
            if self.zone == 1:
                self.x = randint(180,224)
                self.y = randint(20,60)

            if self.zone == 2:
                self.x = randint(20,65)
                self.y = randint(180,224)

            if self.zone == 3:
                self.x = randint(20,85)
                self.y = randint(20,85)

            if self.zone ==4:
                self.x = randint(160,224)
                self.y = randint(170,220)
            if self.zone == 5:
                self.x = 110
                self.y = 110
                self.zone = 0
            
            self.zone += 1
        if type == 7:
            self.x -= 7
            
        if type == 8:
            self.x -= 9
            
        self.xy = [self.x, self.y]
class ListeMonstres : #tableaux contenant les objets monstres
    def __init__(self) :
        self.liste_monstres1 = []
        self.liste_monstres2 = []
        self.liste_monstres3 = []
        self.liste_monstres4 = []
        self.liste_monstres5 = []
        self.liste_monstres6 = []
        self.liste_monstres7 = []

    def mouvement_liste_monstre(self) :
        for monstre in self.liste_monstres1 :
            if monstre.PV<1:
                if randint(1,100)+joueur1.lifesteal>90:
                    if joueur1.PV+monstre.PV_max<joueur1.PV_max:
                        joueur1.PV+=monstre.PV_max
                joueur1.xp = joueur1.xp + 1
                self.liste_monstres1.remove(monstre)
                listeloot.lootCheck(monstre.xy)
                joueur1.score = joueur1.score + 10
                
            if monstre.x +15 > joueur1.x and monstre.x < joueur1.x + 15 and monstre.y < joueur1.y + 15 and monstre.y + 15 > joueur1.y:
                monstre.touch = 1
                joueur1.touch = True
                joueur1.PV -= monstre.ATK
                try:
                    self.liste_monstres1.remove(monstre)
                except ValueError:
                    pass
                listeloot.lootCheck(monstre.xy)
            if p.frame_count % 2 == 0:
                monstre.mouvement_monstre(1)

        for monstre in self.liste_monstres2 :
            if monstre.PV<1:
                if randint(1,100)+joueur1.lifesteal>90:
                    if joueur1.PV+monstre.PV_max<joueur1.PV_max:
                        joueur1.PV+=monstre.PV_max
                joueur1.xp = joueur1.xp + 1
                self.liste_monstres2.remove(monstre)
                listeloot.lootCheck(monstre.xy)
                joueur1.score = joueur1.score + 20
               
            if monstre.x <= joueur1.x + 15 and monstre.x > joueur1.x -15 and monstre.y <= joueur1.y + 15 and monstre.y > joueur1.y - 15:
                monstre.touch = 1
                joueur1.touch = True
                joueur1.PV -= monstre.ATK
                self.liste_monstres2.remove(monstre)
                listeloot.lootCheck(monstre.xy)
            if p.frame_count % 4 == 0:
                monstre.mouvement_monstre(2)

        for monstre in self.liste_monstres3 :
            if monstre.PV<1:
                if randint(1,100)+joueur1.lifesteal>90:
                    if joueur1.PV+monstre.PV_max<joueur1.PV_max:
                        joueur1.PV+=monstre.PV_max
                joueur1.xp = joueur1.xp + 1
                self.liste_monstres3.remove(monstre)
                listeloot.lootCheck(monstre.xy)
                joueur1.score = joueur1.score + 40
                
            if monstre.x +15 > joueur1.x and monstre.x < joueur1.x + 15 and monstre.y < joueur1.y + 15 and monstre.y + 15 > joueur1.y:
                monstre.touch = 1
                joueur1.touch = True
                joueur1.PV -= monstre.ATK
                try:
                    self.liste_monstres3.remove(monstre)
                except ValueError:
                    pass
                listeloot.lootCheck(monstre.xy)
               
            if p.frame_count % 5 == 0:
                monstre.mouvement_monstre(3)
           
        for monstre in self.liste_monstres4 :
            if monstre.PV<1:
                self.liste_monstres4.remove(monstre)
                listeloot.lootCheck(monstre.xy)
                joueur1.score += 100
            if joueur1.x <= monstre.x + 24 and joueur1.x > monstre.x - 16 and joueur1.y <= monstre.y + 24 and joueur1.y > monstre.y - 16:
                joueur1.touch = True
                joueur1.PV -= monstre.ATK

            if p.frame_count % 2 == 0:
                monstre.mouvement_monstre(5)

        for monstre in self.liste_monstres5 :
            if monstre.PV<1:
                self.liste_monstres5.remove(monstre)
                listeloot.lootCheck(monstre.xy)
                joueur1.score += 1000
            if joueur1.x <= monstre.x + 24 and joueur1.x > monstre.x -16 and joueur1.y <= monstre.y + 24 and joueur1.y > monstre.y - 16:
                joueur1.touch = True
                joueur1.PV -= monstre.ATK
               
            if p.frame_count % 50 == 0:
                monstre.mouvement_monstre(6)
                
        # NE PAS TOUCHER MONSTRES 6 et 7 CE SONT LES VAISSEAUX ET TIRS DE L'ATTAQWUE SPECIALE DONC NE PAS AJOUTER DE SCORe/XP/tout power up etc 
            
        
        for monstre in self.liste_monstres6:
            if p.frame_count % 2 == 0:
                monstre.mouvement_monstre(7)
        for monstre in self.liste_monstres7 :
            for mons in self.liste_monstres1:
                if monstre.x  < mons.x + 16 and monstre.x + 32 >= mons.x and monstre.y < mons.y + 16 and monstre.y >= mons.y:
                    mons.PV = 0
            for mons in self.liste_monstres2:
                if monstre.x  < mons.x + 20 and monstre.x + 32 >= mons.x and monstre.y < mons.y + 14 and monstre.y >= mons.y:
                    mons.PV = 0
            for mons in self.liste_monstres3:
                if monstre.x  < mons.x + 16 and monstre.x + 32  >= mons.x and monstre.y < mons.y + 16 and monstre.y >= mons.y:
                    mons.PV = 0
            if p.frame_count % 2 == 0:
                monstre.mouvement_monstre(8)

    def liste_remove(self,other):
        if other.type == 1:
            try:
                self.liste_monstres1.remove(other)
            except ValueError:
                print(other)
        if other.type == 2:
            try:
                self.liste_monstres2.remove(other)
            except ValueError:
                print(other)
        if other.type == 3:
            try:
                self.liste_monstres3.remove(other)
            except ValueError:
                print(other)





class Projectiles :
    def __init__(self,type,lanceur,target) :
        self.x = lanceur.x
        self.y=lanceur.y
        self.xy=lanceur.xy
        self.lanceur = lanceur

        self.progression=0
        self.target=target
        if type == 1 :
            self.ATK = 20

        if type == 2:
            self.ATK = 10

        if type == 3:
            self.ATK = 5
        if type == 4:
            self.ATK = 30


    def mouvement_projectile(self,type) :
        if type == 1:

            chemin = ligne(self.xy,self.target,self.lanceur.range)
            self.x = chemin[3+self.lanceur.vitesse_tir_bonus][0]
            self.y = chemin[3+self.lanceur.vitesse_tir_bonus][1]
            self.xy = [self.x,self.y]
            for monstre in liste_monstres.liste_monstres1:
                if self.x < monstre.x +16 and self.x + 4 > monstre.x -1 and self.y  < monstre.y +16 and self.y + 3 > monstre.y -1:
                    monstre.touch = 1
                    monstre.PV -= self.ATK
                    try:
                        liste_projectiles.list_projectiles1.remove(self)
                    except ValueError:
                        pass

            for monstre in liste_monstres.liste_monstres2:
                if self.x  < monstre.x +16 and self.x + 4 > monstre.x -1 and self.y  < monstre.y +16 and self.y + 3 > monstre.y -1:
                    monstre.touch = 1
                    monstre.PV -= self.ATK
                    try:
                        liste_projectiles.list_projectiles1.remove(self)
                    except ValueError:
                        pass

            for monstre in liste_monstres.liste_monstres3:
                if self.x  < monstre.x +16 and self.x + 4 > monstre.x -1 and self.y  < monstre.y +16 and self.y + 3 > monstre.y -1:
                    monstre.touch = 1
                    monstre.PV -= self.ATK
                    try:
                        liste_projectiles.list_projectiles1.remove(self)
                    except ValueError:
                        pass

            for monstre in liste_monstres.liste_monstres4:
                if self.x  < monstre.x + 24 and self.x + 4> monstre.x -1 and self.y  < monstre.y + 24 and self.y + 3 > monstre.y -1:
                    monstre.touch = 1
                    monstre.PV -= self.ATK
                    try:
                        liste_projectiles.list_projectiles1.remove(self)
                    except ValueError:
                        pass
            for monstre in liste_monstres.liste_monstres5:
                if self.x  < monstre.x + 24 and self.x + 4 > monstre.x -1 and self.y  < monstre.y + 24 and self.y + 3 > monstre.y -1:
                    monstre.touch = 1
                    if randint(1,100)<=joueur1.taux_crit:
                        monstre.PV -= self.ATK*2
                        print("crit")
                    else:
                        monstre.PV -= self.ATK
                    try:
                        liste_projectiles.list_projectiles1.remove(self)
                    except ValueError:
                        pass

            self.progression += 2


        if type == 2:
            chemin = ligne(self.xy,self.target)
            self.x = chemin[3][0]
            self.y = chemin[3][1]
            self.xy = [self.x,self.y]

            if self.x  < joueur1.x +16 and self.x + 4 > joueur1.x -1 and self.y  < joueur1.y +16 and self.y + 3> joueur1.y -1:
                joueur1.touch = True
                joueur1.PV -= 5
                liste_projectiles.list_projectiles2.remove(self)
               
            self.progression += 3

        if type == 3:
            chemin = ligne(self.xy,self.target)
            self.x = chemin[8][0]
            self.y = chemin[8][1]
            self.xy = [self.x,self.y]

            if self.x  < joueur1.x +16 and self.x + 4> joueur1.x -1 and self.y  < joueur1.y +16 and self.y + 3> joueur1.y -1:
                joueur1.touch = True
                joueur1.PV -= 5
                liste_projectiles.list_projectiles3.remove(self)
                

            self.progression += 8

        if type == 4:
            chemin = ligne(self.xy,self.target)
            self.x = chemin[7][0]
            self.y = chemin[7][1]
            self.xy = [self.x,self.y]

            if self.x  < joueur1.x +16 and self.x  + 4> joueur1.x -1 and self.y  < joueur1.y +16 and self.y  + 3> joueur1.y -1:
                joueur1.touch = True
                joueur1.PV -= 5
                liste_projectiles.list_projectiles4.remove(self)
                

            self.progression += 7

class ListeProjectiles :
    def __init__(self):
        self.list_projectiles1 = []
        self.list_projectiles2 = []
        self.list_projectiles3 = []
        self.list_projectiles4 = []

    def mouvement_liste_projectiles(self) :
        for projectiles in self.list_projectiles1 :
            if p.frame_count % 2 == 0:
                if projectiles.progression>80:
                    self.list_projectiles1.remove(projectiles)
                else:
                    projectiles.mouvement_projectile(1)
        for projectiles in self.list_projectiles2 :
            if p.frame_count % 2 == 0:
                if projectiles.progression>100:
                    self.list_projectiles2.remove(projectiles)
                else:
                    projectiles.mouvement_projectile(2)
        for projectiles in self.list_projectiles3 :
            if p.frame_count % 2 == 0:
                if projectiles.progression>200:
                    self.list_projectiles3.remove(projectiles)
                else:
                    projectiles.mouvement_projectile(3)
        for projectiles in self.list_projectiles4 :
            if p.frame_count % 3 == 0:
                if projectiles.progression>100:
                    self.list_projectiles4.remove(projectiles)
                else:
                    projectiles.mouvement_projectile(4)


class Spawn:
    def __init__(self):
        self.x=randint(0,250)
        self.y=randint(0,250)
        self.xy=(self.x,self.y)



class Liste_Spawn:
    def __init__(self):
        self.spawnlist=[]
        nb=randint(1,3) #nb de mobs a spawn
        for _ in range(nb):
            self.spawnlist.append(Spawn())

    def update(self):
        self.spawnlist=[]
        nb=randint(1,3) #nb de mobs a spawn
        for _ in range(nb):
            self.spawnlist.append(Spawn())

class Loot:
    
    def __init__(self,type,pos:tuple,spawntime):
        if type>=0 and type<=9:
            self.type="   ATK"
        if type>=10 and type<=20:
            self.type="    HP"
        if type>=21 and type<=31:
            self.type="   tir"
        if type>=32 and type<=42:
            self.type=" sangsue"
        if type>=43 and type<=53:
            self.type="   Spd"
        if type>=54 and type<=64:
            self.type="  luck"
        if type>=65 and type<=75:
            self.type="   def"
        if type>=76 and type<=86:
            self.type="  crit"
        if type>=87 and type<=97:
            self.type=" SPD proj"
        if type>=98 and type<=100:
            self.type="   1UP"
        self.pos=pos
        self.spawntime=spawntime
    
    
class ListeLoot:
    def __init__(self):
        self.liste_loot=[]
    
    def lootCheck(self,pos):
        random=randint(0,100)+joueur1.luck
        if random>=90:
            self.liste_loot.append(Loot(randint(0,100),pos,pyxel.frame_count))
            
def ligneZ(depart,arrivee,taille=60):
    
    
    taille=60 #modifier la distance des projectiles ici!
    x1=depart[0]
    x2=arrivee[0]
    y1=depart[1]
    y2=arrivee[1]
    try:
        coef=(y2-y1)/(x2-x1)
    except ZeroDivisionError:
            coef= None
    if x2>x1 and coef!=None:
        origine=y1-coef*x1
        x2,y2=x2*3, coef*x2*3+origine
    elif x2<x1 and coef!=None:
        origine=y1-coef*x1
        x2,y2= (-1*x2)*3, coef*(x2*-1)*3+origine
    if coef is None and y2<y1:
        y2/=10
    if coef is None and y2>y1:
        y2*=2
   
    points = []
    a=[x1,y1]
    vecteur=(x2-x1,y2-y1)
    distance=(vecteur[0]**2+vecteur[1]**2)**0.5
    try:
        normal=(vecteur[0]/distance,vecteur[1]/distance)
    except ZeroDivisionError:
        normal=(vecteur[0]/1,vecteur[1]/1)
    for _ in range(taille):
        points.append((int(a[0]),int(a[1]))) 
        a[0]+=normal[0]
        a[1]+=normal[1]
 
    return points

def ligne(depart,arrivee,taille=60):

    #modifier la distance des projectiles ici!
    x1=depart[0]
    x2=arrivee[0]
    y1=depart[1]
    y2=arrivee[1]
    points = []
    a=[x1,y1]
    vecteur=(x2-x1,y2-y1)
    distance=(vecteur[0]**2+vecteur[1]**2)**0.5
    try:
        normal=(vecteur[0]/distance,vecteur[1]/distance)
    except ZeroDivisionError:
        normal=(vecteur[0]/1,vecteur[1]/1)
    for _ in range(taille):
        points.append((int(a[0]),int(a[1])))
        a[0]+=normal[0]
        a[1]+=normal[1]

    return points

def ligne2(depart,arrivee):
    x1=depart[0]
    x2=arrivee[0]
    y1=depart[1]
    y2=arrivee[1]
    points = []
    distance_x = abs(x2 - x1)
    distance_y = abs(y2 - y1)
    signe_x = 1 if x1 < x2 else -1
    signe_y = 1 if y1 < y2 else -1
    coef = distance_x - distance_y
    while x1 != x2 or y1 != y2:
        points.append((x1, y1))
        coef2 = 2 * coef
        if coef2 > -distance_y:
            coef -= distance_y
            x1 += signe_x
        if coef2 < distance_x:
            coef += distance_x
            y1 += signe_y
    points.append((x2, y2))
    return points







liste_projectiles= ListeProjectiles()
liste_monstres = ListeMonstres()
joueur1 = Joueur(100,10)
spawnlist=Liste_Spawn()
listeloot=ListeLoot()
Jeu()