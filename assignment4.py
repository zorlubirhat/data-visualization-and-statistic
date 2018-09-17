import matplotlib.pyplot as plot
import numpy as np
import random
import sys

infile = sys.argv[1]
nomin = str(sys.argv[2]).split(",")
#infile = "ElectionIran2009.csv"
#nomin = "Mousavi", "Karrubi", "Rezai"


def retrieveData(text, *nominees):

    global votes
    votes = []
    outfile = "retrievedData.txt"
    input_file = open(text, "r")
    output_file = open(outfile, "w")

    list = []
    list2 = []

    for line in input_file.readlines():
        item = line.rstrip("\n")
        items = item.split(",")
        list.append(items)
        list2 = list[0]

    for names in nominees:
        if names in list2:
            ind = list2.index(names)
            for i in list:
                if i[ind] == names:
                    pass
                else:
                    votes.append(i[ind])
                    output_file.write(i[ind])
                    output_file.write(" ")
    #print(votes)
    return votes

retrieveData(infile, *nomin)


def DispBarPlot():

    input_file = open(infile, "r")
    list = []
    list2 = []

    for line in input_file.readlines():
        item = line.rstrip("\n")
        items = item.split(",")
        list.append(items)
        list2 = list[0]

    names = list2
    names.pop(0)
    names.pop(0)

    states = []
    for i in list:
        states.append(i[0])
    states.pop(0)

    deger = []
    list.pop(0)
    for i in list:
        i.pop(0)
        i.pop(0)
        deger.append(i)

    nom1 = []
    nom2 = []
    for lst in deger:
        number = [int(i) for i in lst]
        max1 = max(number)
        ind1 = number.index(max1)
        number.remove(max1)
        max2 = max(number)
        number.insert(ind1, max1)
        ind2 = number.index(max2)

        if ind1 > ind2:
            nom2.append(number[ind1])
            nom1.append(number[ind2])
        else:
            nom2.append(number[ind2])
            nom1.append(number[ind1])

    x_pos = [x for x in range(len(states))]

    p1 = plot.bar(x_pos, nom1, align='edge', color="b", width=0.25)
    plot.xticks(x_pos, states, rotation=90, fontsize=10)

    p2 = plot.bar(x_pos, nom2, align='edge', color="r", width=-0.25)
    plot.xticks(x_pos, states)

    plot.ylabel("Vote Count")
    plot.xlabel("States", fontsize=10)
    plot.legend((p1[0], p2[0]), (names[ind2], names[ind1]))
    plot.tight_layout()
    plot.xlim()
    plot.savefig("ComparativeVotes.pdf")
    plot.close()
    plot.show()
    return
DispBarPlot()


def compareVoteonBar():

    input_file = open(infile, "r")
    list = []

    for line in input_file.readlines():
        item = line.rstrip("\n")
        items = item.split(",")
        list.append(items)

    votes = []
    names = []
    totals = []
    pers = []
    for name in list[0]:
        if name in nomin:
            ind = list[0].index(name)
            names.append(name)
            result = 0
            for i in list:
                if i[ind] == name:
                    pass
                else:
                    result += int(i[ind])
            votes.append(result)
    totalvote = 0
    for vote in votes:
        totalvote += vote
    totals.append(totalvote)
    for total in totals:
        for nomvote in votes:
            per = "%0.3f" % ((nomvote * 100) / total)
            pers.append(per)

    x_pos = [x for x in range(len(pers))]
    pers2 = [float(x) for x in pers]

    colors = ["r", "b", "y", "c"]

    p1 = plot.bar(x_pos, pers2, width=0.50, align="center", color=colors)

    plot.xticks(x_pos, pers2, fontsize=10)
    plot.ylabel("Vote Percentages")
    plot.xlabel("Nominees")
    plot.legend(p1, nomin)
    plot.xlim()
    plot.savefig("CompVotePercs.pdf")
    plot.close()
    plot.show()
    return

compareVoteonBar()


