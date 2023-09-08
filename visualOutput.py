import functions

seqStr = open("rawsequence.txt", "r")
seqStart = seqStr.read()
seq = seqStart.strip()
seq = seq.replace("\n", "")

primerLeftStr = open("leftPrimer.txt", "r")
primerLeftStart = primerLeftStr.read()
primerLeft = primerLeftStart.strip()
leftReversed = primerLeft[::-1]

primerRightStr = open("rightPrimer.txt", "r")
primerRightStart = primerRightStr.read()
primerRight = primerRightStart.strip()
rightReversed = primerRight[::-1]

leftPrimerSeq = functions.leftPrimerAlign(primerRight, functions.GeneSwap(functions.ReverseSeq(
    functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                       functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed),
                                                            seq),
                       seq))))
rightPrimerSeq = functions.rightPrimerAlign(functions.GeneSwap(leftReversed), functions.GeneSwap(functions.ReverseSeq(
    functions.Trimming(functions.findStartingPosOfLeftPrimer(
        primerLeft, seq),
        functions.findEndingPosOfRightPrimer(
            functions.GeneSwap(rightReversed),
            seq),
        seq))))
trimmedSeq = functions.GeneSwap(
    functions.ReverseSeq(functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                                            functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed),
                                                                                 seq),
                                            seq)))

seq2 = functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                          functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed),
                                                               seq),
                          seq)

primerLeftStart = functions.findStartingPosOfLeftPrimer(primerLeft, seq)
primerRightEnd = functions.findEndingPosOfRightPrimer(functions.GeneSwap(primerRight[::-1]), seq)


def rawLeftPrimerAlign(primer, primerLeftStart, primerRightEnd, seq):
    int(primerLeftStart)
    int(primerRightEnd)
    primer.upper()
    seq.upper()
    leftPrimerVisual = ""
    leftPrimerVisual2 = ""
    newList = []
    for nuc in range(0, primerLeftStart):
        leftPrimerVisual += '-'
    newList += [leftPrimerVisual]
    newList += [primer]
    for nuc in range(primerLeftStart+len(primer), primerRightEnd):
        leftPrimerVisual2 += '|'
    newList += [leftPrimerVisual2]
    tempFinal = ''.join(newList)
    final = tempFinal.ljust(len(seq), '-')
    return final


def rawRightPrimerAlign(primer, primerLeftStart, primerRightEnd, seq):
    int(primerRightEnd)
    int(primerLeftStart)
    primer.upper()
    primer = primer[::-1]
    seq.upper()
    leftPrimerVisual = ""
    newList = []
    for nuc in range(0, primerLeftStart):
        leftPrimerVisual += '-'
    for nuc in range(primerLeftStart, primerRightEnd - len(primer)):
        leftPrimerVisual += '|'
    newList += [leftPrimerVisual]
    newList += [primer]
    tempFinal = ''.join(newList)
    final = tempFinal.ljust(len(seq), '-')
    return final


func = open("output.html", 'r+')
func.truncate(0)
func = open("output.html", "w")

func.write("<html>\n<head>\n<title> \nDNA visualization \
          \n</title>\n</head>  <link rel='stylesheet' href='style.css'>\
          \n<body> <p id=" + "content" + ">" + functions.leftPrimerAlign(primerLeft, seq2) + "\n" + seq2 + "\n" + functions.rightPrimerAlign(functions.GeneSwap(rightReversed), seq2) + "\n" + "</p>\
          \n<p id='content2'>" + leftPrimerSeq + "\n" + trimmedSeq + "\n" + rightPrimerSeq + "\n" + "</p>\
          \n<p id='content3'>" + rawLeftPrimerAlign(primerLeft, primerLeftStart, primerRightEnd, seq) + "\n" + seq + "\n" + rawRightPrimerAlign(functions.GeneSwap(primerRight),primerLeftStart, primerRightEnd, seq) + "\n" + "</p>\
          \n <h1 id='DNA'>Raw DNA strand: </h1> <p id='updated3'></p> <h1 id='trimmedDNA'>Trimmed DNA: </h1> <p id='updated'></p> <p id='updated2'></p> <h1 id='Comp'>Reverse Complementary trimmed DNA strand: </h1> <script src='script.js'></script></body></html>")

func.close()

