#include <iostream>
#include <string>
using namespace std;

// Node Declaration
struct node {
    string label;         // Name of the node
    int ch_count;         // Number of children
    struct node *child[10]; // Array of pointers to child nodes
} * root;

// Class Declaration
class GT {
public:
    GT() {
        root = NULL; // Initialize the root to NULL
    }

    void create_tree(); // Method to create the tree structure
    void display(node *r1); // Method to display the tree
};

// Method to create the tree
void GT::create_tree() {
    root = new node;

    cout << "Enter name of book: ";
    cin.get(); // Clear input buffer
    getline(cin, root->label);

    cout << "Enter number of chapters in book: ";
    cin >> root->ch_count;

    for (int i = 0; i < root->ch_count; i++) {
        root->child[i] = new node;

        cout << "Enter the name of Chapter " << i + 1 << ": ";
        cin.get(); // Clear input buffer
        getline(cin, root->child[i]->label);

        cout << "Enter number of sections in Chapter " << root->child[i]->label << ": ";
        cin >> root->child[i]->ch_count;

        for (int j = 0; j < root->child[i]->ch_count; j++) {
            root->child[i]->child[j] = new node;

            cout << "Enter Name of Section " << j + 1 << ": ";
            cin.get(); // Clear input buffer
            getline(cin, root->child[i]->child[j]->label);
        }
    }
}

// Method to display the tree
void GT::display(node *r1) {
    if (r1 != NULL) {
        cout << "\n----- Book Hierarchy -----\n";
        cout << "Book Title: " << r1->label << "\n";

        for (int i = 0; i < r1->ch_count; i++) {
            cout << "Chapter " << i + 1 << ": " << r1->child[i]->label << "\n";

            cout << "Sections: ";
            for (int j = 0; j < r1->child[i]->ch_count; j++) {
                cout << "\n  " << r1->child[i]->child[j]->label;
            }
            cout << "\n";
        }
    }
}

// Main Function
int main() {
    GT gt; // Create an instance of the General Tree class
    int choice;

    while (true) {
        cout << "\n-----------------\n";
        cout << "Book Tree Creation\n";
        cout << "-----------------\n";
        cout << "1. Create\n";
        cout << "2. Display\n";
        cout << "3. Quit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            gt.create_tree();
            break;

        case 2:
            gt.display(root);
            break;

        case 3:
            cout << "Thanks for using this program!!!\n";
            return 0;

        default:
            cout << "Invalid choice! Please select a valid option.\n";
        }
    }
}
