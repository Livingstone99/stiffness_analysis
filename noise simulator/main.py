#SIMULATION AND STATISTICAL ANALYSIS OF
#VARIOUS NOISE SOURCES IN NIGERIA HIGHER INSTITUTION

# NSUKKA NOISE MAP AND SIMULATION OF INFLUENCES
# OF VARIOUS NOISE SOURCES.


# basically this script predicts
# and simulates the effects of various noise
# sources within nigeria higher institution.
# with some parameter, the algorithm will set out to
# bring about the transient effect of the noise sources
# generated over time


## GET AN ALGORITHM THAT RELATES THE EFFECTS OF VARIOUS NOISE SOURCES
## TO THE GENERAL NOISE SOISE OF AN AREA
from tkinter import*
root = Tk()
frame = Frame(root, height = 700, width = 1600)
frame.pack()


def Noise_Sources():
    pass
def no_of_roads(no_main_roads,no_of_perdestrain_tracks, route_engagement, no_of_minor_roads, road_noise):
    if route_engagement == 'low':
        noise_level = (no_main_roads * 10) + (no_of_perdestrain_tracks *10) + (no_of_minor_roads*5)
    elif route_engagement == 'moderate':
        noise_level = no_main_roads * 20+ (no_of_perdestrain_tracks *30)+ (no_of_minor_roads*10)
    elif route_engagement == 'high':
        noise_level = no_main_roads * 30 + (no_of_perdestrain_tracks *40)+ (no_of_minor_roads*20)
    road_noise = noise_level
    return road_noise

def business_center(no_of_generators, business_intensity, human_noise_rating):
    if business_intensity == 'high' or 'High':
        noise_buz = no_of_generators*10
    elif business_intensity == 'low' or 'Low':
        noise_buz = no_of_generators*5
    elif business_intensity == 'normal' or 'Normal':
        noise_buz = no_of_generators*8
    for i in range(10):
        if human_noise_rating == 1 or 2 or 3 or 4:
            pass
def on_going_constructions(no_of_maga_projects, time_span_mega_pro, renovation, time_span_renovation):
    pass
def human_activites(no_of_residence, popuplation_density, hawkers):
    pass
root.mainloop()