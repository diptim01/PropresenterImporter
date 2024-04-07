from docx import Document
import re


def remove_special_characters(text):
    # Define a pattern to match the characters you want to remove
    pattern = r'[?*"]'
    # Use the sub() function to replace any matched character with an empty string
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


document = Document(".\data\SONGS_LYRICS2.docx")

songtitle = ''
song_aggregate = []
isFirstRun = True

for (idx, paragraph) in enumerate(document.paragraphs):
    if paragraph.style.name == 'Heading 1':
        if(isFirstRun is False):
            if(song_aggregate[-1:] == [' ']):
                song_aggregate.pop()

            songtitle = remove_special_characters(songtitle)
            songLyrics = str1 = '\n'.join(str(e) for e in song_aggregate)
            file_path = f".\data\ProExportedSongs\{songtitle}.pro"

            # Open the file in write mode and write the string to it
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(songLyrics)
                print(f"song title:- {paragraph.text} saved successfully!!")
            

        #reset the title and song
        songtitle = ''
        song_aggregate = []
        songtitle = paragraph.text.strip()
        print(f"song title:- {paragraph.text}")
        isFirstRun = False
        # if(paragraph.text.strip() == 'Praise Chant'):
        #     break
        continue
    
    isEmptyLine = (len(paragraph.text.strip()) == 0) 
    # if isEmptyLine:
    #     print("boooooooooooooooo")


    if(song_aggregate[-1:] != [' '] and isEmptyLine is False):
        song_aggregate.append(paragraph.text.strip())
    

    if(song_aggregate[-1:] == [' '] and isEmptyLine is False):
        song_aggregate.append(paragraph.text.strip())

    if(len(song_aggregate) > 0 and song_aggregate[-1:] != [' '] and isEmptyLine):
        song_aggregate.append(' ')
    
    # if(paragraph.text != ''):
    #     message = paragraph.text.strip()
    #     print(paragraph.text.strip())

    # if(paragraph.text.strip() == 'Praise Chant'):
    #     break


print('songs completed successfully!')


# for index, item in enumerate(song_aggregate): 
#     print (item, " at index ", index)

# str1 = '\n'.join(str(e) for e in song_aggregate)
# print(str1)

