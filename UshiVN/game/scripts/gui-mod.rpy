###############
# This file contains misc. settings from the Hellhound VN that are reused
###############

image black = Solid((0, 0, 0, 255))


######
# Characters
######

#Unknown speaker
define un = Character('???', what_prefix='"', what_suffix='"')

#FemMC
define f = Character('FemMC', color="#B72743", image="FemMC", what_prefix='"', what_suffix='"')

#The MC
#As his inner thoughts will be handled by the narrator we need to add quotes
define mc = Character("MC", color="#4b55b7", what_prefix='"', what_suffix='"')


#####
# Things that require an init
#####

init:
    define dis = Dissolve(0.2)

    $ circirisout = ImageDissolve("images/backgrounds/circleiris.png", 1.5, 8)
    $ circirisin = ImageDissolve("images/backgrounds/circleiris.png", 1.5, 8, reverse=True)

    image rain:
        "images/backgrounds/rain.png"
        0.033334
        "images/backgrounds/rain2.png"
        0.033334
        "images/backgrounds/rain3.png"
        0.033334
        "images/backgrounds/rain4.png"
        0.033334
        "images/backgrounds/rain5.png"
        0.033334
        "images/backgrounds/rain6.png"
        0.033334

        "images/backgrounds/rain4.png"
        0.033334
        "images/backgrounds/rain2.png"
        0.033334
        "images/backgrounds/rain.png"
        0.033334
        "images/backgrounds/rain4.png"
        0.033334
        "images/backgrounds/rain3.png"
        0.033334
        "images/backgrounds/rain6.png"
        0.033334
        repeat

    #Defines the Vignette toggle for later
    if persistent.vignette is None:
        $ persistent.vignette = True

    #Defines the flash effect for use during climaxes
    $ flash = Fade(.25, 0, .75, color="#fff")