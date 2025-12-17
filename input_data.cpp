#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string name, email, phone, education, experience, skills, hobbies;

    cout << "Enter your full name: ";
    getline(cin, name);

    cout << "Enter your email: ";
    getline(cin, email);

    cout << "Enter your phone number: ";
    getline(cin, phone);

    cout << "Enter your education details: ";
    getline(cin, education);

    cout << "Enter your work experience: ";
    getline(cin, experience);

    cout << "Enter your skills (comma-separated): ";
    getline(cin, skills);

    cout << "Enter your hobbies (comma-separated): ";
    getline(cin, hobbies);

    // Write data to resume_data.txt, overwrite if it already exists
    ofstream file("resume_data.txt", ios::trunc);
    if (file.is_open()) {
        file << name << endl;
        file << email << endl;
        file << phone << endl;
        file << education << endl;
        file << experience << endl;
        file << skills << endl;
        file << hobbies << endl;  // New line for hobbies
        file.close();
        cout << "\n? Resume data saved to 'resume_data.txt'." << endl;
    } else {
        cout << "? Unable to open file!" << endl;
    }

    return 0;
}

