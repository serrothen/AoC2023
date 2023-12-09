#include <iostream>
#include <fstream>
#include <string>
//#include <set>
#include <map>
#include <vector>
//#include <algorithm>
using namespace std;


string step(node0,network,direction):
  
  if (direction == "L") {
    node0 = network[node0][0];
  } else {
    node0 = network[node0][1];
  }

  return node0;

int main() {

  std::str fname {"test1.txt"};
  //std::str fname = "test2.txt";
  //std::str fname = "input.txt";

  std::map<string,std::vector<string>> network;
  std::string destination {"ZZZ"};
  int num_steps {0};
  bool arrived {false};

  std::ifstream file(fname);

  std::string path;
  file >> path;

  std::string line;

  file >> line;
//  while (std::getline(std::cin, line)) {
//    std::cout << line << std::endl;
//  }


      
    return 0;
}

