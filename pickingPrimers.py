with open("rawsequence.txt", "r") as seqFile:
    sequence = seqFile.read().replace('_', '')

dna = sequence.replace('\n', '')
newList = []
primer3file = open("primer3file", "w")
primer3file.truncate(0)
primer3file = open("primer3file", "a")

while True:
    name = input("Name the sequence: ")
    print("SEQUENCE_ID=" + name, file=primer3file)
    print("SEQUENCE_TEMPLATE=" + dna.lower(), file=primer3file)
    print("PRIMER_TASK=generic", file=primer3file)
    print("PRIMER_MAX_END_STABILITY=9.0", file=primer3file)
    print("PRIMER_MAX_SELF_ANY_TH=45.00", file=primer3file)
    print("PRIMER_MAX_SELF_END_TH=35.00", file=primer3file)
    print("PRIMER_PAIR_MAX_COMPL_ANY=45.00", file=primer3file)
    print("PRIMER_PAIR_MAX_COMPL_END=35.00", file=primer3file)
    print("PRIMER_TM_FORMULA=1", file=primer3file)
    print("PRIMER_SALT_CORRECTIONS=1", file=primer3file)
    print("PRIMER_SALT_MONOVALENT=50.0", file=primer3file)
    print("PRIMER_PICK_LEFT_PRIMER=1", file=primer3file)
    print("PRIMER_PICK_INTERNAL_OLIGO=0", file=primer3file)
    print("PRIMER_PICK_RIGHT_PRIMER=1", file=primer3file)
    print("PRIMER_OPT_SIZE=21", file=primer3file)
    print("PRIMER_MIN_SIZE=18", file=primer3file)
    print("PRIMER_MAX_SIZE=25", file=primer3file)
    print("PRIMER_MIN_TM=57.0", file=primer3file)
    print("PRIMER_OPT_TM=60.0", file=primer3file)
    print("PRIMER_MAX_TM=63.0", file=primer3file)
    print("PRIMER_PAIR_MAX_DIFF_TM=1.0", file=primer3file)
    print("PRIMER_MAX_HAIRPIN_TH=24.00", file=primer3file)
    print("PRIMER_MAX_TEMPLATE_MISPRIMING_TH=40.00", file=primer3file)
    print("PRIMER_MIN_GC=20.0", file=primer3file)
    print("PRIMER_MAX_GC=80.0", file=primer3file)
    print("PRIMER_PAIR_MAX_DIFF_TM=1.0", file=primer3file)
    print("PRIMER_SALT_MONOVALENT=50.0", file=primer3file)
    print("PRIMER_SALT_CORRECTIONS=1", file=primer3file)
    print("PRIMER_SALT_DIVALENT=1.5", file=primer3file)
    print("PRIMER_DNTP_CONC=0.6", file=primer3file)
    print("PRIMER_DNA_CONC=50.0", file=primer3file)
    print("PRIMER_THERMODYNAMIC_OLIGO_ALIGNMENT=1", file=primer3file)
    print("PRIMER_THERMODYNAMIC_TEMPLATE_ALIGNMENT=0", file=primer3file)
    print("PRIMER_LOWERCASE_MASKING=0", file=primer3file)
    while True:
        try:
            selection = input("a) 150-200\n"
                              "b) 200-250\n"
                              "c) 250-300\n"
                              "d) 300-350\n"
                              "e) Custom\n"
                              "\nSelect the letter for primer product size range: ").upper()
            if selection == 'A':
                print("PRIMER_PRODUCT_SIZE_RANGE=150-200", file=primer3file)
                break
            if selection == 'B':
                print("PRIMER_PRODUCT_SIZE_RANGE=200-250", file=primer3file)
                break
            if selection == 'C':
                print("PRIMER_PRODUCT_SIZE_RANGE=250-300", file=primer3file)
                break
            if selection == 'D':
                print("PRIMER_PRODUCT_SIZE_RANGE=300-350", file=primer3file)
                break
            if selection == 'E':
                while True:
                    try:
                        first = int(input("\nEnter the minimum of the size range: "))
                        if first > 499:
                            print("\n(x) Size range is too large, it has to be smaller than 500!\n")
                            continue
                        if first < 100:
                            print("\n(x) Size range is too small, it has to be at least 100!\n")
                            continue
                        else:
                            newList += [first]
                            break
                    except ValueError:
                        print("(!) Please enter an integer! ")
                        continue
                first = newList[0]
                while True:
                    try:
                        second = int(input("Enter the maximum of the size range: "))
                        if second > 500:
                            print("\n(x) Size range is too large, it has to be smaller or equal to 500!\n")
                            continue
                        if first > second:
                            print("\n(x) Maximum has to be larger than minimum.\n")
                            continue
                        if second < 100:
                            print("\n(x) Size range is too small, it has to be at least 100!")
                            continue
                        else:
                            newList += [second]
                            break
                    except ValueError:
                        print("(!) Please enter an integer! ")
                        continue
                second = newList[1]
                if first != 0 and second != 0 and first < second:
                    print("PRIMER_PRODUCT_SIZE_RANGE=" + str(first) + "-" + str(second), file=primer3file)
                    break
                else:
                    continue
            else:
                print("(x) Invalid input!\n")
        except ValueError:
            continue
    print("PRIMER_EXPLAIN_FLAG=1", file=primer3file)
    print("=", file=primer3file)
    primer3file.close()
    break
