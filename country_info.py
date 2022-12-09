from fpdf import FPDF
from msvcrt import getch
from countryinfo import CountryInfo
from os import system
import os


class Collect_country_information():
    """ Collect any contry information with online """

    def __init__(self):
        """ Intialization """
        self.setup()
        self.input_info()

    def setup(self):
        ''' This funtion setup all the file and folders or a requirement to run this funtion '''
        
        ls=os.listdir()
        current_location=os.getcwd() 
        if 'File' in ls:
            os.chdir("File")
            ls1=os.listdir()
            if 'Text' not in   ls1:
                os.mkdir("Text")
            if 'Pdf' not in   ls1:
                os.mkdir("Pdf")
            os.chdir( current_location)
        else:
            os.mkdir("File")
            os.chdir("File")
            ls1=os.listdir()
            if 'Text'  not in   ls1:
                os.mkdir("Text")
            if 'Pdf' not in   ls1:
                os.mkdir("Pdf")
            os.chdir( current_location )


    def input_info(self):
        system("cls")
        country_name = input("\n\t\t Enter the Country name ----> ")
        try:
            country = CountryInfo(country_name)
            self.processing_info(country)
        except:
            print(
                "\n\t\t <----- Country name is not matched or internet not worked -----> ")
            print(
                "\t\t <----- Error Occured Please Reenter the name of the country -----> ")
            print("\t\t <----- Press any key to Reinput -----> ")
            getch()
            self.input_info()

    def processing_info(self, country):

        # introduction
        self.name = country.name()
        self.native_name = country.native_name()
        self.alternative_name = country.alt_spellings()
        self.Area = country.area()
        self.language = country.languages()
        self.currency = country.currencies()
        self.democracy = country.demonym()
        self.capital = country.capital()

        # Features
        self.location_country = country.latlng()
        self.population = country.population()
        self.phone_code = country.calling_codes()
        self.top_domain = country.tld()
        self.capital_location = country.capital_latlng()
        self.region = country.region()
        self.sub_region = country.subregion()
        self.time_zone = country.timezones()
        self.borders = country.borders()
        self.provinces = country.provinces()
        self.iso_code = country.iso()
        self.translaition = country.translations()
        self.wikipedia_link = country.wiki()

        self.basic()

    def convert_list_to_list(self, list):
        str = ""
        for element in list:
            if element == list[-1]:
                str = str+element
            else:
                str = element+","+str

        return str

    def convert_dic_to_string(self, dict):
        str = ""
        for var, key in dict.items():
            first = var
            str = " "+f"{var} :- {key}" + str
            break

        for var, key in dict.items():
            if var != first:
                str = " "+f"{var} :- {key}" + "," + str
        return str

    def basic(self):
        system("cls")
        print("\n\t <----- All The Information based on Wikipedia -----> ")
        print("\t\t <----   Basic Information ----> ")

        print(f"\t\t Country Name     ----> {self.name}")
        print(f"\t\t Native Name      ----> {self.native_name}")
        print(
            f"\t\t Alternative Name ----> {self.convert_list_to_list(self.alternative_name)}")
        print(
            f"\t\t Location Country ----> {self.location_country[0]} lati, {self.location_country[1]} longitude")
        print(f"\t\t Capital City     ----> {self.capital}")
        print(f"\t\t Total Population ----> {self.population}")
        print(
            f"\t\t Language  Spoken ----> {self.convert_list_to_list(self.language)}")
        print(
            f"\t\t Currency         ----> {self.convert_list_to_list(self.currency)}")
        print(f"\t\t Total Area       ----> {self.Area} sq.km ")
        print(f"\t\t Nationality      ----> {self.democracy}")
        # time zone
        print(
            f"\t\t Time zone        ----> {self.convert_list_to_list(self.time_zone)} ")
        print(f"\t\t wikipedia link   ----> {self.wikipedia_link}")

        self.menu()

    def menu(self):
        """ Navigation bar for to asked input """
        while(True):

            print(
                "\n\t 1.Another Country    2.Full Details   5.Save     10.Source of Information     99.Exit ")
            ch = int(input())

            if ch == 1:
                self.input_info()
            elif ch == 2:
                self.full_details()
            elif ch == 5:
                self.save_info()
            elif ch == 10:
                print(
                    "\n\t\t <-----  All the Inforamtion are based on the Wikipedia information ----> ")
                getch()
            elif ch == 99:
                print(f"\n\t\t <---- Thanks for using our program ----> ")
                system("exit")

            else:
                print("\n\t\t Invalid options ")

    def save_info(self):
        """ Save the information of country in file or pdf """

        print("\t\t  a. Text File      b. PDF File ")
        cha = input()
        try:
            if cha == "a":
               
                        

                filename = input("\t\t Enter File name ----> ")
                filename = "File/Text/"+filename+".txt"
                # print(filename)
                print("\t\t i) Basic Information         ii) Full Information ")
                chaa = input()
                if chaa == 'i':

                    with open(filename, "wb") as file:
                        file.write(self.return_basic())
                        print(f"\n\t\t Sucessfully save to {filename}")
                    file.close()

                elif chaa == "ii":

                    with open(filename, "wb") as file:
                        file.write(self.return_full_details())
                        print(f"\n\t\t Sucessfully save to {filename}")
                    file.close()

                else:
                    print("\n\t\t <---- Invalid Options ----> ")
                    getch()
                    system("cls")
                    self.save_info()

            elif cha == "b":
                # Pdb file
                
                        
                filename = input("\t\t Enter File name ----> ")
                filename = "File/Pdf/"+filename+".pdf"
                print("\t\t i) Basic Information         ii) Full Information ")
                chaa = input()
                if chaa == 'i':
                    # basic pdf
                    pdf = FPDF()
                    # Add a page
                    pdf.add_page()
                    pdf.set_font("Helvetica", size=15)
                    # Create a cell
                    pdf.cell(
                        200, 10, txt="All The Information based on Wikipedia", ln=1, align='C')
                    pdf.cell(
                        200, 10, txt=f"Basic Information of {self.name}", ln=1, align='C')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Country name       :- {self.name}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Location Country   :- {self.location_country[0]} lati, {self.location_country[1]} longitude", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Captial City       :- {self.capital}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Population         :- {self.population} Peoples", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Democracy          :- {self.democracy}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Total Area         :- {self.Area} sq Km", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Language  Spoken :- {self.convert_list_to_list(self.language)} ", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Currency             :- {self.convert_list_to_list(self.currency)}", ln=1, align='L')
                    # pdf.cell(200,10, txt=f"\t\t\t  Time zone            :- {self.convert_list_to_list(self.time_zone)} ", ln=5, align='L' )
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Wikipedia link      :- {self.wikipedia_link}", ln=1, align='L')

                    pdf.output(filename)
                    print(
                        f"\n\t\t <---- Sucessfull Created pdf to {filename} ----> ")

                elif chaa == "ii":
                    # full details pdf
                    # basic pdf
                    pdf = FPDF()
                    # Add a page
                    pdf.add_page()
                    pdf.set_font("Helvetica", size=15)
                    # Create a cell
                    pdf.cell(
                        200, 10, txt="All The Information based on Wikipedia", ln=1, align='C')
                    pdf.cell(
                        200, 10, txt=f"Full Information of {self.name}", ln=1, align='C')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Country name       :- {self.name}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Location Country   :- {self.location_country[0]} lati, {self.location_country[1]} longitude", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Captial City       :- {self.capital}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\n\t\t  Capital City location :- {self.capital_location[0]} latitude, {self.capital_location[1]} longitude ", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Population         :- {self.population} Peoples", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Democracy          :- {self.democracy}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Total Area         :- {self.Area} sq Km", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Language  Spoken :- {self.convert_list_to_list(self.language)} ", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Currency             :- {self.convert_list_to_list(self.currency)}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\n\t\t  Phone code            :- {self.convert_list_to_list(self.phone_code)}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\n\t\t  Top Domain            :- {self.convert_list_to_list(self.top_domain)} ", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\n\t\t  ISO Code               :- {self.convert_dic_to_string(self.iso_code)}", ln=1, align='L')
                    pdf.cell(
                        200, 10, txt=f"\t\t\t  Wikipedia link      :- {self.wikipedia_link}", ln=1, align='L')

                    pdf.output(filename)
                    print(
                        f"\n\t\t <---- Sucessfull Created pdf to {filename} ----> ")

            else:
                print("\n\t\t Invalid options ")
                getch()
                system("cls")
                self.save_info()
        except:
            print("\n\t\t Error Occured ")
            getch()
            system("cls")
            self.input_info()

    def return_basic(self):
        """ Return basic information into string """
        str = "\n\t <----- All The Information based on Wikipedia -----> " +\
            f"\n\t\t <----   Basic Information {self.name} ----> " +\
            f"\n\t\t Country Name     ---->  {self.name}" + \
            f"\n\t\t Native Name      ----> {self.native_name}" +\
            f"\n\t\t Alternative Name ----> {self.convert_list_to_list(self.alternative_name)}" +\
            f"\n\t\t Location Country ----> {self.location_country[0]} lati, {self.location_country[1]} longitude" +\
            f"\n\t\t Capital City     ----> {self.capital}" +\
            f"\n\t\t Total Population ----> {self.population}" +\
            f"\n\t\t Language  Spoken ----> {self.convert_list_to_list(self.language)}" +\
            f"\n\t\t Currency         ----> {self.convert_list_to_list(self.currency)}" +\
            f"\n\t\t Total Area       ----> {self.Area} sq.km " + \
            f"\n\t\t Nationality      ----> {self.democracy} " + \
            f"\n\t\t Time zone        ----> {self.convert_list_to_list(self.time_zone)} " + \
            f"\n\t\t wikipedia link   ----> {self.wikipedia_link}"

        return str.encode("utf-8")

    def return_full_details(self):
        """ Return all the full details in encoded form """

        str = "\n\t <----- All The Information based on Wikipedia -----> " +\
            f"\n\t\t <----- Full Information of {self.name} ----> " +\
            f"\n\t\t Country Name          ----> {self.name}" +\
            f"\n\t\t Native Name           ----> {self.native_name}" +\
            f"\n\t\t Country location      ----> {self.location_country[0]} latitude, {self.location_country[1]} longitude " +\
            f"\n\t\t Alternative Name      ----> {self.convert_list_to_list(self.alternative_name)}" +\
            f"\n\t\t Location Country      ----> {self.location_country[0]} latitude, {self.location_country[1]} longitude" +\
            f"\n\t\t Capital City          ----> {self.capital}" +\
            f"\n\t\t Capital City location ----> {self.capital_location[0]} latitude, {self.capital_location[1]} longitude " +\
            f"\n\t\t Total Population      ----> {self.population}" +\
            f"\n\t\t Language Spoken       ----> {self.convert_list_to_list(self.language)}" +\
            f"\n\t\t Curreines             ----> {self.convert_list_to_list(self.currency)}" +\
            f"\n\t\t Time zone             ----> {self.convert_list_to_list(self.time_zone)} " +\
            f"\n\t\t Total Area            ----> {self.Area} sq.km " +\
            f"\n\t\t Total Provinces       ----> {self.convert_list_to_list(self.provinces)}" +\
            f"\n\t\t Total Region          ----> {self.convert_list_to_list(self.region)}" +\
            f"\n\t\t Total Sub Region      ----> {self.convert_list_to_list(self.sub_region)}" +\
            f"\n\t\t Borders               ----> {self.convert_list_to_list(self.borders)}" +\
            f"\n\t\t Nationality           ----> {self.democracy}" +\
            f"\n\t\t Phone code            ----> {self.convert_list_to_list(self.phone_code)}" +\
            f"\n\t\t Top Domain            ----> {self.convert_list_to_list(self.top_domain)} " +\
            f"\n\t\t ISO Code              ----> {self.convert_dic_to_string(self.iso_code)}" +\
            f"\n\t\t translaition          ----> {self.convert_dic_to_string(self.translaition)}" +\
            f"\n\t\t Wikipedia link        ----> {self.wikipedia_link}"

        return str.encode("utf-8")

    def full_details(self):
        """ FUll Details now """
        system("cls")
        print("\n\t <----- All The Information based on Wikipedia -----> ")
        print("\t\t <----- Full Information ----> ")

        print(f"\t\t Country Name          ----> {self.name}")
        print(f"\t\t Native Name           ----> {self.native_name}")
        print(
            f"\t\t Country location      ----> {self.location_country[0]} lati, {self.location_country[1]} longitude ")
        print(
            f"\t\t Alternative Name      ----> {self.convert_list_to_list(self.alternative_name)}")
        print(
            f"\t\t Location Country      ----> {self.location_country[0]} lati, {self.location_country[1]} longitude")
        print(f"\t\t Capital City          ----> {self.capital}")
        print(
            f"\t\t Capital City location ----> {self.capital_location[0]} lati, {self.capital_location[1]} longitude ")
        print(f"\t\t Total Population      ----> {self.population}")
        print(
            f"\t\t Language Spoken       ----> {self.convert_list_to_list(self.language)}")
        print(
            f"\t\t Curreines             ----> {self.convert_list_to_list(self.currency)}")
        print(
            f"\t\t Time zone             ----> {self.convert_list_to_list(self.time_zone)} ")
        print(f"\t\t Total Area            ----> {self.Area} sq.km ")
        print(
            f"\t\t Total Provinces       ----> {self.convert_list_to_list(self.provinces)}")
        print(
            f"\t\t Total Region          ----> {self.convert_list_to_list(self.region)}")
        print(
            f"\t\t Total Sub Region      ----> {self.convert_list_to_list(self.sub_region)}")
        print(
            f"\t\t Borders               ----> {self.convert_list_to_list(self.borders)}")
        print(f"\t\t Nationality           ----> {self.democracy}")
        print(
            f"\t\t Phone code            ----> {self.convert_list_to_list(self.phone_code)}")
        print(
            f"\t\t Top Domain            ----> {self.convert_list_to_list(self.top_domain)} ")
        print(
            f"\t\t ISO Code              ----> {self.convert_dic_to_string(self.iso_code)}")
        print(
            f"\t\t translaition          ----> {self.convert_dic_to_string(self.translaition)}")
        print(f"\t\t Wikipedia link        ----> {self.wikipedia_link}")

        getch()
        self.menu()


def main():
    cl = Collect_country_information()


if __name__ == "__main__":
    main()
