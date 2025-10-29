lyrics = """
[Intro]
Desert you
Ooh-ooh-ooh-ooh
Hurt you

[Verse 1]
We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Verse 2]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
And if you ask me how I'm feeling
Don't tell me you're too blind to see

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Bridge]
Ooh (Give you up)
Ooh-ooh (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
[Verse 3]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""

# task 1 - never gonna count
print(lyrics.lower().count("never gonna"))

# task 2 - remove section separators
lyrics = lyrics.replace("[Intro]", "")
lyrics = lyrics.replace("[Verse 1]", "")
lyrics = lyrics.replace("[Pre-Chorus]", "")
lyrics = lyrics.replace("[Chorus]", "")
lyrics = lyrics.replace("[Verse 2]", "")
lyrics = lyrics.replace("[Bridge]", "")
lyrics = lyrics.replace("[Verse 3]", "")
lyrics = lyrics.replace("\n\n\n", "\n")
lyrics = lyrics.replace("\n\n", "\n")
lyrics = lyrics.strip()
print(lyrics)

# task 3 - lines count
lines = lyrics.split("\n")
print(len(lines))

# task 4 - alphabet count
total_alphabets = 0
for character in lyrics:
    if character.isalpha():
        total_alphabets += 1
print(total_alphabets)
