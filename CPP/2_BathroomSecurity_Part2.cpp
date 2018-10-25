#include <string>
#include <fstream>
#include <iostream>
// #include <iomanip>

class Button {
    public:
    Button(int xCoord, int yCoord);
    void right (void);
    void left (void);
    void down (void);
    void up (void);
    void move (char instr);
    std::string number (void);
        
    private:
        int x, y;
};
Button::Button(int xCoord, int yCoord) {
    x = xCoord;
    y = yCoord;
}
void Button::right(void) {
    if((x + abs(y)) < 2) {
        x++;
    }
}
void Button::left(void) {
    if ((-x + abs(y)) < 2) {
        x--;
    }
}
void Button::down(void) {
    if((y + abs(x)) < 2) {
        y++;
    }
}
void Button::up(void) {
    if((-y + abs(x)) < 2) {
        y--;
    }
}
void Button::move(char instr) {
    if(instr == 'R') {     right();}
    else if(instr == 'L') {left(); }
    else if(instr == 'U') {up();   }
    else if(instr == 'D') {down(); }
}
std::string Button::number(void) {
    int num;
    if(abs(y) == 1) {
        num = 7 + 4*y + x;
    }
    else {
        num = 7 + 3*y + x;
    }
    std::cout << std::hex << num;
}

int main() {   
    std::string stage;
    std::ifstream infile ("2_BathroomSecurity.txt");        // opens file
    
    Button button(-2,0);                                    
    
    while (getline(infile, stage)) {                        // stores line in string stage                    
        for (char& instr : stage) {                         // stores char in char instr
            button.move(instr);                             // moves cursor according to instr
        }
        button.number();                                    // displays current button
    }   
    infile.close();
    return 0;
};