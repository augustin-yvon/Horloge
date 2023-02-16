from time import *
import time

def horloge(h,m,s):
    zero = '0'
    h = int(h)
    m = int(m)
    s = int(s)
    if s == 59:
        s = '00'
        m += 1
        if m == 60:
            m = '00'
            h += 1
            if h == 24:
                h = '00'
                return h,m,s
            elif 1 <= h < 9:
                zero += str(h)
                h = zero
                return h,m,s
            else:
                return h,m,s
        elif 1 <= m < 9:
            if h == 0:
                h = '00'
            zero += str(m)
            m = zero
            return h,m,s
        else:
            return h,m,s

    elif 1 <= s < 9:
            s += 1
            if m == 0:
                m = '00'
            elif 1 <= m < 9:
                zero += str(m)
                m = zero

            if h == 0:
                h = '00'
            elif 1 <= h < 9:
                zero += str(h)
                h = zero
            zero = '0'

            zero += str(s)
            s = zero
            return h,m,s

    else:
        s += 1
        if 1 <= s < 9:
            if m == 0:
                m = '00'
            elif 1 <= m < 9:
                zero += str(m)
                m = zero

            if h == 0:
                h = '00'
            elif 1 <= h < 9:
                zero += str(h)
                h = zero
            zero = '0'

            zero += str(s)
            s = zero
            return h,m,s

        else:
            if m == 0:
                m = '00'
            elif 1 <= m < 9:
                zero += str(m)
                m = zero

            if h == 0:
                h = '00'
            elif 1 <= h < 9:
                zero += str(h)
                h = zero
            return h,m,s


def regler_heure(h,m,s):
    if 0 <= int(h) < 24 and 0 <= int(m) < 60 and 0 <= int(s) < 60:
        result = str(h) + ':' + str(m) + ':' + str(s)
        print(result)
        x = 0
        while 1:  
            try:
                x += 1
                h,m,s = horloge(h,m,s)
                result = str(h) + ':' + str(m) + ':' + str(s)
                print(result)
                time.sleep(1)

            except KeyboardInterrupt:
                print ('Stopped at:'), x
                break
    else:
        print('erreur heure')
        h,m,s = '','',''
        heure = input("Tapez l'heure sous la forme hhmmss : ")
        for i in range(len(heure)):
            if 0 <= i < 2:
                h += heure[i]
            if 2 <= i < 4:
                m += heure[i]
            if 4 <= i < 6:
                s += heure[i]
        regler_heure(h,m,s)


def regler_alarme(h,m,s):
    if 0 <= int(h) < 24 and 0 <= int(m) < 60 and 0 <= int(s) < 60:
        ha,ma,sa = h,m,s
        h,m,s = strftime("%H"),strftime("%M"),strftime("%S")
        s = str(int(s) - 1)
        h,m,s = horloge(h,m,s)
        result = str(h) + ':' + str(m) + ':' + str(s)
        print(result)
        x = 0
        while 1:  
            try:
                x += 1
                h,m,s = horloge(h,m,s)
                result = str(h) + ':' + str(m) + ':' + str(s)
                print(result)
                if h == int(ha) and m == int(ma) and s == int(sa):
                    print(result, "Alarme")
                else:
                    print(result)
                time.sleep(1)

            except KeyboardInterrupt:
                print ('Stopped at:'), x
                break
    else:
        print('erreur alarme')
        h,m,s = '','',''
        alarme = input("Tapez l'alarme sous la forme hhmmss : ")
        for i in range(len(alarme)):
            if 0 <= i < 2:
                h += alarme[i]
            if 2 <= i < 4:
                m += alarme[i]
            if 4 <= i < 6:
                s += alarme[i]
        regler_alarme(h,m,s)


def regler_alarme_heure(h,m,s,ha,ma,sa):
    if 0 <= int(h) < 24 and 0 <= int(m) < 60 and 0 <= int(s) < 60 and 0 <= int(ha) < 24 and 0 <= int(ma) < 60 and 0 <= int(sa) < 60:
        result = str(h) + ':' + str(m) + ':' + str(s)
        print(result)
        x = 0
        t = 0
        while 1:  
            try:
                x += 1
                h,m,s = horloge(h,m,s)
                result = str(h) + ':' + str(m) + ':' + str(s)
                if h == int(ha) and m == int(ma) and s == int(sa):
                    print(result, "Alarme")
                else:
                    print(result)
                time.sleep(1)

            except KeyboardInterrupt:
                print ('Stopped at:'), x
                break
    else:
        print('erreur heure et/ou alarme')
        h,m,s = '','',''
        ha,ma,sa = '','',''
        heure = input("Tapez l'heure sous la forme hhmmss : ")
        alarme = input("Tapez l'alarme sous la forme hhmmss : ")
        for i in range(len(alarme)):
            if 0 <= i < 2:
                ha += alarme[i]
            if 2 <= i < 4:
                ma += alarme[i]
            if 4 <= i < 6:
                sa +=  alarme[i]
        for i in range(len(heure)):
            if 0 <= i < 2:
                h += heure[i]
            if 2 <= i < 4:
                m += heure[i]
            if 4 <= i < 6:
                s += heure[i]
        regler_alarme_heure(h,m,s,ha,ma,sa)


def main(choix):
    if choix == '1':
        h,m,s = strftime("%H"),strftime("%M"),strftime("%S")
        s = str(int(s) - 1)
        h,m,s = horloge(h,m,s)
        result = str(h) + ':' + str(m) + ':' + str(s)
        print(result)
        x = 0
        while 1:  
            try:
                x += 1
                h,m,s = horloge(h,m,s)
                result = str(h) + ':' + str(m) + ':' + str(s)
                print(result)
                time.sleep(1)

            except KeyboardInterrupt:
                print ('Stopped at:'), x
                break

    if choix == '2':
        h,m,s = '','',''
        heure = input("Tapez l'heure sous la forme hhmmss : ")
        for i in range(len(heure)):
            if 0 <= i < 2:
                h += heure[i]
            if 2 <= i < 4:
                m += heure[i]
            if 4 <= i < 6:
                s += alarme[i]
        regler_heure(h,m,s)

    if choix == '3':
        h,m,s = '','',''
        alarme = input("Tapez l'alarme sous la forme hhmmss : ")
        for i in range(len(alarme)):
            if 0 <= i < 2:
                h += alarme[i]
            if 2 <= i < 4:
                m += alarme[i]
            if 4 <= i < 6:
                s += alarme[i]
        regler_alarme(h,m,s)
    
    if choix == '4':
        h,m,s = '','',''
        ha,ma,sa = '','',''
        heure = input("Tapez l'heure sous la forme hhmmss : ")
        alarme = input("Tapez l'alarme sous la forme hhmmss : ")
        for i in range(len(alarme)):
            if 0 <= i < 2:
                ha += alarme[i]
            if 2 <= i < 4:
                ma += alarme[i]
            if 4 <= i < 6:
                sa += alarme[i]
        for j in range(len(heure)):
            if 0 <= j < 2:
                h += heure[j]
            if 2 <= j < 4:
                m += heure[j]
            if 4 <= j < 6:
                s += heure[j]
        regler_alarme_heure(h,m,s,ha,ma,sa)


print(" \nBienvenue dans l'horloge,\n Pour afficher l'heure tapez 1\n Pour régler l'heure tapez 2\n Pour régler une alarme tapez 3\n Pour régler l'heure et une alarme tapez 4\n Faîtes Ctrl+C pour quitter\n ")
choix = input("Votre choix : ")
print('')
print(main(choix))