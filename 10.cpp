#include<iostream>
template<typename T>
T max(T a,T b){
    return(a>b)?a:b;
}
int main(){
    int intMax=max(5,10);
    double doubleMax=max(3.14,2.71);

    std::cout<<"maximum of 5 and 10 is:"<<intMax<<std::endl;
    std::cout<<"maximum of 3.14 and 2.71 is"<<doubleMax<<std::endl;
    return 0;
}