def obtainHistogram(givenlist):

    global obtainResult
    obtainResult = []
    digit = []
    for a in givenlist:
        digit.append(a[-2:])

    onedig = []
    twodig = []
    result1 = []
    zero = 0
    for b in digit:
        if int(b) < 10:
            zero += 1
            onedig.append(b[-1:])
        else:
            onedig.append(b[-1:])
            twodig.append(b[-2:-1])
    zero_count = 0
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    seven_count = 0
    eight_count = 0
    nine_count = 0
    for x in onedig:
        if x == '0':
            zero_count += 1
        elif x == '1':
            one_count += 1
        elif x == '2':
            two_count += 1
        elif x == '3':
            three_count += 1
        elif x == '4':
            four_count += 1
        elif x == '5':
            five_count += 1
        elif x == '6':
            six_count += 1
        elif x == '7':
            seven_count += 1
        elif x == '8':
            eight_count += 1
        elif x == '9':
            nine_count += 1
    for y in twodig:
        if y == '0':
            zero_count += 1
        elif y == '1':
            one_count += 1
        elif y == '2':
            two_count += 1
        elif y == '3':
            three_count += 1
        elif y == '4':
            four_count += 1
        elif y == '5':
            five_count += 1
        elif y == '6':
            six_count += 1
        elif y == '7':
            seven_count += 1
        elif y == '8':
            eight_count += 1
        elif y == '9':
            nine_count += 1
    zero_count += zero
    result1.insert(0, zero_count)
    result1.insert(1, one_count)
    result1.insert(2, two_count)
    result1.insert(3, three_count)
    result1.insert(4, four_count)
    result1.insert(5, five_count)
    result1.insert(6, six_count)
    result1.insert(7, seven_count)
    result1.insert(8, eight_count)
    result1.insert(9, nine_count)

    length = len(digit)
    for number in result1:
        frequency = (number / (2 * length))
        obtainResult.append(frequency)
    #print("frequencies: ", obtainResult)
    return obtainResult

obtainHistogram(votes)


def plotHistogram(result):

    liste = result
    total = 0
    count = 0

    for number in liste:
         total += float(number)
         count += 1
    mean = []
    mean2 = (total / count)
    mean.append(mean2)
    #print(mean)
    t = np.arange(0, len(liste))

    p1 = plot.plot(t, liste, 'r-', t, mean*len(liste), 'b--')
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    plot.title("Histogram of least sign. digits")
    plot.legend((p1[0], p1[1]), ('Digit Dist.', 'Mean'), loc='upper right')
    plot.savefig("Histogram.pdf")
    plot.close()
    plot.show()

    return mean

plotHistogram(obtainResult)


