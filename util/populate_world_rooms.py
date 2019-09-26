from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

fun_room_title = [
    ["Forest","Cave","House","Island","Treehouse","Resturant","Castle","Dungeon","Ship","Desert","Farm","Town","Bar"],
    ["Mystery","Death","Sugar Gliders","Randomnes","Whaaaaat!!!","hip-hop","True Love","Explosions","Weapons","Candy","Elves","Trolls","Doby"]
]
fun_room_description = [
    ["It's dark in here", "It's beuitifull", "The area is dark and misty", "The area is seeping with magical power", "The area is covered in flowers"]
]


def fun_room_titles():
    title_noun = random.choice(fun_room_title[0])
    title_adj = random.choice(fun_room_title[1])
    return f'{title_noun} of {title_adj}'


def fun_room_descriptions():
    des = random.choice(fun_room_description[0])
    return des

Room.objects.all().delete()



def create_world(w, room_amount):
    full_map = []
    map_row = []
    ra = room_amount
    map_row_size = 0
    full_map_height = 0
    while ra > 0:
        title = 'adv'
        description = 'des'
        r = Room(title = fun_room_titles(), description = fun_room_descriptions())
        r.save()
        if map_row_size == w:
            full_map.append(map_row)
            map_row_size = 0
            full_map_height += 1
            map_row = []
            map_row.append(r)
            r.x = map_row_size
            r.y = full_map_height
            map_row_size += 1
            ra -= 1
            print(f'{r.title} + {r.description} + x = {r.x} + y = {r.y}')
        elif map_row_size < w:
            map_row.append(r)
            r.x = map_row_size
            r.y = full_map_height
            map_row_size += 1
            ra -= 1
            print(f'{r.title} + {r.description} + x = {r.x} + y = {r.y}')
    print(full_map)
    for row in full_map:
        for node in row:
            y = node.y
            x = node.x
            # North
            if y > 0:
                if full_map[y - 1][x]:
                    node.connectRooms(full_map[y - 1][x], "n")
                    y = node.y
            # East
            if x < len(row) - 1:
                if full_map[y][x + 1]:
                    print(full_map[y][x + 1].id)
                    node.connectRooms(full_map[y][x + 1], "e")
                    x = node.x
            #South
            if y < len(full_map) - 1:
                if full_map[y + 1][x]:
                    node.connectRooms(full_map[y + 1][x], "s")
                    y = node.y
            #West
            if x > 0:
                if full_map[y][x - 1]:
                    node.connectRooms(full_map[y][x - 1], "w")
                    x = node.x
            node.save()
    return full_map

print(create_world(5, 50))