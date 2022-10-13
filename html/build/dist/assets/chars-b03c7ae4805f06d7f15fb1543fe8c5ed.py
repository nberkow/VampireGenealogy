
import xml.etree.cElementTree as ET


def get_text_blocks():

    characters = 'abcdefghijklmnopqrstu'
    path = "/mnt/c/Users/Narthan/Projects/assets/letters"
    blocks = []

    for c in characters:
        block = ''
        record = False
        with open(f"{path}/{c}.svg") as xml:
            for xline in xml:
                if '<g' in xline:
                    block += xline
                    if record:
                        record = False
                    else:
                        record = True
                elif record:
                    block += xline
            blocks.append(block)
    return(blocks)


    

if __name__ == "__main__":
    print(get_text_blocks())
