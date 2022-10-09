from NumDeck import NumDeck

TOTAL_CNT = 100
TOTAL_TRY = 10000

myDeck = NumDeck(TOTAL_CNT)
myDeck.suffleDeck()
myDeck.printDeck()

try_pass = 0
try_fail = 0
max_fail_idx = 0

for i_try in range(1, TOTAL_TRY+1):
    myDeck.suffleDeck()
    trial_all_passed = True
    for i in range(1, TOTAL_CNT+1):
        result = myDeck.seekNumber(i)
        if (result == False):
            # print("Fail case found at trial {}, during searching {}".format(i_try, i))
            if (max_fail_idx < i):
                max_fail_idx = i
            trial_all_passed = False
            break
    
    if (trial_all_passed == True):
        try_pass = try_pass + 1
    else:
        try_fail = try_fail + 1


print("--------------")
print("Passed: {} / {}, rate: {:.3f}".format(try_pass, TOTAL_TRY, try_pass / TOTAL_TRY))
print("Failed: {} / {}, rate: {:.3f}".format(try_fail, TOTAL_TRY, try_fail / TOTAL_TRY))
print("Max Fail idx: ", max_fail_idx)