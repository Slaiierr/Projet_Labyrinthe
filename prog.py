vitesse_roues = 20 # vitesse pour faire des tout droit
vitesse_virage = 20 # vitesse pour faire les virages
vitesse_correction = 20 # vitesse pour faire les manips de correction

def on_forever():
    top_tout_droit = 0 # variables afin de voir si on a déjà affiché les leds en fonction de l'endroit où on veut aller, elle prend la valeur 1 si a déjà affiché les bonnes leds et 0 sinon afain de ne pas les ré allumer et gagner en réaction et en rapidité
    top_gauche = 0
    top_droite = 0
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, vitesse_roues)
        if top_tout_droit == 0:
            basic.show_leds("""
                . . # . .
                                . # . # .
                                # . # . #
                                . . # . .
                                . . # . .
            """)
            top_tout_droit = 1
            top_gauche = 0
            top_droite = 0
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, vitesse_correction)
        maqueen.motor_stop(maqueen.Motors.M2)
        if top_droite == 0:
            basic.show_leds("""
                . . # . .
                                . # . . .
                                # . # # #
                                . # . . .
                                . . # . .
            """)
            top_tout_droit = 0
            top_gauche = 0
            top_droite = 1
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
        maqueen.motor_stop(maqueen.Motors.M1)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_correction)
        if top_gauche == 0:
            basic.show_leds("""
                . . # . .
                                . . . # .
                                # # # . #
                                . . . # .
                                . . # . .
            """)
            top_tout_droit = 0
            top_gauche = 1
            top_droite = 0
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
        delay = 100 # afin d'avancer dans l'intersection et se placer au milieu
        delay_tourner = 1100 # delay durant lequel le robot va tourner afin de se placer droit et de continuer sur la prochaine ligne noire qu'il va trouver
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, vitesse_roues)
        basic.pause(delay)
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1: # tourne jusqu'à trouver du noir
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, vitesse_virage)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, vitesse_virage)
        if maqueen.ultrasonic(0) < 10: # vérifie si il n'y a pas de mur, si il y en a un -> virage à gauche (teste mur à droite)
            maqueen.motor_stop(maqueen.Motors.ALL)
            basic.pause(500)
            while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0: # tourne jusqu'à trouver du blanc
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, vitesse_virage)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_virage)
            while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1: # tourne jusqu'à trouver du noir
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, vitesse_virage)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_virage)
            if maqueen.ultrasonic(0) < 10: # vérifie si il n'y a pas de mur, si il y en a un -> virage à gauche (teste mur en face)
                maqueen.motor_stop(maqueen.Motors.ALL)
                basic.pause(500)
                while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0: # tourne jusqu'à trouver du blanc
                    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, vitesse_virage)
                    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_virage)
                while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1: # tourne jusqu'à trouver du noir
                    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, vitesse_virage)
                    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_virage)
                if maqueen.ultrasonic(0) < 10: # vérifie si il n'y a pas de mur, si il y en a un -> virage à gauche pour faire un demi-tour complet et avance afin de repartir dans la boucle lorsque les deux capteurs voient du noir (teste mur à gauche)
                    maqueen.motor_stop(maqueen.Motors.ALL)
                    basic.pause(500)
                    while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0: # tourne jusqu'à trouver du blanc
                        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, vitesse_virage)
                        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_virage)
                    while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 or maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1: # tourne jusqu'à trouver du noir
                        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, vitesse_virage)
                        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, vitesse_virage)
                    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, vitesse_roues)
                    basic.pause(delay)
                else: # si il n'y a pas de mur à droite, avance pendant le delay pour sortir de l'intersection
                    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, vitesse_roues)
                    basic.pause(delay)
            else: # si il n'y a pas de mur à droite, avance pendant le delay pour sortir de l'intersection
                maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, vitesse_roues)
                basic.pause(delay)
        else: # si il n'y a pas de mur à droite, avance pendant le delay pour sortir de l'intersection
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, vitesse_roues)
            basic.pause(delay)
basic.forever(on_forever)