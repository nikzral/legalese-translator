`#Welcome to my 'legalese' converter!
#If you do end up using this in one of your projects, please make it clear that you took that portion from me!
#The only thing we import here is a automatic grammar corrector
from auto_corrector import correct

#ASCII art classes
#This defines the color of the text that makes up that huge 'Legalese Translator' graphic, and the text colors for the project!
class legalset:
  ASCII = '\033[93m'
  DEFINITION = '\033[94m'
  FINAL = '\033[95m'

#ASCII art
#This prints the text that makes up that huge 'Legalese Translator' graphic!
print(legalset.ASCII + """\

Nik Zral's

   __                  _                  _____                     _       _             
  / /  ___  __ _  __ _| | ___  ___  ___  /__   \_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
 / /  / _ \/ _` |/ _` | |/ _ \/ __|/ _ \   / /\/ '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
/ /__|  __/ (_| | (_| | |  __/\__ \  __/  / /  | | | (_| | | | \__ \ | (_| | || (_) | |   
\____/\___|\__, |\__,_|_|\___||___/\___|  \/   |_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   
           |___/                                                                          

                    """)


#This is the definiton of 'legalese'
print("What is legalese?")
print(legalset.DEFINITION + "le·gal·ese")
print("/ˌlēɡəˈlēz/")
print("noun, INFORMAL")
print("The formal and technical language of legal documents that is often hard to understand.")
print("-")
print(legalset.ASCII + "What does this do?")
print(legalset.DEFINITION + "This translator will change your normal english to the aforementioned 'legalese'. Just simply type or paste your text into the input below and it will come out 'legalized'!")

#This is the main and only input for the translator
input1 = input("Type in here the text that you would like converted to 'legalese': ")

#This is where the magic happens! This part will covert your words from common english to court-ready legalese jargon
legalinput = (input1.replace("many", "a large number of").replace("lots of", "a large number of").replace("some", "a number of").replace("several", "a number of").replace("many", "a number of").replace("give", "accord").replace("gave", "accorded").replace("respect", "accord respect to").replace("get", "aquire").replace("more", "additional").replace("also", "additionally").replace("next", "adjacent").replace("near", "adjacent").replace("advert to", "mention").replace("given", "afforded").replace("previously mentioned", "aforementioned").replace("scope", "ambit").replace("reach", "ambit").replace("amid", "amidst").replace("among", "amongst").replace("about", "appoximatley").replace("determine", "ascertain").replace("find out", "ascertain").replace("info", "information").replace("help", "assist").replace("now", "at present").replace("help", "assist").replace("where", "at the loaction").replace("try", "attempt").replace("because", "because of the fact that").replace("stop", "cease").replace("knows that", "is cognizant that").replace("start", "commence").replace("hide", "conceal").replace("about", "concerning").replace("decided", "came to the conclusion").replace("result", "consequence").replace("show", "demonstrate").replace("do", "demonstrate").replace("doing", "demonstrating").replace("want", "desire").replace("wanted", "desired").replace("although", "despite the fact that").replace("dosent", "does not operate to").replace("dosen't", "does not operate to").replace("does not", "does not operate to").replace("level", "echelon").replace("during", "during the course of").replace("does not", "does not operate to").replace("law", "provision of law").replace("buy", "purchase"))









#This deploys the 'auto_corrector' module and will correct grammar and spelling
legallycorrect = correct(legalinput)

#This tells the user how to export their newly legalized text!
print("To export your 'legalese', just copy the below text to your clipboard!")
print("---------------------------")

#And finally, this prints our output!
print(legalset.FINAL + legallycorrect)

