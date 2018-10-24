#include <iostream>
#include <tuple>
#include <fstream>
using namespace std;

// main() is where program execution begins.
class Bunny {
    public:
        Bunny(int direction);
        void turnRight(void);
        void turnLeft(void);
        void turn(char direction);
        void walk(int steps);
        int getDistance(void);
        tuple<int,int> getCoordinates(void);
        int drctn;
        int x, y;
};
Bunny::Bunny(int direction) {
    drctn = direction;
    x = 0; y = 0;
} 
void Bunny::turnRight(void) {
    drctn = (drctn + 1) % 4;
}
void Bunny::turnLeft(void) {
    drctn = (drctn - 1) % 4;
}
void Bunny::turn(char direction) {
    if(direction == 'R') {
        turnRight();
    }
    else if(direction == 'L') {
        turnLeft();
    }
}
void Bunny::walk(int steps) {
    if(drctn == 0) {
        y += steps; 
    }
    else if(drctn == 1 || drctn == -3) {
        x += steps;
    }
    else if(drctn == 2 || drctn == -2) {
        y -= steps;
    }
    else if(drctn == 3 || drctn == -1) {
        x -= steps;
    }
}
int Bunny::getDistance(void) {
    return abs(x) + abs(y);
}
tuple<int,int> Bunny::getCoordinates(void) {
    return make_tuple(x, y);
}

int main() {
    Bunny bunny(0);
    ifstream infile("1_NoTimeForATaxicab.txt"); // opens file
    string line = "";
    getline(infile, line, '#');                 // data stored in line
    size_t pos = 0;
    string instr;
    while ((pos = line.find(", ")) != string::npos) {   // until there are delimiters left
        instr = line.substr(0, pos);            // read string before delimiter (current instruction)
        line.erase(0, pos + 2);                 // erase instruction from string
        
        char drctn = instr.at(0);               // drctn = instr[0]
        int steps = stoi(instr.substr(1, instr.length()));  // steps = instr[1:]
        bunny.turn(drctn);
        bunny.walk(steps);
    }                                           // one more for the last instruction
    char drctn = line.at(0);
    int steps = stoi(line.substr(1, line.length()));
    bunny.turn(drctn);
    bunny.walk(steps);
    
    cout << bunny.getDistance() << endl;
    return 0;
};