def plotHistogramWithSample():

    import random

    freq1 = []
    mean1 = []
    sized_ten = []

    for i in range(10):
        sized_ten.append("%d" % random.randint(0, 100))

    onedig1 = []
    twodig1 = []
    result1 = []

    zero1 = 0
    for a in sized_ten:
        if int(a) < 10:
            zero1 += 1
            onedig1.append(a[-1:])
        else:
            onedig1.append(a[-1:])
            twodig1.append(a[-2:-1])
    zero_count1 = 0
    one_count1 = 0
    two_count1 = 0
    three_count1 = 0
    four_count1 = 0
    five_count1 = 0
    six_count1 = 0
    seven_count1 = 0
    eight_count1 = 0
    nine_count1 = 0
    for x in onedig1:
        if x == '0':
            zero_count1 += 1
        elif x == '1':
            one_count1 += 1
        elif x == '2':
            two_count1 += 1
        elif x == '3':
            three_count1 += 1
        elif x == '4':
            four_count1 += 1
        elif x == '5':
            five_count1 += 1
        elif x == '6':
            six_count1 += 1
        elif x == '7':
            seven_count1 += 1
        elif x == '8':
            eight_count1 += 1
        elif x == '9':
            nine_count1 += 1
    for y in twodig1:
        if y == '0':
            zero_count1 += 1
        elif y == '1':
            one_count1 += 1
        elif y == '2':
            two_count1 += 1
        elif y == '3':
            three_count1 += 1
        elif y == '4':
            four_count1 += 1
        elif y == '5':
            five_count1 += 1
        elif y == '6':
            six_count1 += 1
        elif y == '7':
            seven_count1 += 1
        elif y == '8':
            eight_count1 += 1
        elif y == '9':
            nine_count1 += 1
    zero_count1 += zero1
    result1.insert(0, zero_count1)
    result1.insert(1, one_count1)
    result1.insert(2, two_count1)
    result1.insert(3, three_count1)
    result1.insert(4, four_count1)
    result1.insert(5, five_count1)
    result1.insert(6, six_count1)
    result1.insert(7, seven_count1)
    result1.insert(8, eight_count1)
    result1.insert(9, nine_count1)
    #print(result1)

    length1 = len(sized_ten)
    for num in result1:
        freq = "%0.3f" % (num / (2 * length1))
        freq1.append(freq)
    #print(freq1)
    total1 = 0
    count1 = 0
    for number in freq1:
        total1 += float(number)
        count1 += 1
        mean = "%0.3f" % (total1 / count1)
    mean1.append(mean)
    #print(mean1)

    freq2 = []
    mean2 = []
    sized_fifty = []

    for i in range(50):
        sized_fifty.append("%d" % random.randint(0, 100))

    onedig2 = []
    twodig2 = []
    result2 = []

    zero2 = 0
    for a in sized_fifty:
        if int(a) < 10:
            zero2 += 1
            onedig2.append(a[-1:])
        else:
            onedig2.append(a[-1:])
            twodig2.append(a[-2:-1])
    zero_count2 = 0
    one_count2 = 0
    two_count2 = 0
    three_count2 = 0
    four_count2 = 0
    five_count2 = 0
    six_count2 = 0
    seven_count2 = 0
    eight_count2 = 0
    nine_count2 = 0
    for x in onedig2:
        if x == '0':
            zero_count2 += 1
        elif x == '1':
            one_count2 += 1
        elif x == '2':
            two_count2 += 1
        elif x == '3':
            three_count2 += 1
        elif x == '4':
            four_count2 += 1
        elif x == '5':
            five_count2 += 1
        elif x == '6':
            six_count2 += 1
        elif x == '7':
            seven_count2 += 1
        elif x == '8':
            eight_count2 += 1
        elif x == '9':
            nine_count2 += 1
    for y in twodig2:
        if y == '0':
            zero_count2 += 1
        elif y == '1':
            one_count2 += 1
        elif y == '2':
            two_count2 += 1
        elif y == '3':
            three_count2 += 1
        elif y == '4':
            four_count2 += 1
        elif y == '5':
            five_count2 += 1
        elif y == '6':
            six_count2 += 1
        elif y == '7':
            seven_count2 += 1
        elif y == '8':
            eight_count2 += 1
        elif y == '9':
            nine_count2 += 1
    zero_count2 += zero2
    result2.insert(0, zero_count2)
    result2.insert(1, one_count2)
    result2.insert(2, two_count2)
    result2.insert(3, three_count2)
    result2.insert(4, four_count2)
    result2.insert(5, five_count2)
    result2.insert(6, six_count2)
    result2.insert(7, seven_count2)
    result2.insert(8, eight_count2)
    result2.insert(9, nine_count2)
    #print(result2)

    length2 = len(sized_fifty)
    for num in result2:
        freq = "%0.3f" % (num / (2 * length2))
        freq2.append(freq)
    #print(freq2)
    total2 = 0
    count2 = 0
    for number in freq2:
        total2 += float(number)
        count2 += 1
        mean = "%0.3f" % (total2 / count2)
    mean2.append(mean)
    #print(mean2)

    freq3 = []
    mean3 = []
    sized_hundred = []

    for i in range(100):
        sized_hundred.append("%d" % random.randint(0, 100))

    onedig3 = []
    twodig3 = []
    result3 = []

    zero3 = 0
    for a in sized_hundred:
        if int(a) < 10:
            zero3 += 1
            onedig3.append(a[-1:])
        else:
            onedig3.append(a[-1:])
            twodig3.append(a[-2:-1])
    zero_count3 = 0
    one_count3 = 0
    two_count3 = 0
    three_count3 = 0
    four_count3 = 0
    five_count3 = 0
    six_count3 = 0
    seven_count3 = 0
    eight_count3 = 0
    nine_count3 = 0
    for x in onedig3:
        if x == '0':
            zero_count3 += 1
        elif x == '1':
            one_count3 += 1
        elif x == '2':
            two_count3 += 1
        elif x == '3':
            three_count3 += 1
        elif x == '4':
            four_count3 += 1
        elif x == '5':
            five_count3 += 1
        elif x == '6':
            six_count3 += 1
        elif x == '7':
            seven_count3 += 1
        elif x == '8':
            eight_count3 += 1
        elif x == '9':
            nine_count3 += 1
    for y in twodig3:
        if y == '0':
            zero_count3 += 1
        elif y == '1':
            one_count3 += 1
        elif y == '2':
            two_count3 += 1
        elif y == '3':
            three_count3 += 1
        elif y == '4':
            four_count3 += 1
        elif y == '5':
            five_count3 += 1
        elif y == '6':
            six_count3 += 1
        elif y == '7':
            seven_count3 += 1
        elif y == '8':
            eight_count3 += 1
        elif y == '9':
            nine_count3 += 1
    zero_count3 += zero3
    result3.insert(0, zero_count3)
    result3.insert(1, one_count3)
    result3.insert(2, two_count3)
    result3.insert(3, three_count3)
    result3.insert(4, four_count3)
    result3.insert(5, five_count3)
    result3.insert(6, six_count3)
    result3.insert(7, seven_count3)
    result3.insert(8, eight_count3)
    result3.insert(9, nine_count3)
    #print(result3)

    length3 = len(sized_hundred)
    for num in result3:
        freq = "%0.3f" % (num / (2 * length3))
        freq3.append(freq)
    #print(freq3)
    total3 = 0
    count3 = 0
    for number in freq3:
        total3 += float(number)
        count3 += 1
        mean = "%0.3f" % (total3 / count3)
    mean3.append(mean)
    #print(mean3)

    freq4 = []
    mean4 = []
    sized_thousand = []

    for i in range(1000):
        sized_thousand.append("%d" % random.randint(0, 100))

    onedig4 = []
    twodig4 = []
    result4 = []

    zero4 = 0
    for a in sized_thousand:
        if int(a) < 10:
            zero4 += 1
            onedig4.append(a[-1:])
        else:
            onedig4.append(a[-1:])
            twodig4.append(a[-2:-1])
    zero_count4 = 0
    one_count4 = 0
    two_count4 = 0
    three_count4 = 0
    four_count4 = 0
    five_count4 = 0
    six_count4 = 0
    seven_count4 = 0
    eight_count4 = 0
    nine_count4 = 0
    for x in onedig4:
        if x == '0':
            zero_count4 += 1
        elif x == '1':
            one_count4 += 1
        elif x == '2':
            two_count4 += 1
        elif x == '3':
            three_count4 += 1
        elif x == '4':
            four_count4 += 1
        elif x == '5':
            five_count4 += 1
        elif x == '6':
            six_count4 += 1
        elif x == '7':
            seven_count4 += 1
        elif x == '8':
            eight_count4 += 1
        elif x == '9':
            nine_count4 += 1
    for y in twodig4:
        if y == '0':
            zero_count4 += 1
        elif y == '1':
            one_count4 += 1
        elif y == '2':
            two_count4 += 1
        elif y == '3':
            three_count4 += 1
        elif y == '4':
            four_count4 += 1
        elif y == '5':
            five_count4 += 1
        elif y == '6':
            six_count4 += 1
        elif y == '7':
            seven_count4 += 1
        elif y == '8':
            eight_count4 += 1
        elif y == '9':
            nine_count4 += 1
    zero_count4 += zero4
    result4.insert(0, zero_count4)
    result4.insert(1, one_count4)
    result4.insert(2, two_count4)
    result4.insert(3, three_count4)
    result4.insert(4, four_count4)
    result4.insert(5, five_count4)
    result4.insert(6, six_count4)
    result4.insert(7, seven_count4)
    result4.insert(8, eight_count4)
    result4.insert(9, nine_count4)
    #print(result4)

    length4 = len(sized_thousand)
    for num in result4:
        freq = "%0.3f" % (num / (2 * length4))
        freq4.append(freq)
    #print(freq4)
    total4 = 0
    count4 = 0
    for number in freq4:
        total4 += float(number)
        count4 += 1
        mean = "%0.3f" % (total4 / count4)
    mean4.append(mean)
    #print(mean4)

    freq5 = []
    mean5 = []
    sized_tenthousand = []

    for i in range(10000):
        sized_tenthousand.append("%d" % random.randint(0, 100))

    onedig5 = []
    twodig5 = []
    result5 = []

    zero5 = 0
    for a in sized_tenthousand:
        if int(a) < 10:
            zero5 += 1
            onedig5.append(a[-1:])
        else:
            onedig5.append(a[-1:])
            twodig5.append(a[-2:-1])
    zero_count5 = 0
    one_count5 = 0
    two_count5 = 0
    three_count5 = 0
    four_count5 = 0
    five_count5 = 0
    six_count5 = 0
    seven_count5 = 0
    eight_count5 = 0
    nine_count5 = 0
    for x in onedig5:
        if x == '0':
            zero_count5 += 1
        elif x == '1':
            one_count5 += 1
        elif x == '2':
            two_count5 += 1
        elif x == '3':
            three_count5 += 1
        elif x == '4':
            four_count5 += 1
        elif x == '5':
            five_count5 += 1
        elif x == '6':
            six_count5 += 1
        elif x == '7':
            seven_count5 += 1
        elif x == '8':
            eight_count5 += 1
        elif x == '9':
            nine_count5 += 1
    for y in twodig5:
        if y == '0':
            zero_count5 += 1
        elif y == '1':
            one_count5 += 1
        elif y == '2':
            two_count5 += 1
        elif y == '3':
            three_count5 += 1
        elif y == '4':
            four_count5 += 1
        elif y == '5':
            five_count5 += 1
        elif y == '6':
            six_count5 += 1
        elif y == '7':
            seven_count5 += 1
        elif y == '8':
            eight_count5 += 1
        elif y == '9':
            nine_count5 += 1
    zero_count5 += zero5
    result5.insert(0, zero_count5)
    result5.insert(1, one_count5)
    result5.insert(2, two_count5)
    result5.insert(3, three_count5)
    result5.insert(4, four_count5)
    result5.insert(5, five_count5)
    result5.insert(6, six_count5)
    result5.insert(7, seven_count5)
    result5.insert(8, eight_count5)
    result5.insert(9, nine_count5)
    #print(result5)

    length3 = len(sized_tenthousand)
    for num in result5:
        freq = "%0.3f" % (num / (2 * length3))
        freq5.append(freq)
    #print(freq5)
    total5 = 0
    count5 = 0
    for number in freq5:
        total5 += float(number)
        count5 += 1
        mean = "%0.3f" % (total5 / count5)
    mean5.append(mean)
    #print(mean5)

    t1 = np.arange(0, len(freq1))
    p1 = plot.plot(t1, freq1, 'r-', t1, mean1 * len(freq1), 'g--', linewidth=1.5)
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    plot.title("Histogram of least sign. digits - Sample:1 ")
    plot.legend((p1[0], p1[1]), ('Digit Dist.', 'Mean'), loc='upper left')
    plot.savefig("HistogramofSample1.pdf")
    plot.close()
    plot.show()

    t2 = np.arange(0, len(freq2))
    p2 = plot.plot(t2, freq2, 'b-', t2, mean2 * len(freq2), 'g--', linewidth=1.5)
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    plot.title("Histogram of least sign. digits - Sample:2 ")
    plot.legend((p2[0], p2[1]), ('Digit Dist.', 'Mean'), loc='upper left')
    plot.savefig("HistogramofSample2.pdf")
    plot.close()
    plot.show()

    t3 = np.arange(0, len(freq3))
    p3 = plot.plot(t3, freq3, 'y-', t3, mean3 * len(freq3), 'g--', linewidth=1.5)
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    plot.title("Histogram of least sign. digits - Sample:3 ")
    plot.legend((p3[0], p3[1]), ('Digit Dist.', 'Mean'), loc='upper left')
    plot.savefig("HistogramofSample3.pdf")
    plot.close()
    plot.show()

    t4 = np.arange(0, len(freq4))
    p4 = plot.plot(t4, freq4, 'c-', t4, mean4 * len(freq4), 'g--', linewidth=1.5)
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    plot.title("Histogram of least sign. digits - Sample:4 ")
    plot.legend((p4[0], p4[1]), ('Digit Dist.', 'Mean'), loc='upper left')
    plot.savefig("HistogramofSample4.pdf")
    plot.close()
    plot.show()

    t5 = np.arange(0, len(freq5))
    p5 = plot.plot(t5, freq5, 'm', t5, mean5 * len(freq5), 'g--', linewidth=1.5)
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    plot.title("Histogram of least sign. digits - Sample:5 ")
    plot.legend((p5[0], p5[1]), ('Digit Dist.', 'Mean'), loc='upper left')
    plot.savefig("HistogramofSample5.pdf")
    plot.close()
    plot.show()
    return

