import cv2
import pytesseract
import os
import Levenshtein
import numpy as np

#Levenshtein.distance() gives Levenshtein distance between two strings, 0 means the strings are exactly the same, higher means they are not alike

levenshiten_distance_all = {}

# nxn kernal of 1s
img = cv2.imread("/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
actual_output = """POSITION OF WOMEN 31

lady must have her devoted knight or minstrel-her
lover, in fact, who could not and must not be her
husband; and every man who aspired to be courteous
must have his mistress.

"There are," says a Troubadour, "four degrees in Love:
the first is hesitancy, the second is suppliancy, the third is
acceptance, and the fourth is friendship. He who would love
a lady and goes to court her, but does not venture on address-
ing her, is in the stage of Hesitancy. But if a lady gives
him any encouragement, and he ventures to tell her of his
pains, then he has advanced to the stage of Suppliant. And
if, after speaking to his lady and praying her, she retains him
as her knight, by the gift of ribbons, globes, or girdle, then he
enters on the grade of Acceptance. And if, finally, it pleases
the lady to accord to her loyal accepted lover so much as a
kiss, then she has elevated him to Friendship."

In the life of a knight the contracting of such
an union was a most solumn moment. The cere-
mony by which it was sealed was formulated on that
in which a vassal takes oath of fealty to a sovereign.
Kneeling before the lady, with his hands joined
between hers, the knight devoted himself and all his
powers to her, swore to serve her faithfully to death,
and to defend her to the utmost of his power from
harm and insult. The lady, on her side, accepted these
services, promised in return the tenderest affections of
her heart, put a gold ring on his finger as pledge of
union, and then raising him gave him a kiss, always the
first, and often the only one he was to receive from her.
An incident in the Provençal romance of Gerard de
Roussillon shows us just what were the ideas prevalent
as to marriage and love at this time. Gerard was
deperately in love with a lady, but sh was moved by"""

i = 1
while i < 11:
    kernel = np.ones((i, i), np.uint8)
    open = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    output_file_name = "/Users/veersingh/Desktop/Internship/data-extraction/noise_reduction_testing/opening_testing/image_outputs/out_" + str(i) + ".jpg"
    cv2.imwrite(output_file_name, open)
    i = i + 1

images_directory = "/Users/veersingh/Desktop/Internship/data-extraction/noise_reduction_testing/opening_testing/image_outputs"
for filename in os.listdir(images_directory):
    if filename.endswith(".jpg"):
        image_path = images_directory + '/' + filename
        img = cv2.imread(image_path)

        ocr_output = pytesseract.image_to_string(img)
        levenshtein_distance = Levenshtein.distance(actual_output,ocr_output)
        levenshiten_distance_all.update({filename : levenshtein_distance})

print(levenshiten_distance_all)
best = min(levenshiten_distance_all, key=levenshiten_distance_all.get)
print("Highest Accuracy - " + best)

