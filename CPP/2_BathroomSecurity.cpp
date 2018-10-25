#include <string>
#include <fstream>
#include <iostream>

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
    if(x < 2) {
        x++;
    }
}
void Button::left(void) {
    if (x > 0) {
        x--;
    }
}
void Button::down(void) {
    if(y < 2) {
        y++;
    }
}
void Button::up(void) {
    if(y > 0) {
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
    num = 3*y + x + 1;
    return std::to_string(num);
}

int main() {   
    std::string stage;
    std::ifstream infile ("2_BathroomSecurity.txt");        // opens file
    
    Button button(-2,0);                                    
    
    while (getline(infile, stage)) {                        // stores line in string stage                    
        for (char& instr : stage) {                         // stores char in char instr
            button.move(instr);                             // moves cursor according to instr
        }
        std::string num = button.number();
        std::cout << num;                                   // displays current button
    }   
    infile.close();
    return 0;
};