#c++ version
#include <iostream>
#using namespace std;

#double fac(int input) {
#    double output = 1;
#    double in = (double) input;
#    if (input == 1 || input == 0) {
#        return output;
#    }
#    return in * fac(input - 1);
#}
#int main() {
#    double output;
#    for (int people = 1; people <= 32; people++) {
#        for (int room1 = 0; room1 <= min(4, people); room1++) {
#            for (int room2 = 0; room2 <= min(4, people - room1); room2++) {
#                for (int room3 = 0; room3 <= min(4, people - room1 - room2); room3++) {
#                    for (int room4 = 0; room4 <= min(4, people - room1 - room2 - room3); room4++) {
#                        for (int room5 = 0; room5 <= min(4, people - room1 - room2 - room3 - room4); room5++) {
#                            for (int room6 = 0; room6 <= min(4, people - room1 - room2 - room3 - room4 - room5); room6++) {
#                                for (int room7 = 0; room7 <= min(4, people - room1 - room2 - room3 - room4 - room5 - room6); room7++) {
#                                    for (int room8 = 0; room8 <= min(4, people - room1 - room2 - room3 - room4 - room5 - room6 - room7); room8++) {
#                                        if (room1 + room2 + room3 + room4 + room5 + room6 + room7 + room8 == people) {
#                                            output += fac(people) / (fac(room1) * fac(room2) * fac(room3) * fac(room4) * fac(room5) * fac(room6) * fac(room7) * fac(room8));
#                                        } else if (room1 + room2 + room3 + room4 + room5 + room6 + room7 + room8 > people) {
#                                            cout << "wrong" << endl;
#                                            return 1;
#                                        }
#                                    }
#                                }
#                            }
#                       }
#                    }
#                }
#            }
#        }
#    }
#    cout << output << endl;
#    return 1;
#}
#output from c++ is 6.83539e+24

import math

output = 0

for people in range(1, 33):
    for room1 in range(0, min(5, people + 1)):
        for room2 in range(0, min(5, people - room1 + 1)):
            for room3 in range(0, min(5, people - room1 - room2 + 1)):
                for room4 in range(0, min(5, people - room1 - room2 - room3 + 1)):
                    for room5 in range(0, min(5, people - room1 - room2 - room3 - room4 + 1)):
                        for room6 in range(0, min(5, people - room1 - room2 - room3 - room4 - room5 + 1)):
                            for room7 in range(0, min(5, people - room1 - room2 - room3 - room4 - room5 - room6 + 1)):
                                for room8 in range(0, min(5, people - room1 - room2 - room3 - room4 - room5 - room6 - room7 + 1)):
                                    if (room1 + room2 + room3 + room4 + room5 + room6 + room7 + room8) == people:
                                        output += (math.factorial(people) / (math.factorial(room1) * math.factorial(room2) * math.factorial(room3) * 
                                        math.factorial(room4) * math.factorial(room5) * math.factorial(room6) * math.factorial(room7) * math.factorial(room8)))
                                    elif (room1 + room2 + room3 + room4 + room5 + room6 + room7 + room8) > people:
                                        print("wrong")
                                        quit()
print (output)



