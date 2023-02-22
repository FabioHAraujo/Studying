#include <iostream>
#include <iomanip>

class pessoa {
    private:
        int idade;
        int forca;
        int resistencia;
        char nome[];

    public:
        void setIdade(int idade){
            this->idade = idade;
        }
        void setForca(int forca){
            this->forca = forca;
        }
        void setResist(int resist){
            this->resistencia = resist;
        }
        int getInfo(){
            return idade, forca, resistencia;
        }
};