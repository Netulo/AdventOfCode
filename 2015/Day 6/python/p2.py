def switch_lights(instruction, lights):
    instruction_table = instruction.split(' ')
    start_range = [int(x) for x in instruction_table[-3].split(',')]
    end_range = [int(x) for x in instruction_table[-1].split(',')]
    brighttness_change = 0

    for i in range(start_range[1], end_range[1]+1):
        for j in range(start_range[0], end_range[0]+1):
            if instruction_table[1] == 'on':
                lights[i][j] += 1
                brighttness_change += 1
            elif instruction_table[1] == 'off':
                if lights[i][j] == 0: 
                    continue
                lights[i][j] -= 1
                brighttness_change -= 1
            else:
                lights[i][j] += 2
                brighttness_change += 2
                
    return brighttness_change
            
    # light_grid[:] = lights


light_grid = [[0 for i in range(1000)] for j in range(1000)]

input_string_table = open('2015/Day 6/input.txt', 'r').read().split('\n')

brightness = 0

for i in input_string_table:
    brightness += switch_lights(i, light_grid)
    
print(brightness)