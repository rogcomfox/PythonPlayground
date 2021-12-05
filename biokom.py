patientInfo = []
male = "Laki-Laki"
female = "Perempuan"
yes = "ya"
no = "tidak"

def checkCondition():
    # check first condition
    while True:
        firstCon = str(input("Apakah Anda Mengalami Demam? [ya/tidak]")).capitalize()
        if firstCon == yes.capitalize() or firstCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")
    
    # check second condition
    while True:
        secCon = str(input("Apakah Anda Mengalami Sesak Napas? [ya/tidak]")).capitalize()
        if secCon == yes.capitalize() or secCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")
    
    # check third condition
    while True:
        thirdCon = str(input("Apakah Anda Mengalami Batuk? [ya/tidak]")).capitalize()
        if thirdCon == yes.capitalize() or thirdCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")
    
    # check fourth condition
    while True:
        fourthCon = str(input("Apakah Anda Mengalami Nyeri Dada? [ya/tidak]")).capitalize()
        if fourthCon == yes.capitalize() or fourthCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")

    # check fifth condition
    while True:
        fifthCon = str(input("Apakah Anda Mengalami Gejala Mual Muntah? [ya/tidak]")).capitalize()
        if fifthCon == yes.capitalize() or fifthCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")
    
    # check sixth condition
    while True:
        sixthCon = str(input("Apakah Anda Mengalami Kelelahan? [ya/tidak]")).capitalize()
        if sixthCon == yes.capitalize() or sixthCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")
    
    # check seventh condition
    while True:
        sevCon = str(input("Apakah Anda Mengalami Kelenjar Getah Bening Membengkak? [ya/tidak]")).capitalize()
        if sevCon == yes.capitalize() or sevCon == no.capitalize():
            break
        else:
            print("Input salah, silahkan masukkan ya atau tidak")
    
    if firstCon == yes.capitalize() and secCon == yes.capitalize() and thirdCon == yes.capitalize() and fourthCon == yes.capitalize() and fifthCon == yes.capitalize() and sixthCon == yes.capitalize() and sevCon == yes.capitalize() :
        # check eight condition
        while True:
            eiCon = str(input("Apakah Anda Pernah Kontak Dengan Pasien Covid? [ya/tidak]")).capitalize()
            if eiCon == yes.capitalize():
                covid("iya")
                break
            elif eiCon == no.capitalize():
                covid("tidak")
                break
            else:
                print("Input salah, silahkan masukkan ya atau tidak")
    else :
        bronkitis()

def bronkitis():
    print("Nama Pasien: ", patientInfo[0])
    print("\nJenis Kelamin: ", patientInfo[1])
    print("\nPenyakit pernapasan disebabkan oleh banyak kemungkinan. Apabila Anda mengalami salah satu gejala tersebut, segera lakukan pemeriksaan ke dokter untuk pemeriksaan lebih lanjut. Apabila tidak mengalami gejala apapun, Anda sehat.")

def covid(condition):
    print("Nama Pasien: ", patientInfo[0])
    print("\nJenis Kelamin: ", patientInfo[1])
    if condition == "iya".casefold():
        print("\nAnda Diwajibkan Melakukan Swab")
    elif condition == "tidak".casefold():
        print("\nSilakan lakukan pemeriksaan ke dokter dengan melalukukan foto toraks atau dada")

if __name__ == "__main__":
    print("Selamat Datang!")
    name = str(input("Masukkan Nama Anda: ")).title()
    while True:
        gender = str(input("\nMasukkan Jenis Kelamin: ")).title()
        if gender.casefold() == male.casefold() or gender.casefold() == female.casefold():
            break
        else:
            print("\nAnda Salah Memasukkan Jenis Kelamin, Masukkan Perempuan atau Laki-Laki")
    patientInfo.append(name)
    patientInfo.append(gender)
    checkCondition()
