# mangaExtractor
Downloads specified manga from kissmanga.org


Run using python. For the command line arguments, provide the name of the manga (This can be anything, used to create a local directory in client machine), link (link to the specified manga, must be in the format (https://kissmanga.org/chapter/[identification of manga by the site]), starting chapter #, ending chapter #.

Ex. If I wanted to download jujutsu kaisen chapters 1 - 5
python main.py jujutsu-kaisen https://kissmanga.org/chapter/[identification of manga by the site] 1 5


May have to install a few packages before running, but there is code implemented to automatically download the packages when running the script. 

After running, code will create a local directory with the given name with a pdf for each chapter specified. 
