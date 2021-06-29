import cv2
import pytesseract
import Levenshtein
import numpy as np

img = cv2.imread(
    "/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg"
)


def opening_accuracy(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    levenshiten_distance_all = {}
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
        # kernel of ones of size 1x1 upto 10x10
        kernel = np.ones((i, i), np.uint8)
        # applied opening to the image
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

        # runs ocr on this image
        ocr_output = pytesseract.image_to_string(opening)
        levenshtein_distance = Levenshtein.distance(actual_output, ocr_output)
        levenshiten_distance_all.update({i: levenshtein_distance})
        i = i + 1

    print(levenshiten_distance_all)
    best = min(levenshiten_distance_all, key=levenshiten_distance_all.get)
    print("Highest Accuracy -> " + str(best))


image = "/Users/veersingh/Desktop/Internship/data-extraction/assets/noise_red_test_img.jpg"

opening_accuracy(image)
