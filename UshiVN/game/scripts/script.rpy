# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    un "Unknown Speaker test"
    f "Female MC dialogue test"
    mc "MC dialogue test"
    "Inner Thoughts test"
    mc "This is a really long sentence to test how the game handles long sentences blah blah blah"
    
    # This ends the game.

    return
