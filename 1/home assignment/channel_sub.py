import os
import sys
import time

class Channel():

    def __init__(self,id:int,descr:str,) -> None:
        self.channel_id = id
        self.channel_description = descr
    
    def get_channel_info(self) -> list:
        return [self.channel_description,self.channel_id]

    def update_channel_description(self,update_descr:str):
        self.channel_description += f"{update_descr}"

    def remove_channel_description(self):
        self.channel_description = ""

        return True     #for unittests' sake

class Account:

    def __init__(self,name:str) -> None:
        self.subscribed_channels = []
        self.account_name = name

    def subscribe_to_channel(self,channel):

        if channel not in self.subscribed_channels:
            self.subscribed_channels.append(channel)
            
            return True

        else:
            print(f"{self.account_name} is already subscribed to {channel}")

            return False

    def unsubscribe_to_channel(self, channel):

        if channel in self.subscribed_channels:
            self.subscribed_channels.remove(channel)

            return True

        else:
            print(f"Could not remove channel {channel} from {self.account_name}, try again.")

            return False

    def get_user_info(self):

        self.combined_info = (self.subscribed_channels,self.account_name)
        print(self.combined_info)

USR_INFO = "Naciśnij 1 aby zasubskrybować kanał\nNaciśnij 2 aby odsubskrybować kanał\nNaciśnij 3 aby dodać (dopisać) treść kanału\nNaciśnij 4 aby usunąć treść kanału\nNaciśnij 5 aby wypisać treści subskrybowanych kanałów\nNaciśnij 6 aby dodać użytkownika\nNaciśnij 7 aby dodać kanał\n"
accepted_input = [str(x) for x in range(1,8)]

accounts = {"User1":Account("User1")}
channels = {
    "TVN":Channel("TVN","jakies niebieskie"),
    "polsat":Channel("polsat","sloneczko")
}

if __name__ == "__main__":
    while True:

        try:

            print(USR_INFO)
            usr_input = input("")

            pretty_channel_list = [*channels]   #update lists everytime new loop is ran
            pretty_accounts_list= [*accounts]   

            if usr_input in accepted_input:

                if not channels and not accounts:
                    print("BRAK KANAŁÓW / UŻYTKOWNIKÓW, DODAJ ICH NAJPIERW")
                    time.sleep(1)

                else:
                    
                    if usr_input =="1":

                        print(f"Podaj ID użytkownika:\n{pretty_accounts_list}")
                        USR_ID = input(" ")
                        print(f"Podaj kanał do zasubskrybowania:\n{pretty_channel_list}")
                        CHANNEL_ID = input(" ")
                        accounts[USR_ID].subscribe_to_channel(channels[CHANNEL_ID])

                        print(f"Pomyślnie zasubskrybowano kanał {channels[CHANNEL_ID].channel_id}")
                        
                    elif usr_input == "2":

                        print(f"Podaj ID użytkownika:\n{pretty_accounts_list}")
                        USR_ID = input(" ")

                        if accounts[USR_ID].subscribed_channels:

                            print(f"Podaj kanał do odsubskrybowania:\n{accounts[USR_ID].subscribed_channels[0].channel_id}")
                            CHANNEL_ID = input(" ")
                            accounts[USR_ID].unsubscribe_to_channel(channels[CHANNEL_ID])
                            print(accounts[USR_ID].subscribed_channels)

                            print(f"Pomyślnie odsubskrybowano kanał {channels[CHANNEL_ID].channel_id}")

                        else:
                            os.system("cls")
                            print("!!! Brak treści do odsubskrybowania dla tego użytkownika. !!!")

                    elif usr_input == "3":

                        print(f"Podaj kanał, którego opis chcesz zmienić:\n{pretty_channel_list}")
                        CHANNEL_ID = input(" ")

                        if CHANNEL_ID in channels:

                            print(f"Aktualny opis to: {channels[CHANNEL_ID].channel_description}")

                            print("Dopisz opis do aktualnego: ")
                            NEW_DESCRIPTION = input("")
                            channels[CHANNEL_ID].update_channel_description(NEW_DESCRIPTION)
                        
                            print(f"\n!!!Zaktualizowano opis:!!!\n{channels[CHANNEL_ID].channel_id}:{channels[CHANNEL_ID].channel_description}")
                        
                        else:

                            os.system("cls")
                            print("!!! Błędny kanał. !!!")

                    elif usr_input == "4":

                        print(f"Podaj kanał, którego opis chcesz usunąć:\n{pretty_channel_list}")
                        CHANNEL_ID = input(" ")
                        channels[CHANNEL_ID].remove_channel_description()
                        print(f"\n!!!Usunięto opis:!!!\n{channels[CHANNEL_ID].channel_id}:{channels[CHANNEL_ID].channel_description}")

                    elif usr_input == "5":

                        print(f"Wprowadź ID użytkownika którego kanaly chcesz wypisać:\n{pretty_accounts_list} ")
                        USER_ID = input("")

                        for subscribed_channel in accounts[USER_ID].subscribed_channels:
                            print(f"Użytkownik: {USER_ID} zasubskrybował: {subscribed_channel.channel_id}:{subscribed_channel.channel_description}")

                    elif usr_input == "6":

                        print("Wprowadź ID użytkownika który chcesz utworzyć")
                        USER_ID = input("")
                        accounts[USER_ID] = Account(USER_ID)
                    
                    elif usr_input == "7":

                        print("Wprowadź ID kanału który chcesz utworzyć")
                        CHANNEL_ID = input("")
                        print(r"Chcesz stworzyć opis? Y\N")
                        user_flag = input("")

                        if user_flag == "Y":

                            print("Wprowadź opis:")
                            USER_INPUT = input("")
                            channels[CHANNEL_ID] = Channel(CHANNEL_ID,USER_INPUT)

                        elif user_flag == "N":

                            channels[CHANNEL_ID] = Channel(CHANNEL_ID,"")

                        else:

                            os.system("cls")
                            print("!!! Błędny wybór. !!!")

                        pass

            else:

                print("Zły wybór! Spróbuj ponownie.")
                time.sleep(0.5)
                os.system("cls")

            pass
        except EOFError:
            quit()
