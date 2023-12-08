seed_to_soil = {}
soil_to_fertiliser = {}
fertiliser_to_water = {} 
water_to_light = {} 
light_to_temperature = {} 
temperature_to_humidity = {} 
humidity_to_location = {} 

maps = [seed_to_soil, soil_to_fertiliser, fertiliser_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location] 

def ingest_map_str(map_str, dest_map):
    range_lists = [s.split(' ') for s in map_str.strip().split('\n')[1:]]
    for range_list in range_lists:
        dest, src, r_len = [int(x) for x in range_list]
        dest_map[(src, src + r_len)] = dest

def get_src_from_dest(dest, dest_map):
    print(f'USING MAP {maps.index(dest_map)}')
    for (start, end) in dest_map.keys():
        if dest not in range(start, end):
            print(f'{dest} NOT in ({start}, {end})') 
            continue 
        print(f'{dest} IN ({start}, {end})') 
        return dest_map[(start, end)] + dest - start 
    print(f'DEFAULT {dest}') 
    return dest

seeds = [] 
with open('5-input.txt', 'r') as f:
    lines = f.readlines() 
    seeds += lines[0].split(':')[1].strip().split(' ')
    map_strs = ''.join(lines[1:]).split('\n\n')
    for i in range(len(map_strs)):
        ingest_map_str(map_strs[i], maps[i])

seeds = [int(s) for s in seeds]

for key in seed_to_soil.keys(): 
    print(f'{key} : {seed_to_soil[key]}')

for i in range(len(seeds)):
    for m in maps:
        print(f'MAP {maps.index(m)}')
        for key in m.keys():
            print(f'{key}: {m[key]}')
        seeds[i] = get_src_from_dest(seeds[i], m)

print(f'PART 1: {min(seeds)}')
