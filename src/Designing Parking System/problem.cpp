class ParkingSystem {
public:
    int big, medium, small;
    ParkingSystem(int big, int medium, int small) {
        this->big = big;
        this->medium = medium;
        this->small = small;
    }
    
    bool addCar(int carType) {
        if(carType == 1 && big >= 1) {
            big -= 1;
            return true;
        }
        else if(carType == 2 && medium >=1) {
            medium -= 1;
            return true;
        }
        else if(carType == 3 && small >= 1) {
            small -= 1;
            return true;
        }
        return false;
    }
};
