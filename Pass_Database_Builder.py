import anydbm
import pickle
import os

def build():
    DataFile = open("Pass_Database.bin", "wb+")

    pass_dict = {
                "bses" : ("151344894", "lionheart"),
                "dominos" : ("9911349196", "Lionheart96"),
                "dropbox" : ("mansimarsingh.bhatia@gmail.com", "strongbox1234"),
                "steam" : ("Drake_Ramor", "whatarethey150696"),
                "uplay" : ("Drake_Ramor", "lionheart96"),
                "ncfm" : ("MansimarBhatia", "Lionheart_96"),
                "irctc" : ("MS_Bhatia", "rail1234"),
                "relishsports" : ("mansimarsingh.bhatia@gmail.com", "guns1234567890"),
                "investing.com" : ("mansimarsingh.bhatia@gmail.com", "sherdil1234")


                }

    dump = pickle.dumps(pass_dict)

    DataFile.write(dump)





    DataFile.close()


def main():



    while True:
        print "\n\nOptions : view/exit"
        u_input = raw_input("Enter choice : ")


        if u_input == "view":

            DataFile = open("Pass_Database.txt", "r")

            dict_form = pickle.loads(DataFile.read())
            print dict_form
            service_name = raw_input("Enter Service Name : ")

            if service_name not in dict_form.keys():

                print "Invalid Sercice Name, Enter Again"
                continue

            print "\n\nLogin : ", dict_form[service_name][0]
            print "Pass : ", dict_form[service_name][1]


        elif u_input == "exit":
            print "Thanks for using Pass Manager!"
            break




build()
