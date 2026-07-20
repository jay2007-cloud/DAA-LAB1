#include <iostream> 
#include <fstream> 
int main() { 
    
    std::ofstream outFile("output.txt"); // Open file for writing 
    if (!outFile) { 
        std::cerr << "Error opening output file!" << std::endl; 
        return 1; 
    } 
 
    outFile << "Hello, File Streams!" << std::endl; 
    outFile << "This is a sample text." << std::endl; 
    outFile.close();  
 
     
    std::ifstream inFile("output.txt");  
    if (!inFile) { 
        std::cerr << "Error opening input file!" << std::endl; 
        return 1; 
    } 
 
 
 
    std::string line; 
    while (std::getline(inFile, line)) { 
        std::cout << line << std::endl; 
    } 
    inFile.close(); 
 
    return 0; 
}