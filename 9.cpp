#include <iostream> 
#include <vector> 
#include <stdexcept> 
template <typename T> 
class Stack { 
private: 
    std::vector<T> data; 
 
public: 
    void push(const T& value) { 
        data.push_back(value); 
    } 
 
    void pop() { 
        if (!data.empty()) { 
            data.pop_back(); 
        } 
    } 
 
    T top() const { 
        if (!data.empty()) { 

 
            return data.back(); 
        } 
        throw std::runtime_error("Stack is empty"); 
    } 
 
    bool empty() const { 
        return data.empty(); 
    } 
 
    size_t size() const { 
        return data.size(); 
    } 
}; 
 
int main() { 
    Stack<int> intStack; 
    Stack<double> doubleStack; 
 
    intStack.push(10); 
    intStack.push(20); 
    intStack.push(30); 
 
    doubleStack.push(3.14); 
    doubleStack.push(2.71); 
 
    std::cout << "Int Stack Size: " << intStack.size() << std::endl; 
    std::cout << "Top of Int Stack: " << intStack.top() << std::endl; 
    intStack.pop(); 
 
    std::cout << "Double Stack Size: " << doubleStack.size() << std::endl; 
    std::cout << "Top of Double Stack: " << doubleStack.top() << std::endl; 
    doubleStack.pop(); 
 
    return 0; 
}