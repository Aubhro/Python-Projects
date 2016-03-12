while True:

    #Virtual Machine Program
    #input register
    ir = 0
    #Program counter
    pc = 0
    acc = 0
    inp = 0
    out = 0

    #Defining Memory, creates list of 100 cells
    memory = [0] * 100
    memory[0]  = 1
    memory[99] = 800

    #Adding Program
    HDD = [34, 35, 134, 235, 636, 536, 900]

    #Absolute Value Program
    HDD = [34, 134, 312, 534, 900, 734, 734, 634, 534, 900]

    #Division Program 
    HDD = [34, 35, 134, 735, 634, 101, 200, 601, 134, 318, 809, 101, 700, 601, 501, 900]      

    #Function Sign Program
    HDD = [34, 134, 317, 700, 314, 500, 900, 200, 501, 900, 101, 700, 601, 501, 900]     

    #Natural Numbers Program
    HDD = [34, 100, 601, 134, 701, 318, 101, 200, 201, 601, 810, 101, 200, 200, 200, 601, 501, 900]
      
    #Transfer Program to Memory
    pc = 7

    for i in range(pc, len(HDD)+pc):
        memory[i] = HDD[i - pc]
    

    #Execute Instructions
    stop = False

    while stop == False:
    #Decode Instructions
        ir = memory[pc]
        pc = pc + 1
        opcode = ir / 100
        memorycode = ir % 100
        if opcode == 9:
            stop = True
        if opcode == 8:
            pc = memorycode
        if opcode == 7:
            acc = acc - memory[ memorycode]
        if opcode == 6:
            memory[memorycode] = acc
        if opcode == 5:
            out = memory[memorycode]
            print out
        if opcode == 4:
            left = memorycode / 10
            right = memorycode % 10
            acc = acc * (10**left) % 10000
            acc = acc * acc/(10**right)
        if opcode == 3:
            if acc < 0:
                pc = memorycode
        if opcode == 2:
            acc = acc + memory[memorycode]
        if opcode == 1:
            acc = memory[memorycode]
        if opcode == 0:
            memory[memorycode] = int(raw_input('input: \n'))                  




    
