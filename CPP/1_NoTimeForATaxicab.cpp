#include <iostream>
#include <tuple>
#include <fstream>
#include <set>
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
        pair<int,int> getCoordinates(void);
        void storePosition(void);
        int drctn;
        int x, y;
        set<pair<int, int>> visited;
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
pair<int,int> Bunny::getCoordinates(void) {
    return make_pair(x, y);
}
void Bunny::storePosition(void) {
    visited.insert(make_pair(x, y));
}

int main() {
    Bunny bunny(0);
    string line = "";
     size_t pos = 0;
    string instr;
    
    ifstream infile("1_NoTimeForATaxicab.txt");             // opens file
    getline(infile, line, '#');                             // data stored in line
    
    bool foundHQ = false;
    
    while ((pos = line.find(", ")) != string::npos) {       // until there are delimiters left
        instr = line.substr(0, pos);                        // read string before delimiter (current instruction)
        line.erase(0, pos + 2);                             // erase instruction from string
        
        char drctn = instr.at(0);                           // drctn = instr[0]
        int steps = stoi(instr.substr(1, instr.length()));  // steps = instr[1:]
        bunny.turn(drctn);                                  // bunny turns drctn
        bunny.walk(steps);                                  // bunny walks steps
        
        if(!foundHQ) {                                      // if HQ not found yet
            pair<int,int> coords = bunny.getCoordinates();
            const bool is_in = bunny.visited.find(coords) != bunny.visited.end();
            if(!is_in) {                                    // and if position not already visited
                bunny.storePosition();
            }
            else {                                          // if position already visited
                cout << bunny.getDistance() << endl;        // display solution to Part2 (wrong)
                foundHQ = true;
            }
            bunny.storePosition();
        }
    }                                                       // one more for the last instruction
    char drctn = line.at(0);
    int steps = stoi(line.substr(1, line.length()));
    bunny.turn(drctn);
    bunny.walk(steps);
    
    cout << bunny.getDistance() << endl;                    // solution to Part1
    return 0;
};