plotHistogramWithSample()


def calculateMSE(givelist1, givelist2):

    totalmse = 0
    for x in givelist1:
        for y in givelist2:
            mse = ((float(x) - float(y)) ** 2)
            totalmse += mse

    #print("MSE Value:", totalmse)
    return totalmse

real_MSE = calculateMSE(obtainResult, ['0.1'])


def multiple_list(size):        #for create 10000 list
    init_list = list()
    for i in range(0, size):
        init_list.append(list())
    return init_list

myList = multiple_list(10000)

for i in range(10000):
    for j in range(204):
        myList[i].append(str(random.randint(0, 100)))

frequency_result = [obtainHistogram(x) for x in myList]

MSE_result = [calculateMSE(y, ['0.1']) for y in frequency_result]


def compareMSEs(list_mse):

    output_file = open("myAnswer.txt", "w")

    list_mse = []
    list_mse.append(real_MSE)

    count_bigger = 0
    count_smaller = 0
    for x in MSE_result:
        for y in list_mse:
            if y >= x:
                count_bigger += 1
            else:
                count_smaller += 1
    p_value = count_smaller / len(MSE_result)

    print("MSE Value of 2012 USA election is {}".format(real_MSE))
    output_file.write("MSE Value of 2012 USA election is {}".format(real_MSE))
    print("The number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(count_bigger))
    output_file.write("\nThe number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(count_bigger))
    print("The number of MSE of random samples which are smaller than USA election MSE is {}".format(count_smaller))
    output_file.write("\nThe number of MSE of random samples which are smaller than USA election MSE is {}".format(count_smaller))
    print("2012 USA election rejection level p is {}".format(p_value))
    output_file.write("\n2012 USA election rejection level p is {}".format(p_value))

    if p_value < 0.05:
        print("Finding: We reject the null hypothesis at the p = {} level".format(p_value))
        output_file.write("\nFinding: We reject the null hypothesis at the p = {} level".format(p_value))
    else:
        print("Finding: There is no statistical evidence to reject null hypothesis")
        output_file.write("\nFinding: There is no statistical evidence to reject null hypothesis")

    output_file.close()
    return

compareMSEs(real_MSE)
