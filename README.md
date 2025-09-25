# Russian Declension 0.1
Extremely simple script, to help learn declensions of Russian Language

## Inspirationn  
Russian declension are relatively difficult, evefor a native greek speaker, the language of whom contains declensions. 
Repetition is the key, and this script is used by me  to solidify basic declension. I have been using a similar android app but the letters on the phone keyboard became to small :-)

## Usage
python3 declensions.py

## How
The script reads a csv file (here named declensions.csv) and then asks the user the correct form of a specific word.
A full list of all declension is printed if the answer is not correct.
Finally, a list of all answers is output on the screen.

## Acknowledgement
The words used were handpicked from the russian edition of wikiktionary and wikipedia.
The script was inspired by an android app named Russian Declension (from Marinokiba) 
( I have no relation with the creators of the app)
A LLM was used to make the script code look better

## Disclaimer
I have no official training and limited knowledge of the Russian Language, and therefor, no guarantees on the correctness of the
grammar - spelling in the file.

## ToDo  List
1. Use a trakcer of the errors, to focus learning on them
2. Fix bugs on the word comparison. A strip_accent function (copied from a [stack_overflow] (https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string) answer is used to remove accents, but the problem remains that there are many unicode representations for specific letters (i.e.  ё ) making comparisons difficult. A simple solution could be to parse the cvs (maybe with an iconv _to_ASCII  -> iconv _to_UTF)
3. Generalise to other languages -relatively easy, change the csv file and add-remove cases
4. Use directly wikiktionary data for declension patterns. Most tools for extracting wiktionary data do not support declension boxes yet, and too lazy to parse html (wiktionary [uses](https://en.wiktionary.org/wiki/Module:ru-noun) a [rather interesting way of generating inflections] (https://www.dfki.de/web/forschung/projekte-publikationen/publikation/10149] and the declensions are generated real time on the fly)
5. Combine a keyboard library (i like [blessed] (https://pypi.org/project/blessed/) ) with a transileration package to remove the necessity of an OS keyboard layout of the target language (like a custom keyboard layout for the application)
6. Expand functionality to combination of nouns and adjectives
7. Use wikiktionary to include example sentences for better memory retention of words
8. Use a simple GUI
   
