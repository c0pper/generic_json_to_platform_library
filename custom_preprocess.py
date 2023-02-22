import re
from typing import Union


def custom_prep(text: Union[str, bytes]):
    # Remove the 'b"' at the start of the 4th element and '"' at the end of the 4th element
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    else:
        text = text.replace("b'", "").replace('b"', "")
    # Remove URLs from the 4th element
    text = re.sub(r'http\S+', '', text)
    text = text.replace(r"\xe2\x80\x94", "-")
    text = text.replace(r"\xe2\x80\x99", "'")
    text = text.replace(r"\xe2\x80\xa6", " ...")
    text = text.replace(r"\xe2\x80\x98", "'")
    text = text.replace(r"\xe2\x80\x93", "-")
    text = text.replace(r"\xe2\x80\x9c", "'")
    text = text.replace(r"\xe2\x80\x9d", "'")
    text = text.replace("&gt", ">")
    text = text.replace("&lt", "<")
    text = re.sub(r'\\n+', '.\n', text)
    text = re.sub(r'\\x.+(\\x.+)+', '', text)

    text = re.sub(r'x..x..(x..)?', '', text)



    # Convert the 4th element from Unicode to utf-8
    # text = text.encode('utf-8')

    return text
#
# ls = ["b""@TreadLightly_RE @wisemindmoney We've had the hottest summer on record and everyone hates it. We've had wildfires a\xe2\x80\xa6 https://t.co/4gJ6L1Evxj""",
# b'@MichaelJFell @NYGovCuomo @realDonaldTrump Gov -when Trump is reelected in Nov. your ass is out of here. Ever heard\xe2\x80\xa6 https://t.co/P1xtsRCSv3',
# "b'""Pueyo\xe2\x80\x99s accessible blog post spread like wildfire. Worldometer charts allowed people to naively compare their prog\xe2\x80\xa6 https://t.co/fpXi3D6cYF'",
# b'@MissLanaMadison Too bad about the wildfire smoke...',
#       '"b""Wildfire smoke will continue to impact Reno/Sparks with a similar pattern to today\'s. Expect Unhealthy for Sensitiv\xe2\x80\xa6 https://t.co/YaUcdL2sww"""']
# for i in ls:
#     print(custom_prep(i))
